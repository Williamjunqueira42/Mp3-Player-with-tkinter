# Teste de deselvonvimento de sistemas
# desenvolvindo por William, Lucas Leal, Pedro Damazio ...



from tkinter import *
from pygame import *  #  tem que instalar a blibioteca no seu pc

# Obs vamos usar todas as funçoes com nome em ingles
# nome de metodos em camelCase 

class mp3():
    def __init__(self, master): 
        self.master = master
        
        self.frameButtons = Frame(self.master, bg='black') #  frames de botões
        self.frameButtons.pack(side=BOTTOM, pady=50)

        # -----Buttons--------

        # imagens dos botões
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.img_btpause = PhotoImage(file='imagens/btpause.png')
        self.img_btstop = PhotoImage(file='imagens/btstop.png')
        self.img_btreturn = PhotoImage(file='imagens/btreturn.png')
        self.img_btavanced = PhotoImage(file='imagens/btavanced.png')


        # adicionado os botões
        self.btstart = Button(self.frameButtons, image=self.img_btstart, width=50)
        self.btpause = Button(self.frameButtons, image=self.img_btpause, width=50)
        self.btstop = Button(self.frameButtons, image=self.img_btstop, width=50)
        self.btreturn = Button(self.frameButtons, image=self.img_btreturn, width=50)
        self.btavanced = Button(self.frameButtons, image=self.img_btavanced, width=50)
        
        self.btstart.imagem = self.img_btstart
        self.btpause.imagem = self.img_btpause
        self.btstop.imagem = self.img_btstop
        self.btreturn.imagem = self.img_btreturn
        self.btavanced.imagem = self.img_btavanced


        # adicionado os botões no frameButtons
        self.btreturn.pack(side = LEFT, padx=10)
        self.btstart.pack(side = LEFT, padx=10)
        self.btpause.pack(side = LEFT, padx=10)
        self.btstop.pack(side = LEFT, padx=10) 
        self.btavanced.pack(side = LEFT, padx=10)

# Codigo Principal

root = Tk()
mp3(root)

root.iconbitmap('favicon.ico')
root.title('Mp3')
root.geometry('375x667')
root.configure(background='black')
root.mainloop()

