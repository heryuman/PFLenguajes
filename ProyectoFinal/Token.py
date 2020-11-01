class TipoToken:

    def __init__(self, tipo, valor,descripcion,fila,columna):

        self.tip= tipo
        self.val = valor
        self.descrip = descripcion
        self.fil=fila
        self.col=columna


    def getTipo(self):
        return self.tip

    def getvalor(self):

        return self.val

    def getDescripcion(self):
        return self.descrip

    def getFila(self):
        return self.fil

    def getColumna(self):
        return self.col


