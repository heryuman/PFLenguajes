from graphviz import Digraph

subrutina="no"
cola= ""
lbl1="inicio"
NodoPadre= []
lb1master=[]
llaveA=0
swhitch = "no"
def unGrafo(entrada):
    global t
    cont=0
    f = Digraph(filename=str(cont)+'grafohdp.gv')
    f.attr('node', shape='box', color='blue', fontcolor='red')
    t=f
    global p
    bp = Digraph('BloquePrincipal')
    bp.graph_attr.update(rank='min')
    p=bp
    cont+=1

    global subrutina
    global cola
    global NodoPadre
    global llaveA
    global lbl1
    global lb1master
    global swhitch


    for i in range(0, len(entrada)):
        #dibuja asignaciones fuera de llaves
       # print('token acutal ',entrada[i].getTipo())
        if (entrada[i].getTipo() == "tk_let" or entrada[i].getTipo() == "tk_var" or entrada[i].getTipo() == "tk_const") and (entrada[i+3].getTipo() != "tk_parA" and llaveA==0):


            lbl2='Asignacion_'+str(entrada[i+1].getvalor())
            cabeza=str(i+1)
           # print('arista de ', cola, ' a ', cabeza)
            principal(cola,cabeza, lbl1, lbl2)

            cola=cabeza
            lbl1=lbl2

#dibuja definicion de funciones  fuera de llaves
        elif (entrada[i].getTipo() == "tk_let" or entrada[i].getTipo() == "tk_var" or entrada[i].getTipo() == "tk_const") and (entrada[i + 3].getTipo() == "tk_parA" and llaveA == 0):
           # print("dibujando deffunciones")
            parametro=[]
            cabeza = str(i + 1)
            lbl2 = 'DEfFunc_' + str(entrada[i + 1].getvalor())
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)

            principal(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2
            llaveA+=1
            for s in range(i+2,len(entrada)):
                if entrada[s].getTipo() == "tk_Id":
                    #print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i=s
                    break

           # print('los parametros',parametro)
            lbl2 = 'Params_' + str(parametro)
            cabeza = str(i + 1)
           # print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2

#Dibujando definicion de funciones dentro de llaves
        elif (entrada[i].getTipo() == "tk_let" or entrada[i].getTipo() == "tk_var" or entrada[i].getTipo() == "tk_const") and (entrada[i + 3].getTipo() == "tk_parA" and llaveA > 0):
           # print("dibujando deffunciones entre llaves")
            parametro=[]
            cabeza = str(i + 1)
            lbl2 = 'DEfFunc_' + str(entrada[i + 1].getvalor())
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)

            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2
            llaveA+=1
            for s in range(i+2,len(entrada)):
                if entrada[s].getTipo() == "tk_Id":
                   # print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i=s
                    break

           # print('los parametros',parametro)
            lbl2 = 'Params_' + str(parametro)
            cabeza = str(i + 1)
           # print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2

#dibujando for fuera de llaves

        elif entrada[i].getTipo() == 'tk_foreach'and llaveA==0:
          #  print('en el for')
            parametro=[]
            cabeza= str(i)
            lbl2 = 'sentencia_Foreach'
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)
            principal(cola,cabeza,lbl1,lbl2)
            cola = cabeza
            lbl1 = lbl2
            llaveA += 1

            for s in range(i + 2, len(entrada)):
                if entrada[s].getTipo() == "tk_Id" or entrada[s].getTipo() == "tk_in":
                   # print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i = s
                    break

            lbl2 = 'rango_' + str(parametro)
            cabeza = str(i + 1)
         #   print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2


#dibujando sentencias foreach entre llaves
        elif entrada[i].getTipo() == 'tk_foreach' and llaveA > 0:
            #print('en el for')
            parametro = []
            cabeza = str(i)
            lbl2 = 'sentencia_Foreach'
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)
            principal(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2
            llaveA += 1

            for s in range(i + 2, len(entrada)):
                if entrada[s].getTipo() == "tk_Id" or entrada[s].getTipo() == "tk_in":
                   # print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i = s
                    break

            lbl2 = 'rango_' + str(parametro)
            cabeza = str(i + 1)
         #   print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2
#dibujando llamada de funciones fuera de llaves

        elif entrada[i].getTipo() == 'tk_Id' and entrada[i+1].getTipo()== 'tk_parA' and llaveA == 0:
          #  print('dibujando Llamada de Funcioes')
            parametro = []
            cabeza = str(i)
            lbl2 = 'Llamada_'+str(entrada[i].getvalor())
           # NodoPadre.append(cabeza)
            #lb1master.append(lbl2)
            principal(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2
          #  llaveA += 1

            for s in range(i +1, len(entrada)):
                if entrada[s].getTipo() == "tk_Id" or entrada[s].getTipo() == "tk_true" or entrada[s].getTipo() == "tk_false"or entrada[s].getTipo() == "tk_Numero":
                  #  print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i = s
                    break

            lbl2 = 'Parametros_' + str(parametro)
            cabeza = str(i + 1)
          #  print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2

# dibujando llamada de funciones entre llaves

        elif entrada[i].getTipo() == 'tk_Id' and entrada[i + 1].getTipo() == 'tk_parA' and llaveA > 0:
            #print('dibujando Llamada de Funcioes')
            parametro = []
            cabeza = str(i)
            lbl2 = 'Llamada_' + str(entrada[i].getvalor())
            # NodoPadre.append(cabeza)
            # lb1master.append(lbl2)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2


            for s in range(i + 1, len(entrada)):
                if entrada[s].getTipo() == "tk_Id" or entrada[s].getTipo() == "tk_true" or entrada[
                    s].getTipo() == "tk_false" or entrada[s].getTipo() == "tk_Numero":
                #    print('*/*/*/*/*/hay id en params')
                    parametro.append(entrada[s].getvalor())
                elif entrada[s].getTipo() == "tk_parC":
                    i = s
                    break

            lbl2 = 'Parametros_' + str(parametro)
            cabeza = str(i + 1)
           # print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2





        #dibuja sentencias fuera dellaves
        elif (entrada[i].getTipo() == "tk_if"or entrada[i].getTipo() == "tk_while")and llaveA == 0:


            lbl2 = 'sentencia_' + str(entrada[i].getvalor())
            cabeza= str(i)
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)
           # print('arista de ', cola, ' a ', cabeza)
            principal(cola,cabeza,lbl1,lbl2)
            cola=cabeza
            lbl1=lbl2


            cabeza=str(i+2)
            lbl2= 'condicion_'+entrada[i+2].getvalor()
         #   print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola,cabeza,lbl1,lbl2 )
            cola=cabeza
            lbl1=lbl2

            llaveA+=1
          #  print(llaveA)

#dibuja seentencias if o while entrellaves
        elif (entrada[i].getTipo() == "tk_if"or entrada[i].getTipo() == "tk_while") and llaveA>0:
           #  print("if o while cuando llave >0")
             cabeza=str(i)
             NodoPadre.append(cabeza)
             lbl2='sentencia_'+str(entrada[i].getvalor())
             lb1master.append(lbl2)
            # print('arista de ',cola,' a ',cabeza)
             Subrutina(cola,cabeza,lbl1,lbl2)
             cola=cabeza
             lbl1 = lbl2

             cabeza = str(i+2)
             lbl2 = 'condicion_' + entrada[i+2].getvalor()
            # print('arista de ', cola, ' a ', cabeza)
             Subrutina(cola, cabeza, lbl1, lbl2)
             cola = cabeza
             lbl1 = lbl2

             llaveA+=1

#dibuja asignaciones  en llaves
        elif (entrada[i].getTipo() == "tk_let" or entrada[i].getTipo() == "tk_var" or entrada[i].getTipo() == "tk_const") and (entrada[i+3].getTipo() != "tk_mayorQ" and llaveA>0):

            lbl2='Asignacion_'+str(entrada[i+1].getvalor())
            cabeza=str(i+1)
         #   print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola,cabeza, lbl1, lbl2)

            cola=cabeza
            lbl1=lbl2

# dibujando switch fuera de llavees

        elif entrada[i].getTipo() == 'tk_switch' and llaveA == 0:
            swhitch ="si"
            lbl2 = 'sentencia_' + str(entrada[i].getvalor())
            cabeza = str(i)
            NodoPadre.append(cabeza)
            lb1master.append(lbl2)
         #   print('arista de ', cola, ' a ', cabeza)
            principal(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2

            cabeza = str(i + 2)
            lbl2 = 'condicion_' + entrada[i + 2].getvalor()
           # print('arista de ', cola, ' a ', cabeza)
            Subrutina(cola, cabeza, lbl1, lbl2)
            cola = cabeza
            lbl1 = lbl2

            llaveA += 1

        elif entrada[i].getTipo() == 'tk_case' :
            lbl2 ='case_'+ str(entrada[i+1].getvalor())
            cabeza = str(i)
            Subrutina(cola,cabeza,lbl1,lbl2)
            cola=cabeza
            lbl1=lbl2


        elif i == len(entrada)-1:
          #  print('fin entrada')
            f.subgraph(bp)

            f.view()
            NodoPadre.clear()
            lbl1="inicio"
            lb1master.clear()
            llaveA=0
            subrutina = "no"
            cola = ""

        elif entrada[i].getTipo()== "tk_LlaveC":
            if llaveA>0 :
             #   print(NodoPadre)
                cola = NodoPadre[llaveA - 1]
                lbl1 = lb1master[llaveA - 1]
                NodoPadre.pop(llaveA - 1)
                lb1master.pop(llaveA - 1)
             #   print('hay ', llaveA, ' llaves, la cola es: ', cola)
             #   print('la lbl1 es ', lbl1)
                llaveA -= 1


           # print('quedan ', llaveA)





def principal(inicio,final,lbl1,lbl2):

    p.node(inicio,label=lbl1)
    p.node(final,lbl2)
    p.edge(inicio,final)

def Subrutina(inicio,final,lbl1,lbl2):

    sb = Digraph('BloqueSec'+lbl2)
    sb.node(inicio,label=lbl1)
    sb.node(final,label=lbl2)
    sb.edge(inicio,final)
    t.subgraph(sb)












