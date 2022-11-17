#Clase Fraccion con métodos
class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador
    
    def mostrarFraccion(self):
        fraccion = self.num, "/", self.den
        arr = [self.num,self.den]
        return print(arr[0],"/",arr[1])
    
    def multiplicar(self, otraFraccion):
        numnuevo = self.num * otraFraccion.num
        dennuevo = self.den * otraFraccion.den
        arr = [numnuevo,dennuevo]
        return arr

    def dividir(self, otraFraccion):
        numnuevo = self.num * otraFraccion.den
        dennuevo = self.den * otraFraccion.num
        return numnuevo, dennuevo
    
    def sumar(self, otraFraccion):
        numnuevo = (self.num * otraFraccion.den) + (self.den * otraFraccion.num)
        dennuevo = self.den * otraFraccion.den
        arr = [numnuevo,dennuevo]
        return arr
    
    def restar(self, otraFraccion):
        numnuevo = (self.num * otraFraccion.den) - (self.den * otraFraccion.num)
        dennuevo = self.den * otraFraccion.den
        arr = [numnuevo,dennuevo]
        return arr