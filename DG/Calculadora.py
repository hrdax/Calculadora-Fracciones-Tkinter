from cProfile import label
from distutils.cmd import Command
from tkinter import *
from ClassFraccion import *

#modificacion para pruebas en unittest

def suma(n1, n2):
        ns = n1 + n2
        print(f'la suma es de {str(ns)}')
        return ns

def resta(n1, n2):
        ns = n1 - n2
        print(f'la resta es de {str(ns)}')
        return ns

def multiplicacion(n1, n2):
    ns = n1 * n2
    print(f'la multiplicacion es de {str(ns)}')
    return ns
    
def division(n1, n2):
    ns = n1 / n2
    print(f'la division es de {str(ns)}')
    return ns


#Funciones para fracciones
def sumaFraccion(n1,n2,n3,n4):
    fraccion1 = Fraccion(n1, n2)
    fraccion2 = Fraccion(n3, n4)
    fraccionnueva = fraccion1.sumar(fraccion2)
    print(f'la suma es de {str(fraccionnueva)}')
    return fraccionnueva
    
def restaFraccion(n1,n2,n3,n4):
    fraccion1 = Fraccion(n1, n2)
    fraccion2 = Fraccion(n3, n4)
    fraccionnueva = fraccion1.multiplicar(fraccion2)
    print(f'la resta es de {str(fraccionnueva)}')
    return fraccionnueva

def multiplicacionFraccion(n1,n2,n3,n4):
        fraccion1 = Fraccion(n1, n2)
        fraccion2 = Fraccion(n3, n4)
        fraccionnueva = fraccion1.multiplicar(fraccion2)
        print(f'la multiplicacion es de {str(fraccionnueva)}')
        return fraccionnueva

def divisionFraccion(n1,n2,n3,n4):
        fraccion1 = Fraccion(n1, n2)
        fraccion2 = Fraccion(n3, n4)
        fraccionnueva = fraccion1.dividir(fraccion2)
        print(f'la division es de {str(fraccionnueva)}')
        return fraccionnueva

#fin modificacion para pruebas en unittest

# #Función para mostrar ventana main
# def vista_tkinter():
#     ventana = Tk()
#     ventana.title("eh?")
#     ventana.resizable(1,1)
#     ventana.geometry("1320x720")
#     ventana.config(bg="black")

#     #Funciones numeros no fraccionados
#     def suma():
#             ns = float(Entry_num1.get()) + float(Entry_num2.get())
#             Entry_resultado.delete(0, END)
#             Entry_resultado.insert(0, ns)

#     def resta():
#             ns = float(Entry_num1.get()) - float(Entry_num2.get())
#             Entry_resultado.delete(0, END)
#             Entry_resultado.insert(0, ns)

#     def multiplicacion():
#         ns = float(Entry_num1.get()) * float(Entry_num2.get())
#         Entry_resultado.delete(0, END)
#         Entry_resultado.insert(0, ns)
    
#     def division():
#         ns = float(Entry_num1.get()) / float(Entry_num2.get())
#         Entry_resultado.delete(0, END)
#         Entry_resultado.insert(0, ns)
    
#     #Funciones para fracciones
#     def sumaFraccion():
#         fraccion1 = Fraccion(float(Entry_numF1.get()), float(Entry_denF1.get()))
#         fraccion2 = Fraccion(float(Entry_numF2.get()), float(Entry_denF2.get()))
#         fraccionnueva = fraccion1.sumar(fraccion2)
#         Entry_resultadoF1.delete(0, END)
#         Entry_resultadoF2.delete(0, END)
#         Entry_resultadoF1.insert(0,fraccionnueva[0])
#         Entry_resultadoF2.insert(0,fraccionnueva[1])
    
#     def restaFraccion():
#         fraccion1 = Fraccion(float(Entry_numF1.get()), float(Entry_denF1.get()))
#         fraccion2 = Fraccion(float(Entry_numF2.get()), float(Entry_denF2.get()))
#         fraccionnueva = fraccion1.restar(fraccion2)
#         Entry_resultadoF1.delete(0, END)
#         Entry_resultadoF2.delete(0, END)
#         Entry_resultadoF1.insert(0,fraccionnueva[0])
#         Entry_resultadoF2.insert(0,fraccionnueva[1])

#     def multiplicacionFraccion(n1,n2):
#         fraccion1 = Fraccion(float(Entry_numF1.get()), float(Entry_denF1.get()))
#         fraccion2 = Fraccion(float(Entry_numF2.get()), float(Entry_denF2.get()))
#         fraccionnueva = fraccion1.multiplicar(fraccion2)
#         Entry_resultadoF1.delete(0, END)
#         Entry_resultadoF2.delete(0, END)
#         Entry_resultadoF1.insert(0,fraccionnueva[0])
#         Entry_resultadoF2.insert(0,fraccionnueva[1])
    
#     def divisionFraccion(n1,n2):
#         fraccion1 = Fraccion(float(Entry_numF1.get()), float(Entry_denF1.get()))
#         fraccion2 = Fraccion(float(Entry_numF2.get()), float(Entry_denF2.get()))
#         fraccionnueva = fraccion1.dividir(fraccion2)
#         Entry_resultadoF1.delete(0, END)
#         Entry_resultadoF2.delete(0, END)
#         Entry_resultadoF1.insert(0,fraccionnueva[0])
#         Entry_resultadoF2.insert(0,fraccionnueva[1])

#     #Numeros no fraccionados
#     labelN1 = Label(ventana, fg="Grey",bg="White",text="Numero 1: ")
#     labelN1.place(x=50, y=20)
    
#     labelN2 = Label(ventana, text="Numero 2: ")
#     labelN2.place(x=50, y=60)

#     labelResultado = Label(ventana, text="Resultado: ")
#     labelResultado.place(x=50, y=100)

#     #Entrys
#     Entry_num1 = Entry(ventana, width=10)
#     Entry_num1.place(x=150, y=20)
    
#     Entry_num2 = Entry(ventana, width=10)
#     Entry_num2.place(x=150, y=60)

#     Entry_resultado = Entry(ventana, width=10)
#     Entry_resultado.place(x=150, y=100)

#     #Botones
#     btn_sumar = Button(ventana, text="Sumar", command=suma)
#     btn_sumar.place(x=50, y=140)

#     btn_restar = Button(ventana, text="Restar", command=resta)
#     btn_restar.place(x=150, y=140)

#     btn_multiplicar = Button(ventana, text="Multiplicar", command=multiplicacion)
#     btn_multiplicar.place(x=250, y=140)

#     btn_dividir = Button(ventana, text="Dividir", command=division)
#     btn_dividir.place(x=350, y=140)

#     #Numeros fraccionados
#     labelNumerador = Label(ventana, text="Numerador: ")
#     labelNumerador.place(x=50, y=200)

#     labelDenominador = Label(ventana, text="Denominador: ")
#     labelDenominador.place(x=50, y=250)

#     labelResultadoF = Label(ventana, text="=")
#     labelResultadoF.place(x=248, y=225)

#     #Entrys
#     Entry_numF1 = Entry(ventana, width=5)
#     Entry_numF1.place(x=150, y=200)

#     Entry_denF1 = Entry(ventana, width=5)
#     Entry_denF1.place(x=150, y=250)

#     Entry_numF2 = Entry(ventana, width=5)
#     Entry_numF2.place(x=200, y=200)

#     Entry_denF2 = Entry(ventana, width=5)
#     Entry_denF2.place(x=200, y=250)

#     Entry_resultadoF1 = Entry(ventana, width=5)
#     Entry_resultadoF1.place(x=275, y=200)

#     Entry_resultadoF2 = Entry(ventana, width=5)
#     Entry_resultadoF2.place(x=275, y=250)

#     #Botones
#     btn_sumar_Fraccion = Button(ventana, text="Sumar Fracciones", command=sumaFraccion)
#     btn_sumar_Fraccion.place(x=50, y=300)

#     btn_restar_Fraccion = Button(ventana, text="Restar Fracciones", command=restaFraccion)
#     btn_restar_Fraccion.place(x=170, y=300)

#     btn_multiplicar_Fraccion = Button(ventana, text="Multiplicar Fracciones", command=multiplicacionFraccion)
#     btn_multiplicar_Fraccion.place(x=290, y=300)

#     btn_dividir_Fraccion = Button(ventana, text="Dividir Fracciones", command=divisionFraccion)
#     btn_dividir_Fraccion.place(x=435, y=300)
    
#     ventana.mainloop()