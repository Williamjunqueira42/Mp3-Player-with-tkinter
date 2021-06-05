# Teste de deselvonvimento de sistemas
# desenvolvindo por William, Lucas Leal, Pedro Damazio ...



from tkinter import *
from pygame import *  #  tem que instalar a blibioteca no seu pc

# Obs vamos usar todas as funçoes com nome em ingles 

class mp3():
    def __init__(self, master):
        self.master = master

# Codigo Principal

root =Tk()
mp3(root)

root.iconbitmap('favicon.ico')
root.title('Mp3')
root.geometry("300x400")
root.configure(background="black")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack()

#Botões de start e pause

imgbotao1=PhotoImage(file="icons8-start-50.png")
btnsalvar1=Button(root,image=imgbotao1,height=50,width=50).place(x=50,y=75)

imgbotao2=PhotoImage(file="icons8-pause-50.png")
btnsalvar2=Button(root,image=imgbotao2,height=50,width=50).place(x=200,y=75)

#Nome da música e do artista

txt1 = Label(root, text="", bg="white", fg="black")
txt1.place(x=10, y=10, width=280, height=20)

txt2 = Label(root, text="", bg="white", fg="black")
txt2.place(x=10, y=40, width=280, height=20)

#Músicas disponiveis 

txt3 = Label(root, text="", bg="white", fg="black")
txt3.place(x=10, y=240, width=280, height=20)

txt4 = Label(root, text="", bg="white", fg="black")
txt4.place(x=10, y=270, width=280, height=20)

txt5 = Label(root, text="", bg="white", fg="black")
txt5.place(x=10, y=300, width=280, height=20)

txt6 = Label(root, text="", bg="white", fg="black")
txt6.place(x=10, y=330, width=280, height=20)

txt7 = Label(root, text="", bg="white", fg="black")
txt7.place(x=10, y=360, width=280, height=20)


root.mainloop()

