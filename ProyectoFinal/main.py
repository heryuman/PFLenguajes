import Scanner
mensaje = ""
import CreateGraphviz
entrada = " {  \n [a]    >] \n n; l; , }"
def saludo():
    print('*/*/*/*/*/*/*/*/* BIENVENIDO ---- PROYECTO FINAL LENGUAJES FORMALES/*/*/*/*/*/*/*/*/*/*/*')
    print('Elija una opcion:')
    print('1.- Cargar un Script JS')
    print('2.- Manejo AFD')
    print('3.- Pila Interactiva')
    print('4.- Diagrama a bloques del codigo')
    print('Q.- para salir')

def menu():

    while True:
        saludo()
        eleccion = input()
        if eleccion == '1':
            loadScript()
        elif eleccion == '2':
            ManejoAFD()
        elif eleccion == '3':
            PilaInteractiva()
        elif eleccion =='4':
            DiagrmaBloques()
        elif eleccion == 'q' or eleccion == 'Q':
            break
        else:
            print("Error!, por favor ingrese una opcion valida")

def loadScript():
    global mensaje
    print("ingrese una direccion Valida para el script:")
    pathfile = input()
    #f = open('C:/Users/ASUS/Documents/Repositorios/Lenguajes/ProyectoFinal/prueba3.js', 'r')
    f = open(pathfile, 'r')
    mensaje = f.read()
    #print(mensaje)
    f.close()
    print('Script Cargado con exito!')

    #Scanner.ImprimirListaToknes()
    #Scanner.ImprimirListaErrores()


   # CreateGraphviz.unGrafo()
    #Scanner.GeneararGrafo()

def ManejoAFD():
    Scanner.analizadorLexico(mensaje)
    Scanner.ReporteTokens()
    Scanner.ReporteErrores()
    print("Reportes generados con exito,en la siguiente ruta: ProyectoFinal\Reportes")

def PilaInteractiva():
    Scanner.LlamarParser()

def DiagrmaBloques():
    Scanner.GeneararGrafo()

if __name__ == '__main__':
    menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
