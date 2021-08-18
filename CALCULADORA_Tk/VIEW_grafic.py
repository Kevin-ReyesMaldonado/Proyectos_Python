from Operadores import suma, subtraction, multiplication, division, potencia, porciento
from tkinter import *

class Master_Principal:
    def __init__(self, master) -> None:
        self.principal = Frame(master, width=300, height=200, bg='orange')
        self.frameTwo = Frame(master, width=300, height=70)
        self.frameTwo.pack()
        self.principal.pack(expand=True, fill='y')

    # buttons
        self.valor = StringVar()
        self.entrada = Entry(self.frameTwo, textvariable=self.valor, font=('', 20))
        self.entrada.config(justify=RIGHT)
        self.entrada.place(x=5, y=5,width=290, height=60)

        self.borrar = Button(self.principal, text='c', font=('', 20), width=2, fg='blue', activeforeground='red', command=self.suprimir)
        self.borrar.place(x=0, y=0)
        self.num7 = Button(self.principal, text='7', font=('', 20), width=2, command=lambda:self.mostrar('7'))
        self.num7.place(x=0, y=46)
        self.num4 = Button(self.principal, text='4', font=('',20), width=2, command=lambda:self.mostrar('4'))
        self.num4.place(x=0, y=92)
        self.num1 = Button(self.principal, text='1', font=('', 20), width=2, command=lambda:self.mostrar('1'))
        self.num1.place(x=0, y=138)

        self.num8 = Button(self.principal, text='8', font=('',20), width=2, command=lambda:self.mostrar('8'))
        self.num8.place(x=62, y=46)
        self.num5 = Button(self.principal, text='5', font=('',20), width=2, command=lambda:self.mostrar('5'))
        self.num5.place(x=62, y=92)
        self.num2 = Button(self.principal, text='2', font=('',20), width=2, command=lambda:self.mostrar('2'))
        self.num2.place(x=62, y=138)

        self.num9 = Button(self.principal, text='9', font=('',20), width=2, command=lambda:self.mostrar('9'))
        self.num9.place(x=124, y=46)
        self.num6 = Button(self.principal, text='6', font=('',20), width=2, command=lambda:self.mostrar('6'))
        self.num6.place(x=124, y=92)
        self.num3 = Button(self.principal, text='3', font=('',20), width=2, command=lambda:self.mostrar('3'))
        self.num3.place(x=124, y=138)

        self.suma = Button(self.principal, text='+', font=('',20), command=lambda:self.mostrar('+'))
        self.suma.place(x=186, y=46,width=55, height=92)
        self.resta = Button(self.principal, text='-', font=('',20), command=lambda:self.mostrar('-'))
        self.resta.place(x=186, y=138, width=55)
        
        self.num0 = Button(self.principal, text='0', font=('',20), width=2, command=lambda:self.mostrar('0'))
        self.num0.place(x=0, y=184)
        self.punto = Button(self.principal, text='.', font=('',20), width=2, command=lambda:self.mostrar('.'))
        self.punto.place(x=62, y=184)
        self.division = Button(self.principal, text='/', font=('',16), command=lambda:self.mostrar('/'))
        self.division.place(x=124, y=184,width=62, height=46)

        self.porciento = Button(self.principal, text='%', font=('',20), command=lambda:self.mostrar('%'))
        self.porciento.place(x=241, y=46, width=59, height=52)
        self.potencia = Button(self.principal, text='^', font=('',20), command=lambda:self.mostrar('^'))
        self.potencia.place(x=241, y=98, width=59, height=40)
        self.producto = Button(self.principal, text='x', font=('',20), command=lambda:self.mostrar('x'))
        self.producto.place(x=241, y=138, width=59)

        self.igual = Button(self.principal, text='=', font=('',20), fg='blue', activeforeground='red', 
        command=self.operar)
        self.igual.place(x=186, y=184, width=114, height=46)

        self.digitos = []

    def mostrar(self, val): # mostrar el el caracter del boton
        self.entrada.insert(END,val)
        self.digitos.append(val)
        print(self.digitos)

    def suprimir(self):# limpiar la entrada de digitos
        self.entrada.delete(0, END)
        self.digitos.clear()
    
    def operar(self): # el método a operar dependerá del operador para ejecutar su función
        valor1 = ''
        valor2 = ''
        if '+' in self.digitos: # si es un operador de suma
            for elem1 in range(self.digitos.index('+')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('+')+1:]:
                valor2 += elem2

            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = suma(valor1, valor2)
        
        elif '-' in self.digitos: # si es un operador de resta
            for elem1 in range(self.digitos.index('-')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('-')+1:]:
                valor2 += elem2

            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = subtraction(valor1, valor2)
        
        elif 'x' in self.digitos: # si es un operador de multiplicación
            for elem1 in range(self.digitos.index('x')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('x')+1:]:
                valor2 += elem2

            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = multiplication(valor1, valor2)
        
        elif '/' in self.digitos: # si es un operador de división
            for elem1 in range(self.digitos.index('/')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('/')+1:]:
                valor2 += elem2

            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = division(valor1, valor2)
        
        elif '^' in self.digitos: # si es un operador para sacar la potencia
            for elem1 in range(self.digitos.index('^')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('^')+1:]:
                valor2 += elem2
            
            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = potencia(valor1, valor2)
        
        elif '%' in self.digitos: # si la operación es para sacar el porcentaje de un número
            for elem1 in range(self.digitos.index('%')):
                valor1 += self.digitos[elem1]
            for elem2 in self.digitos[self.digitos.index('%')+1:]:
                valor2 += elem2

            if '.' in valor1:
                valor1 = float(valor1)
            else: valor1 = int(valor1)
            if '.' in valor2:
                valor2 = float(valor2)
            else: valor2 = int(valor2)

            funcion = porciento(valor1, valor2)

#---------métodos para los cambios en la entrada de caracteres----------
        self.entrada.delete(0, END) # elimina loq ue halla dentro de la entrada de texto
        self.entrada.insert(END, funcion) # inserta el caracter según el botón que se oprima
        self.digitos.clear() # borra el contenido de la lista de dígitos
        self.digitos.append(str(funcion)) # agrega al la lista el resultado de una operación


myRoot = Tk()
myRoot.geometry('300x300')
myRoot.title('Calculadora Gráfica')
myRoot.resizable(0,0)

objet = Master_Principal(myRoot)

myRoot.mainloop()