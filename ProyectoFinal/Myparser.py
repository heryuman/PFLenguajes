#METER A LA PILA SOLO REGLAS QUE SE NECESITEN

def AutomatadePila(ListadeTokens):
    entrada=list(ListadeTokens)
    Analizando = True
    produccionM=['tk_PtoYcoma','B','tk_sigIgual','tk_Id','A']
    produccionN=['S','tk_LlaveC','S','tk_LlaveA','tk_parC','L','tk_parA','tk_if']
    produccionO=['S','tk_LlaveC','S','tk_LlaveA','tk_parC','L','tk_parA','tk_while']
    produccionR=['S','tk_LlaveC','S','tk_LlaveA','tk_parC','tk_Id','tk_in','tk_Id','tk_parA','tk_foreach']
    produccionX=['S','tk_LlaveC','K','tk_LlaveA','tk_parC','tk_Id','tk_parA','tk_switch']
    produccionP=['K','D','S','tk_dosP','B','tk_case']
    produccionW=['K','D','S','tk_dosP','tk_default']
    produccionY=['S','tk_LlaveC','S','tk_LlaveA','tk_mayorQ','tk_sigIgual','tk_parC','C','tk_parA','tk_sigIgual','tk_Id','A']
    produccionZ=['S','tk_PtoYcoma','tk_parC','I','tk_parA','tk_Id']

    pila = []

    it = (len(pila) - 1)
    n = 0  # iterador de la lista de entrada
    estado = "i"
    print("presione ENTER para continuar con el analisis")
    while Analizando == True:

        input()
        # Estado inicial del Automata, agrega el simbolo de aceptacion
        if estado == "i":

            print("PILA: ", 'λ')
            print("ENTRADA: ",entrada[n].getTipo())
            print("TRANSICION: i", ',λ , λ', ";", " p,", "#")
            print("--------------------")

            pila.append('#')
            estado = "p"


        # Estado p agrega el simbolo inicial de la gramatica sobre el simbolo de aceptacion
        elif estado == "p" and pila[0] == "#":

            print("PILA: ", pila)
            print("ENTRADA: ",entrada[n].getTipo())
            print("TRANSICION: p", ", λ, ", pila[it], ";", estado, ",S")
            print("--------------------")


            pila.append("S")
            estado = "q"



        elif estado == "q":
            # con input() pedimos secuencia de enters
            if pila[it]=="S" and entrada[n].getTipo() == "tk_var" and entrada[n+3].getTipo()!="tk_mayorQ":
                print("PILA: ", pila)
                print("ENTRADA: ",entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",MS")
                print("--------------------")

                pila.pop(it)
                pila.append("S")
                pila.append("M")
                #print(pila)

            elif pila[it]=="S" and entrada[n].getTipo()== "tk_let"and entrada[n+3].getTipo()!="tk_parA" :

                print("PILA: ", pila)
                print("ENTRADA: ",entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",MS")
                print("--------------------")

                pila.pop(it)
                pila.append("S")
                pila.append("M")
               # print(pila)

            elif pila[it]=="S"and entrada[n].getTipo() == "tk_const"and entrada[n+3].getTipo()!="tk_parA":
                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",MS")
                print("--------------------")

                pila.pop(it)
                pila.append("S")
                pila.append("M")
                #print(pila)

            elif pila[it] == "S" and entrada[n].getTipo() == "tk_var" and entrada[n + 3].getTipo() == "tk_parA":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",Y")
                print("--------------------")
                pila.pop(it)
                pila.append("Y")
               # print(pila)

            elif pila[it] == "S" and entrada[n].getTipo() == "tk_let" and entrada[n + 3].getTipo() == "tk_parA":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",Y")
                print("--------------------")

                pila.pop(it)
                pila.append("Y")
               # print(pila)

            elif pila[it] == "S" and entrada[n].getTipo() == "tk_const" and entrada[n + 3].getTipo() == "tk_parA":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",Y")
                print("--------------------")

                pila.pop(it)
                pila.append("Y")
                #print(pila)

            elif pila[it] == "S" and entrada[n].getTipo() == "tk_Id":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",Z")
                print("--------------------")

                pila.pop(it)
                pila.append("Z")
                #print(pila)



            elif pila[it]=="S"and entrada[n].getTipo()== "tk_if":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",N")
                print("--------------------")


                pila.pop(it)
                pila.append("N")
               # print(pila)

            elif pila[it]=="S"and entrada[n].getTipo()== "tk_while":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",O")
                print("--------------------")
                pila.pop(it)
                pila.append("O")
                #print(pila)

            elif entrada[n].getTipo() == "tk_LlaveC" and pila[it] == "K":
                pila.pop(it)


            elif pila[it]=="S"and entrada[n].getTipo()== "tk_foreach":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",R")
                print("--------------------")
                pila.pop(it)
                pila.append("R")
                #print(pila)

            elif pila[it]=="S"and entrada[n].getTipo()== "tk_switch":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",X")
                print("--------------------")
                pila.pop(it)
                pila.append("X")
                print(pila)



            elif pila[it] == "S" and entrada[n].getTipo() == "tk_case":
                pila.pop(it)
               # print(pila)

            elif pila[it] == "S" and entrada[n].getTipo() == "tk_break":
                pila.pop(it)
              #  print(pila)



            elif pila[it] == "I" and entrada[n].getTipo()=="tk_parC":
                pila.pop(it)

            elif pila[it]== "S"and entrada[n].getTipo()== "tk_LlaveC":
                pila.pop(it)



            elif pila[it]== "S" and len(entrada)-1 == n:
                pila.pop(it)


            elif entrada[n].getTipo() == "tk_Comentario":
                n+=1

# ingresamos las producciones que consiguen una definicion de variable
            elif pila[it]== "M":
                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",",produccionM)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionM)
                #print(pila)
#producciones para  el if
            elif pila[it] == "N":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionN)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionN)
              #  print(pila)

#Producciones para while
            elif pila[it] == "O":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionO)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionO)
                print(pila)

#producciones para for
            elif pila[it] == "R":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionR)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionR)
                #print(pila)


#produccioens para switch
            elif pila[it] == "X":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionX)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionX)
               # print(pila)

            elif pila[it]== "K" and entrada[n].getTipo() == "tk_case":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionW)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionP)
                #print(pila)

            elif pila[it] == "K" and entrada[n].getTipo() == "tk_default":
                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionW)
                print("--------------------")

                pila.pop(it)
                pila.extend(produccionW)
               # print(pila)

#produccion para definicion de funciones

            elif pila[it]== "Y":

                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionY)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionY)


            elif pila[it]== "C":
               # print("sustituyendo C")
                if entrada[n].getTipo() == "tk_Id" and entrada[n+1].getTipo() == "tk_coma":

                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ", C, tk_coma,tk_Id")
                    print("--------------------")

                    pila.pop(it)
                    pila.append("C")
                    pila.append("tk_coma")
                    pila.append("tk_Id")
                 #   print(pila)

                elif entrada[n].getTipo() == "tk_Id" and entrada[n+1].getTipo() == "tk_parC":

                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Id")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Id")
                   # print(pila)

# producciones para llamadas de funciones
            elif pila[it] == "Z":
                print("PILA: ", pila)
                print("ENTRADA: ", entrada[n].getTipo())
                print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",", produccionZ)
                print("--------------------")
                pila.pop(it)
                pila.extend(produccionZ)

            elif pila[it] == "I":
                if entrada[n+1].getTipo()== "tk_coma":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",I,tk_coma,B2")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("I")
                    pila.append("tk_coma")
                    pila.append("B2")

                elif entrada[n+1].getTipo()== "tk_parC":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",B2")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("B2")

            elif pila[it] == "B2":
               # print("sustituyendo B2")
                if entrada[n].getTipo() == "tk_Numero":

                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Numero")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Numero")
                  #  print(pila)

                elif entrada[n].getTipo() == "tk_Cadena":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Cadena")
                    print("--------------------")
                    pila.pop(it)
                    pila.append(("tk_Cadena"))
                   # print(pila)

                elif entrada[n].getTipo() == "tk_true":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_true")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_true")
                    #print(pila)

                elif entrada[n].getTipo() == "tk_false":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_false")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_false")

                elif entrada[n].getTipo() == "tk_Id":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Id")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Id")



            #Bloque de declaracion de variables
            elif pila[it] ==  "A":
               # print("sustituyendo A")
                if entrada[n].getTipo() == "tk_let":

                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_let")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_let")
                  #  print(pila)

                elif entrada[n].getTipo() == "tk_const":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_const")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_const")
                   # print(pila)

                elif entrada[n].getTipo() == "tk_var":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_var")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_var")
                    #print(pila)

            elif pila[it] == "B":
                #print("sustituyendo B")
                if entrada[n].getTipo() == "tk_Numero":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Numero")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Numero")
                    #print(pila)

                elif entrada[n].getTipo() == "tk_Cadena":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Cadena")
                    print("--------------------")
                    pila.pop(it)
                    pila.append(("tk_Cadena"))
                    print(pila)

                elif entrada[n].getTipo() == "tk_true":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_true")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_true")
                    print(pila)

                elif entrada[n].getTipo() == "tk_false":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_false")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_false")

#fin del Bloque declaracion de variables

#bloque que compara dentro del parentesis de if/while
            elif pila[it] == "L":
                #print("sustituyendo L")
                if entrada[n].getTipo()== "tk_Id":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Id")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Id")
                  #  print(pila)

                elif entrada[n].getTipo()== "tk_false":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_false")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_false")
                  #  print(pila)

                elif entrada[n].getTipo() == "tk_true":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_true")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_true")
                    #print(pila)





#bloque  de los case

            elif pila[it] == "D":
               # print("sustituyendo D")
                if entrada[n].getTipo() == "tk_break":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_PtoYcoma,tk_break")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_PtoYcoma")
                    pila.append("tk_break")




                if entrada[n].getTipo() == "tk_case":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",K")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("K")
                   # print(pila)




                elif entrada[n].getTipo() == "tk_LlaveC":
                    pila.pop(it)
                    #print(pila)

            elif pila[it] == "J":
              #  print("sustituyendo J")
                if entrada[n].getTipo() == "tk_Numero":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_Numero")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_Numero")
                   # print(pila)

                elif entrada[n].getTipo() == "tk_false":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_false")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_false")
                    #print(pila)

                elif entrada[n].getTipo() == "tk_true":
                    print("PILA: ", pila)
                    print("ENTRADA: ", entrada[n].getTipo())
                    print("TRANSICION: q", ", λ, ", pila[it], ";", estado, ",tk_true")
                    print("--------------------")
                    pila.pop(it)
                    pila.append("tk_true")
                  #  print(pila)







#bloque que lee la entrada compara en la pila y elimina de la pila
            elif entrada[n].getTipo() == pila[it]:
               # print("El simbolo en el Top de la Pila: ",pila[it]," El simbolo en la entrada: ",entrada[n])
               print("PILA: ", pila)
               print("ENTRADA: ", entrada[n].getTipo())
               print("TRANSICION: q,",entrada[n].getTipo(),',', pila[it], ";", estado, ",λ", )
               print("--------------------")

               pila.pop(it)
              # print(pila)

               if n < (len(entrada)-1):
                    n+=1
               # print("el token siguiente es ",entrada[n].getTipo())

#muestra si la pila esta vacia
            elif len(entrada)-1 == n and pila[it]== "#":
                print("PILA: ", pila)
                print("ENTRADA: #")
                print("TRANSICION: q, λ", ',', pila[it], ";f" , ",λ", )
                print("--------------------")
                print("Secuencia de Tokens Correcta, FIN DEL ANALISIS SINTACTICO")
                break









