import tkinter
from tkinter import *
import tkinter.font as tkFont

mainscreen = Tk()

mainscreen.title('Teste de maioridade')
mainscreen.geometry('500x300')
mainscreen.iconbitmap('icon.ico')
mainscreen.config(background='#f2d096')

stylefont = tkFont.Font(family="Comic Sans MS", size=20, weight="bold", slant="italic")
stylefont2 = tkFont.Font(family="Comic Sans MS", size=10, weight="bold", slant="italic")
stylefont3 = tkFont.Font(family="Comic Sans MS", size=10, weight="bold", slant="italic")

#FUNÇÃO TESTE MAIORIDADE
def teste ():
    aa = idade.get()
    aa = int(aa)
    if(aa <= 0 or aa > 100):
        result['text'] = '{} anos? ERRO!'.format(aa)
        result['fg'] = 'red'

    else:
        if (aa >= 18):
            result['text'] = '{} anos: MAIOR DE IDADE'.format(aa)
            result['fg'] = '#304d63'

        else:
            result['text'] = '{} anos: MENOR DE IDADE'.format(aa)
            result['fg'] = '#304d63'

#-----------------------

#TITULO
lbl1 = Label(mainscreen, text='Teste de maioridade', font=stylefont, bg='#304d63', fg='#b2e7e8')
lbl1.place(x=10,y=10)
#-----------

#LABEL IDADE
lblidade = Label(mainscreen, text='Insira sua idade: ', font=stylefont2, bg='#ed8975')
lblidade.place(x=10,y=60, width=120)
#-----------

#CAMPO IDADE
idade = Entry(mainscreen)
idade.place(x=150, y=63, width=138)
#-----------

#BOTÃO ENVIAR
go = Button(mainscreen, text='OK', command=teste)
go.place(x=10, y=93, width=280)
#------------

#RESULTADO
result = Label(mainscreen, bg='#f2d096', font=stylefont3)
result.place(x=10, y=125)
#---------

mainscreen.mainloop()