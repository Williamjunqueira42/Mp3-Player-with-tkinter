# Teste de deselvonvimento de sistemas
# desenvolvindo por William, Lucas Leal, Pedro Damazio ...


from tkinter import * 
from pygame import *  #  tem que instalar a blibioteca no seu pc
from eyed3 import *  # para pegar os metadados das musicas, tabem tem que installar
from time import *
from mutagen.mp3 import MP3
from tkinter import filedialog
import mysql.connector
 


class Bd():
    def __init__(self):
        
        cnx = mysql.connector.connect(user='root', password='********', host='127.0.0.1')

        mycursor = cnx.cursor()
        mycursor.execute("CREATE DATABASE mydatabase")
        


class mp3():
    def __init__(self, master): 
        self.master = master
        self.master.configure(background='black')
        #  criando os frames
        self.frameLabels = Frame(self.master, bg='black')  #  frame dos labels 
        self.frameButtons = Frame(self.master, bg='black') #  frames de botões
        self.frameTime = Frame(self.master, bg='black')
        self.framelistBox = Frame(self.master, bg='black')
        
        # posicionando os frames
        
        self.frameButtons.pack(side=BOTTOM, pady=30)
        self.frameTime.pack(side=BOTTOM, anchor=S)
        self.frameLabels.pack(side=BOTTOM, pady=30)
        self.framelistBox.pack(side = BOTTOM)
        

#--------------------------------------------------------------------------------
# ----------------------------------MENU------------------------------------------
#---------------------------------------------------------------------------------
        
        self.menu = Menu(self.frameLabels,) #  Criação do menu
        self.master.config(menu=self.menu)

        self.song_menu = Menu(self.menu)
        self.menu.add_cascade(label="Add songs", menu=self.song_menu)
        self.song_menu.add_command(label="Add one song to playlist", command=self.addsong)
        
        self.menu.add_cascade(label="Remove songs", menu=self.song_menu)
      
        
        
#------------------------------------------------------------------------------------------------------------------------
#----------------------------------BUTTONS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Imagens dos botões
        
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


        # posicionando os botões
    
        self.btreturn.pack(side = LEFT, padx=8)
        self.btstart.pack(side = LEFT, padx=8)
        self.btstop.pack(side = LEFT, padx=8) 
        self.btavanced.pack(side = LEFT, padx=8)

        self.song_box = Listbox(self.framelistBox, bg='black', fg='green', width=60, height=20, selectbackground='gray')
        self.song_box.pack()


#---------------------------------------------------------------------------------
#----------------------------------LABELS-----------------------------------------#---------------------------------------------------------------------------------
        
         #  variaveis referentes ao nome da musica e nome do cantor
        self.musicanome = StringVar() 
        self.artistanome = StringVar()
        self.musicanome.set('')
        self.artistanome.set('')

     
        #adicionado os labels

        self.lbnomemusica = Label(self.frameLabels, textvariable=self.musicanome, fg='white', bg='black', font='Coolvetica 15 bold')
        self.lbnomeartista = Label(self.frameLabels, textvariable=self.artistanome, fg='white', bg='black', font='Coolvetica 12 bold')

        # posicionando os labels
        
        self.lbnomemusica.pack(anchor=W)
        self.lbnomeartista.pack()
        
#----------------------------------------------------------------------------

        self.time_bar = Label(self.frameTime, text='00:00:00', anchor=E, bg='black', fg='grey')
        self.time_bar.pack(fill=X, padx=20)


#---------------------------------------------------------------------------------
        self.v = 1
        self.mixer = mixer
        
    def playPausesong(self):  #  metodo para tocar a musica
        
        self.y = ''   
        for x in self.song:
            if x == load(self.song).tag.title[0]: break
            self.y += x
            
        self.z = ''  
        for x in self.song[::-1]: 
            if x == load(self.song).tag.title[len(load(self.song).tag.title)-1]: break
            self.z += x
        self.z = self.z[::-1]
        
        self.song = f'{self.y}{self.song_box.get(ACTIVE)}{self.z}'
        
    
      
        self.mixer.init()  #  iniciando mixer pygame
        
        self.musicanome.set(load(self.song).tag.title)
        self.artistanome.set(load(self.song).tag.album_artist)

        
        if self.v == 1:

            #  mudando o botão play para o botão pause
            self.img_btstart = PhotoImage(file='imagens/btpause.png')
            self.btstart['image'] = self.img_btpause
       
            self.mixer.music.load(self.song)
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
    

        self.time_bar.config(text=self.converted_time)
        self.time_bar.after(1000, self.playTime)

    
    def nextSong(self):  #  metodo para passar para o proximo som
        self.nextone = self.song_box.curselection()
        print(self.nextone)
        

    def addsong(self):
        self.song = filedialog.askopenfilename(initialdir='musicas/', title='escolha algum som', )
        print(self.song)
        self.song_box.insert(END, load(self.song).tag.title)
        
        
    def playTime(self):  #  metodo para mostrar o tempo da musica
        time = mixer.music.get_pos() / 1000
        self.converted_time = strftime('%H:%M:%S', gmtime(time)) 
              
        
# Codigo Principal

root = Tk()
mp3(root)

root.iconbitmap('favicon100.ico')
root.title('''                                    
Music Player
''')
root.geometry('375x667')
root.resizable(False, False)


root.mainloop()

