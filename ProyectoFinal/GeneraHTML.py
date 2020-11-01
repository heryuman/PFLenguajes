
#generando html
import webbrowser
def html_create(lista):



        template = open("HTML/template.html", "r")
        output = open("Reportes/Tokens/reportokens.html", "w")


        i = 0
        while i < len(lista):

            text = template.read().format(get_num="0", get_tipoc="", get_lexema="", get_desc="", get_fila="",get_columna="")
            output.write(text)

            output.writelines("<tr>")
            output.writelines("<th scope = 'row'>%s</th >" % (i + 1))

            output.writelines("<td> %s </td>" % lista[i].getTipo()) #tipo de Token
            output.writelines("<td> %s </td>" % lista[i].getvalor())   #valor (lexema)
            output.writelines("<td> %s </td>" % lista[i].getDescripcion()) #Descripcion
            output.writelines("<td> %s </td>" % lista[i].getFila())#Fila
            output.writelines("<td> %s </td>" % lista[i].getColumna())  #Columna
            output.writelines("</tr>")

            i += 1
        output.writelines(" </tbody>")
        output.writelines(" </table>")
        output.writelines(" </html>")
        template.close()
        output.close()
        webbrowser.open_new_tab('Reportes/Tokens/reportokens.html')


def Errores_html_create(lista):
    template = open("HTML/template2.html", "r")
    output = open("Reportes/Errores/reporterrores.html", "w")

    i = 0
    while i < len(lista):
        text = template.read().format(get_num="0", get_Errores="")
        output.write(text)

        output.writelines("<tr>")
        output.writelines("<th scope = 'row'>%s</th >" % (i + 1))

        output.writelines("<td> %s </td>" % lista[i])  # tipo de Token

        output.writelines("</tr>")

        i += 1
    output.writelines(" </tbody>")
    output.writelines(" </table>")
    output.writelines(" </html>")
    template.close()
    output.close()
    webbrowser.open('Reportes/Errores/reporterrores.html')