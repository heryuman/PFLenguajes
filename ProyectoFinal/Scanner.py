import Token
import GeneraHTML
import Myparser
import CreateGraphviz

espacios=0
fila = 1
columna = 0
ListTokens = []
ListaErrores=[]

lexema = ""


def analizadorLexico(entrada):
    print("Analalizando")
    global lexema
    global columna
    global espacios
    global fila
    if len(ListTokens)>0:
        ListTokens.clear()
        fila=1
        columna=0
        print('se borro la lista')
    elif len(ListaErrores)>0:
        ListaErrores.clear()

    caracteres = list(entrada + "#")
    estado = 0
    i=0
    while i < len(caracteres):


        columna += 1
       # print("posicion ",i ,caracteres[i]," el ascii ",ord(caracteres[i]))


        if estado == 0:
            #print(caracteres[i],"posicion ", i)
            if caracteres[i].isalpha():
                #print("el caracter leido si letra: ",caracteres[i])
                estado = 1
                lexema += caracteres[i]
            elif caracteres[i] == '_':
                #print("el caracter leido si guionB: ", caracteres[i])
                estado = 1
                lexema += caracteres[i]



            elif caracteres[i].isdigit():
                #print("el caracter leido si digito: ", caracteres[i])
                estado = 2
                #  print("digitos")
                lexema += caracteres[i]

            elif caracteres[i]== "\n":

                fila+=1
                columna=0
                espacios=0

            elif ord(caracteres[i]) == 32:
                espacios+=1
                #print("hay ",espacios, " espacios en estado ",estado)

            elif caracteres[i] == "=":
               # print("el caracter leido si signo igual: ", caracteres[i])
                lexema += caracteres[i]


                agregarToken("tk_sigIgual", lexema,"Token de tipo simbolo",fila, columna-1)
                estado = 0


            elif caracteres[i] == "{":
                #print("el caracter leido: si { ", caracteres[i])
                lexema += caracteres[i]

                agregarToken("tk_LlaveA", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0

            elif caracteres[i] == ":":

                lexema += caracteres[i]

                agregarToken("tk_dosP", lexema, "Token de tipo simbolo", fila, columna - 1)
                estado = 0

            elif caracteres[i] == "}":
              #  print("el caracter leido si }: ", caracteres[i])
                lexema += caracteres[i]

                agregarToken("tk_LlaveC", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0

            elif caracteres[i] == "(":
              #  print("el caracter leido si (: ", caracteres[i])
                lexema += caracteres[i]
                #   print("token parentesis")
                agregarToken("tk_parA", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0

            elif caracteres[i] == "/":
               # print("el caracter leido: si / ", caracteres[i])
                estado = 5


            elif caracteres[i]== ";":
              #  print("Pto y coma leiodo ", caracteres[i])

                lexema += caracteres[i]

                agregarToken("tk_PtoYcoma", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0

            elif caracteres[i] == ")":
                lexema += caracteres[i]
                agregarToken("tk_parC", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0




            elif caracteres[i]== ">" :
                lexema += caracteres[i]
                agregarToken("tk_mayorQ", lexema,"Token de tipo simbolo", fila, columna-1)
                estado = 0

            elif caracteres[i] == ",":
                lexema += caracteres[i]
                agregarToken("tk_coma", lexema, "Token de tipo simbolo",fila, columna-1)
                estado = 0


            elif caracteres[i] == '\"':
                estado = 4

            else:

                if caracteres[i] != "#" and caracteres[i] != "\t":
                    lexema += caracteres[i]
                    errores="error lexico con: "+ str(lexema) +" en la fila: " +str(fila) + " y columna: "+ str(columna,)
                    print(errores)
                    ListaErrores.append(errores)
                    lexema = ""

                else:
                    if caracteres[i] == "#":
                        print("Analisis Exitoso!")


        elif estado == 1:
            if caracteres[i].isalpha():
                # print("el caracter leido: ", caracteres[i])
                estado = 1
                lexema = lexema + caracteres[i]

            elif caracteres[i] == '_':
                estado = 1
                lexema = lexema + caracteres[i]

            elif caracteres[i].isdigit():
                estado = 1
                lexema = lexema + caracteres[i]

            elif ord(caracteres[i]) == 32:
                espacios+=1
              #  print("hay ",espacios, " espacios en estado ",estado)
                agregarToken(EsReservada(lexema), lexema,"token que contiene un valor de tipo "+str(EsReservada(lexema)), fila, columna-1)
                estado = 0

            else:
               # print(EsReservada(lexema))
                agregarToken(EsReservada(lexema), lexema,"token que contiene un valor de tipo "+str(EsReservada(lexema)),fila,columna-1)
                estado = 0
                i -= 1

        elif estado == 2:
            #print(caracteres[i])
            if caracteres[i].isdigit():
                lexema += caracteres[i]
            elif caracteres[i] == '.':
                lexema += caracteres[i]
                estado = 3

            else:
                agregarToken("tk_Numero", lexema,"Token que contiene un valor de tipo Numerico", fila, columna-1)
                i -= 1
                estado = 0

        elif estado == 3:
           # print(caracteres[i])
            if caracteres[i].isdigit():
                lexema += caracteres[i]
                estado = 2

        elif estado == 4:
            #print(caracteres[i])
            if caracteres[i].isalpha():
                lexema += caracteres[i]
                estado = 4

            elif simbolos(caracteres[i]):
                lexema += caracteres[i]
                estado = 4

            elif caracteres[i].isdigit():
                lexema += caracteres[i]
                estado = 4

            elif caracteres[i] == " ":
                lexema += caracteres[i]
                estado = 4

            elif caracteres[i] == '"':
                agregarToken("tk_Cadena", lexema,"Token que contiene valor de tipo cadena", fila, columna-1)
                estado = 0

            elif caracteres[i] == '*':
                estado = 5

        elif estado == 5:
            if caracteres[i] == '*':
                # agregarToken("tk_Asterisco",lexema,fila,columna)
                estado = 4

            elif caracteres[i] == '/':
                agregarToken("tk_Comentario", lexema,"Token que contiene un comentario", fila, columna-1)
                estado = 0

        i+=1

def agregarToken(tipo, valor,descripcion, fila, columna):
    global lexema
    global ListTokens
    tk = Token.TipoToken(tipo, valor,descripcion, fila, columna)
    ListTokens.append(tk)

    lexema = ""


def simbolos(simbolo):
    Essimbolo = False
    symbl = [';', '/', '=', '>', '(', ')', '{', '}', '.', ' ']
    for i in range(0, len(symbl)):
        if symbl[i] == simbolo:
            Essimbolo = True


    return Essimbolo


def EsReservada(comparar):
    diccionario = ['SCRIPT', 'LANGUE', 'var', 'let', 'const', 'if', 'while', 'foreach', 'case', 'switch', 'break',
                   'default', 'in','print','true','false',]
    tipo = "tk_Id"
    for i in range(0, len(diccionario)):
        if diccionario[i] == comparar:
            tipo = "tk_"+comparar

    return tipo


def ImprimirListaToknes():
    for i in range(0, len(ListTokens)):
        print("*/*/*/*/*/*/ INICIO DEL TOKEN /*/*/*/*/*/*")
        print("Tipo de Token ", ListTokens[i].getTipo())
        print("Valor del Token ", ListTokens[i].getvalor())
        print("Desc. del token", ListTokens[i].getDescripcion())
        print("Fila ", ListTokens[i].getFila())
        print("columna ", ListTokens[i].getColumna())
        print("*/*/*/*/*/*/ FIN DEL TOKEN /*/*/*/*/*/*")
        print()

def ImprimirListaErrores():
    print("*/*/*/*/*/*/*/ LISTA DE ERRORES LEXICOS */*/*/*/*/*/*/*/")
    for i in range(0,len(ListaErrores)):
        print(ListaErrores[i])

    print("*/*/*/*/*/*/ FIN LISTA DE ERRORES */*/*/*/*/")


def ReporteTokens():
    GeneraHTML.html_create(ListTokens)

def ReporteErrores():
    if len(ListaErrores)>0:
        GeneraHTML.Errores_html_create(ListaErrores)

def LlamarParser():

    print("LLAMANDO AL PARSER")
    Myparser.AutomatadePila(ListTokens)

def GeneararGrafo():
    print("Generando el grafo")
    CreateGraphviz.unGrafo(ListTokens)


