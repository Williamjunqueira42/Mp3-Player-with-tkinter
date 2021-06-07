# Teste de deselvonvimento de sistemas
# desenvolvindo por William, Lucas Leal, Pedro Damazio ...



from tkinter import * 
from pygame import *  #  tem que instalar a blibioteca no seu pc
from eyed3 import *  # para pegar os metadados das musicas, tabem tem que installar
import tkinter.ttk as ttk
from time import *
from mutagen.mp3 import MP3
from tkinter import filedialog
 


class mp3():
    def __init__(self, master): 
        self.master = master
        
        self.frameLabels = Frame(self.master, bg='black')  #  frame dos labels 
        self.frameButtons = Frame(self.master, bg='black') #  frames de botões
        self.frameSlide = Frame(self.master, bg='black')
        self.framelistBox = Frame(self.master, bg='white')
        
        self.frameButtons.pack(side=BOTTOM, pady=30)
        self.frameSlide.pack(side=BOTTOM, anchor=S)
        self.frameLabels.pack(side=BOTTOM, pady=30)
        self.framelistBox.pack(side = BOTTOM)
        

        # Menu 
        
        self.menu = Menu(self.frameLabels,)
        self.master.config(menu=self.menu)
        self.song_menu = Menu(self.menu)
        self.menu.add_cascade(label="Add songs", menu=self.song_menu)
        self.song_menu.add_command(label="Add one song", command=self.addsong)

        self.song = ('musicas/⠀.mp3')
        
        # -----Labels---------

        self.musicanome = load(self.song).tag.title
        self.artistanome = load(self.song).tag.album_artist


        #adicionado labels

        self.lista = Listbox(self.framelistBox, bg='white', fg='black', width=60, height=20, selectbackground='black')
        


   
        self.lbnomemusica = Label(self.frameLabels, text=f'{self.musicanome}', fg='white', bg='black', font='Coolvetica 20 bold')

        self.lbnomeartista = Label(self.frameLabels, text=f'{self.artistanome}', fg='white', bg='black', font='Coolvetica 12 bold')

        # adicionado labels na janela


        self.lista.pack()
        self.lbnomemusica.pack(anchor=W)
        self.lbnomeartista.pack()
        


        self.status_bar = Label(self.frameSlide, text='00:00:00', anchor=E, bg='black', fg='white')
        self.status_bar.pack(fill=X, padx=20)




        # -----Buttons--------

        # imagens dos botões
        
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.img_btpause = PhotoImage(file='imagens/btpause.png')
        self.img_btstop = PhotoImage(file='imagens/btstop.png')
        self.img_btreturn = PhotoImage(file='imagens/btreturn.png')
        self.img_btavanced = PhotoImage(file='imagens/btavanced.png')


        # adicionado os botões
        self.btstart = Button(self.frameButtons, image=self.img_btstart, width=50, height=50, bg='black', activebackground='black', relief='flat', command=self.playPausesong)

        self.btstop = Button(self.frameButtons, image=self.img_btstop, width=20, height=30, bg='black', activebackground='black', relief='flat', command=self.stopsong)

        self.btreturn = Button(self.frameButtons, image=self.img_btreturn, width=20, height=20, bg='black', activebackground='black', relief='flat')

        self.btavanced = Button(self.frameButtons, image=self.img_btavanced, width=20, height=20, bg='black', activebackground='black', relief='flat')

    
        self.btstart.imagem = self.img_btstart
        self.btstop.imagem = self.img_btstop
        self.btreturn.imagem = self.img_btreturn
        self.btavanced.imagem = self.img_btavanced


        # adicionado os botões no frameButtons
    
        self.btreturn.pack(side = LEFT, padx=8)
        self.btstart.pack(side = LEFT, padx=8)
        self.btstop.pack(side = LEFT, padx=8) 
        self.btavanced.pack(side = LEFT, padx=8)
    
        self.v = 1
        self.mixer = mixer
        
    def playPausesong(self):  #  metodo para tocar a musica
        
        if self.v == 1:
            #  mudando o botão play para o botão pause
            self.img_btstart = PhotoImage(file='imagens/btpause.png')
            self.btstart['image'] = self.img_btpause

            self.mixer.init()
            self.mixer.music.load(f'{self.song}')
            self.mixer.music.play()
            self.v = 2

        elif self.v == 2:
            self.pausesong()
        
        elif self.v == 3:
            self.img_btstart = PhotoImage(file='imagens/btpause.png')
            self.btstart['image'] = self.img_btpause
            self.mixer.music.unpause()
            self.v = 2
        self.playTime()
        self.musicanome['text'] = load(self.song).tag.title


    def stopsong(self):  #  metodo para parar de tocar a musica
    
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.btstart['image'] = self.img_btstart
        self.mixer.music.stop()
        self.v = 1     
    

    def pausesong(self):  #  metodo para pausar a musica

        #  mudando o botão pause para o botão play
        self.img_btstart = PhotoImage(file='imagens/btstart.png')
        self.btstart['image'] = self.img_btstart
        self.mixer.music.pause()  
        self.v = 3
    

    def playTime(self):  #  metodo para mostrar o tempo da musica
        time = mixer.music.get_pos() / 1000
        self.converted_time = strftime('%H:%M:%S', gmtime(time)) 
        # So Deus Sabe o que eu fiz ai

        self.status_bar.config(text=self.converted_time)
        self.status_bar.after(1000, self.playTime)


    def addsong(self):

        self.song = filedialog.askopenfilename(initialdir='musicas/', title='escolha algum som', )

        self.lista.insert(END, load(self.song).tag.title)
        

# Codigo Principal

root = Tk()
mp3(root)

root.iconbitmap('favicon100.ico')
root.title('''                                    
Music Player
''')
root.geometry('375x667')
root.resizable(False, False)
root.configure(background='black')
root.mainloop()

