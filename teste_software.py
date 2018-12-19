from tkinter import *

global azul
azul= False
global verde
verde= False

def comando(op):
    global azul
    global verde    
    if(op == 1 and azul == False):
        print("led azul ligado")
        azul = True

    elif (op == 1 and azul == True):
        print("Led Azul Desligado")
        azul = False

    elif (op == 2 and verde == False):
        print("led verde ligado")
        verde = True

    elif(op == 2 and verde == True):
        print("Led Verde Desligado")
        verde = False


janela = Tk()

janela.title('leitor de email')
janela.geometry('750x750')

texto1 = Label (text='Ligado led azul')
texto1.place(x=50,y=70)
botão1 = Button(text='on/of ', command = lambda: comando(1), bg = 'blue').place(x=50, y= 90)

texto2 = Label (text='Ligado led verde')
texto2.place(x=200,y=70)
botão2 = Button(text='on/of ', command = lambda: comando(2), bg = 'green').place(x=215, y= 90)

janela.mainloop() 
