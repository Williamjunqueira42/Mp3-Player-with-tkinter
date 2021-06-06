# Teste de deselvonvimento de sistemas
# desenvolvindo por William, Lucas Leal, Pedro Damazio ...



from tkinter import *
from pygame import *  #  tem que instalar a blibioteca no seu pc

# Obs vamos usar todas as funçoes com nome em ingles
# nome de metodos em camelCase 

class mp3():
    def __init__(self, master): 
        self.master = master
        
        self.frameLabels = Frame(self.master, bg='black')  #  frame dos labels 
        self.frameButtons = Frame(self.master, bg='black') #  frames de botões
         
        self.frameButtons.pack(side=BOTTOM, pady=50)
        self.frameLabels.pack(side=BOTTOM, pady=30)
        
        # -----Labels---------

        # imagens labels
        self.img_lbunknow = PhotoImage(file='imagens/unknow.png')

        #adicionado labels
        self.lbunknow = Label(self.frameLabels, image=self.img_lbunknow)
        self.lbunknow.imagem = self.img_lbunknow

        self.lbnomeartista = Label(self.frameLabels, text='Nome artista', fg='white', bg='black')

        # adicionado labels na janela
        self.lbunknow.pack(pady= 10)
        self.lbnomeartista.pack()
        
        # -----Buttons--------

        # imagens dos botões
        
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.img_btpause = PhotoImage(file='imagens/btpause.png')
        self.img_btstop = PhotoImage(file='imagens/btstop.png')
        self.img_btreturn = PhotoImage(file='imagens/btreturn.png')
        self.img_btavanced = PhotoImage(file='imagens/btavanced.png')


        # adicionado os botões
        self.btstart = Button(self.frameButtons, image=self.img_btstart, width=50, bg='black', activebackground='black', relief='flat', command=self.playPausesong)

        self.btpause = Button(self.frameButtons, image=self.img_btpause, width=50, bg='black', activebackground='black', relief='flat', command=self.pausesong)

        self.btstop = Button(self.frameButtons, image=self.img_btstop, width=50, bg='black', activebackground='black', relief='flat', command=self.stopsong)

        self.btreturn = Button(self.frameButtons, image=self.img_btreturn, width=50, bg='black', activebackground='black', relief='flat')

        self.btavanced = Button(self.frameButtons, image=self.img_btavanced, width=50, bg='black', activebackground='black', relief='flat')

    
        self.btstart.imagem = self.img_btstart
        self.btpause.imagem = self.img_btpause
        self.btstop.imagem = self.img_btstop
        self.btreturn.imagem = self.img_btreturn
        self.btavanced.imagem = self.img_btavanced


        # adicionado os botões no frameButtons
    
        self.btreturn.pack(side = LEFT, padx=10)
        self.btstart.pack(side = LEFT, padx=10)
        # self.btpause.pack(side = LEFT, padx=10)
        self.btstop.pack(side = LEFT, padx=10) 
        self.btavanced.pack(side = LEFT, padx=10)
    
        self.v = 1

        
    def playPausesong(self):  #  metodo para tocar a musica
       
        print(self.v)
        if self.v == 1:

            #  mudando o botão play para o botão pause
            self.img_btstart = PhotoImage(file='imagens/btpause.png')
            self.btstart['image'] = self.img_btpause

            mixer.init()
            mixer.music.load('musicas\Jovem Dex  Porsche.mp3')
            mixer.music.play()
            # event.wait()

            self.v = 2

        elif self.v == 2:
            self.pausesong()
        
        elif self.v == 3:
            self.img_btstart = PhotoImage(file='imagens/btpause.png')
            self.btstart['image'] = self.img_btpause
            mixer.music.unpause()
            self.v = 2
            
     


    def stopsong(self):  #  metodo para parar de tocar a musica
      

        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.btstart['image'] = self.img_btstart
        mixer.music.stop()
        self.v = 2
        
    

    def pausesong(self):  #  metodo para pausar a musica

        #  mudando o botão pause para o botão play
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.btstart['image'] = self.img_btstart
        mixer.music.pause()
        self.v = 3

# Codigo Principal

root = Tk()
mp3(root)

root.iconbitmap('favicon.ico')
root.title('Mp3')
root.geometry('375x667')
root.resizable(False, False)
root.configure(background='black')
root.mainloop()

