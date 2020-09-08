x1 = 0
y1 = 25
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x1,y1)
import pygame,sys
import Fonting
from Tkinter import *
from PIL import ImageTk,Image

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('DEGREE HUNT')
pygame.display.set_icon(pygame.image.load('C:\Python27\DLLs\icon.ico'))
white=(255,255,255)
black=(0,0,0)
green=(0,155,0)
grey=(128,128,128)
display_width = 800
display_height = 600
music_select=2
verysmallfont = pygame.font.SysFont("comicsansms",20)
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("Harrington",110)
gameDisplay=pygame.display.set_mode((1370,700))

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad-65))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        
def text_objects(text,color,size):
    if size=="verysmall":
        textSurface=verysmallfont.render(text,True,color)
    elif size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="verysmall"):
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
    
def text_to_button(msg,color, buttonx, buttony, buttonwidth, buttonheight, size = "verysmall"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    gameDisplay.blit(textSurf,textRect)

def button_fnc(x,y,width,height,active_color,action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if action=="story" or action=="how" or action=="optn" or action=="about" or action=="more":
            text_to_button("Click Me!",white,x,y,width,height)
        elif action=="play":
            text_to_button("Let's Play!",white,x,y,width,height)
        if click[0] == 1 and action != None:
            if action == "story":
                story()   
            if action == "how":
                how1()
            if action=="more":
                how2()
            if action == "play":
                play()
            if action == "about":
                about()
                pass
        pygame.display.update()

def button_fnc_on(x,y,radius,active_color,action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + 2*radius > cur[0] > x and y + 2*radius > cur[1] > y:
        pygame.draw.circle(gameDisplay,active_color,(x+35,y+35),radius,0)
        if 570> cur[0] >500:
            text_to_button("Mera",white,x+32,y+15,5,5)
            text_to_button("Chaman",white,x+32,y+36,5,5)
        elif 660> cur[0] >590:
            text_to_button("Mario",white,x+26,y+15,20,10)
            text_to_button("Tone",white,x+25,y+35,20,10)
        elif 750> cur[0] >680:
            text_to_button("Danger",white,x+25,y+19,20,10)
            text_to_button("Tone",white,x+25,y+39,20,10)
        if click[0] == 1 and action != None:
            if action == "Mera_chaman":
                pygame.mixer.music.load("merachaman_music.ogg")
                pygame.mixer.music.play();
                music_select=1
            if action == "Mario":
                pygame.mixer.music.load("mario_music.ogg")
                pygame.mixer.music.play();
                music_select=2
            if action == "Danger":
                pygame.mixer.music.load("Danger_tone.Ogg")
                pygame.mixer.music.play();
                music_select=3
                pass
        pygame.display.update()

def button_fnc_off(x,y,radius,active_color,action=None):
    global music_select
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + 2*radius > cur[0] > x and y + 2*radius > cur[1] > y:
        pygame.draw.circle(gameDisplay,active_color,(x+35,y+35),radius,0)
        text_to_button("No",white,x+27,y+15,20,10)
        text_to_button("Music!",white,x+27,y+35,20,10)
        if click[0] == 1 and action != None:
            if action == "no_music":
                music_select=0
                pygame.mixer.music.stop();
        pygame.display.update()

def save(entry,var,self):
        print("{}".format(entry.get()))
        addstudent = open ("student.txt", "w")
        addstudent.write("Congrats " + entry.get()+"\n"+"You are successful in finding your degree of\n "+var.get())
        addstudent.close ()

        time = open ("time.txt", "w")
        time.write("Time Up!!! " + entry.get()+"\n")
        time.close ()

        lost = open ("lost.txt", "w")
        lost.write(entry.get()+"\n"+"You just lost your degree of"+"\n"+var.get())
        lost.close ()
        self.destroy()
        from Window3 import *
        

def story():
    root=Tk()
    app=FullScreenApp(root)
    icon=ImageTk.PhotoImage(file='icon.jpg')
    root.tk.call('wm','iconphoto',root._w,icon)
    root.title("DEGREE HUNT")
    root.attributes("-topmost", True) #for bringing on top of other windows
    bottomFrame=Frame(root,background='tan')
    bottomFrame.pack(side=BOTTOM)
    button=Button(bottomFrame,text="Back to main screen",font=('Harrington',15,'bold underline'),command=root.destroy,height=2,width=18,fg="black",bg="royal blue")
    button.pack()
    root.option_add("*background","Tan")
    rectangle=Canvas(root,width=1360,height=800)
    rectangle.pack()
    root.resizable(width=False,height=False)
    rectangle.create_rectangle(10,10,1350,370,fill='light blue')
    #Forte Gabriola
    rectangle.create_text(100,30,anchor="nw",justify='center',font='Harrington 40 bold underline',text="               STORY BEHIND THE SCENE                ")
    rectangle.create_line(100,90,1225,90)
    rectangle.create_text(100,110,anchor="nw",justify='left',font='Garamond 30',text="You qualified for a degree from the renowned central"+
                          " university known as\n  Aligarh Muslim University. But a mishappening took place on the day of\n convocation. You were"+
                          " so contented that after receiving the degree you\ndropped it somewhere unknowingly! Don't get dishearten and help"+
                          " yourself\n         find the degree as it plays a paramount role in your future.")

    #Image 1
    mage1 = Image.open("Medicine.jpg")
    mage1 = mage1.resize((230,150), Image.ANTIALIAS)
    mg1 = ImageTk.PhotoImage(mage1)
    panel = Label(root,image = mg1)
    panel.place(x=10,y=540)
    #Image 2
    mage2 = Image.open("arts.jpg")
    mage2 = mage2.resize((230,150), Image.ANTIALIAS)
    mg2 = ImageTk.PhotoImage(mage2)
    panel = Label(root,image = mg2)
    panel.place(x=160,y=540)
    #Image 3
    mage3 = Image.open("law.jpg")
    mage3 = mage3.resize((230,150), Image.ANTIALIAS)
    mg3 = ImageTk.PhotoImage(mage3)
    panel = Label(root,image = mg3)
    panel.place(x=332,y=540)
    #Image 4
    mage4 = Image.open("business.jpg")
    mage4 = mage4.resize((235,150), Image.ANTIALIAS)
    mg4 = ImageTk.PhotoImage(mage4)
    panel = Label(root,image = mg4)
    panel.place(x=796,y=540)
    #Image 5
    mage5 = Image.open("mechanics.jpg")
    mage5 = mage5.resize((230,150), Image.ANTIALIAS)
    mg5 = ImageTk.PhotoImage(mage5)
    panel = Label(root,image = mg5)
    panel.place(x=990,y=540)
    #Image 6
    mage6 = Image.open("Science.jpg")
    mage6 = mage6.resize((220,150), Image.ANTIALIAS)
    mg6 = ImageTk.PhotoImage(mage6)
    panel = Label(root,image = mg6)
    panel.place(x=1130,y=540)
    #Image 7
    mage7 = Image.open("Engineering.jpg")
    mage7 = mage7.resize((230,150), Image.ANTIALIAS)
    mg7 = ImageTk.PhotoImage(mage7)
    panel = Label(root,image = mg7)
    panel.place(x=10,y=393)
    #Image 8
    mage8 = Image.open("Doctor1.jpg")
    mage8 = mage8.resize((230,150), Image.ANTIALIAS)
    mg8 = ImageTk.PhotoImage(mage8)
    panel = Label(root,image = mg8)
    panel.place(x=230,y=375)
    #Image 9
    mage9 = Image.open("Business1.jpg")
    mage9 = mage9.resize((230,150), Image.ANTIALIAS)
    mg9 = ImageTk.PhotoImage(mage9)
    panel = Label(root,image = mg9)
    panel.place(x=445,y=393)
    #Image 10
    mage10 = Image.open("Brains.jpg")
    mage10 = mage10.resize((235,150), Image.ANTIALIAS)
    mg10 = ImageTk.PhotoImage(mage10)
    panel = Label(root,image = mg10)
    panel.place(x=660,y=375)
    #Image 11
    mage11 = Image.open("Dental.jpg")
    mage11 = mage11.resize((230,150), Image.ANTIALIAS)
    mg11 = ImageTk.PhotoImage(mage11)
    panel = Label(root,image = mg11)
    panel.place(x=890,y=393)
    #Image 12
    mage12 = Image.open("Arts1.jpg")
    mage12 = mage12.resize((220,150), Image.ANTIALIAS)
    mg12 = ImageTk.PhotoImage(mage12)
    panel = Label(root,image = mg12)
    panel.place(x=1110,y=375)
    #Image 13
    mage13 = Image.open("Doctor.jpg")
    mage13 = mage13.resize((220,150), Image.ANTIALIAS)
    mg13 = ImageTk.PhotoImage(mage13)
    panel = Label(root,image = mg13)
    panel.place(x=570,y=479)
    root.mainloop()
    
def play():
    root=Tk()
    w = 700 
    h = 580 
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2) - 40
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    icon=ImageTk.PhotoImage(file='icon.jpg')
    root.tk.call('wm','iconphoto',root._w,icon)
    root.title("DEGREE HUNT");
    root.option_add("*background","Tan")
    root.attributes("-topmost", True)
    bottomFrame=Frame(root,background='tan')
    bottomFrame.pack(side=BOTTOM)
    button=Button(bottomFrame,text="Let's Play!!!",font=('Harrington',20,'bold'),command=lambda:save(entry,var,root),height=1,width=10,fg="black",bg="royal blue")
    button.pack()
    root.resizable(width=False,height=False)
    rectangle=Canvas(root,width=1360,height=800)
    rectangle.pack()
    rectangle.create_rectangle(10,10,690,515,fill='light blue')
    #Forte Gabriola
    rectangle.create_text(100,30,anchor="nw",justify='center',font='Harrington 30 bold underline',text="  STUDENT'S INFORMATION  ")
    rectangle.create_line(100,80,638,80)
    rectangle.create_text(30,100,anchor="nw",justify='center',font='Harrington 25 bold',text="Enter your name:")
    entry=Entry(root,font=("Garamond",20),width=40,bg="Cadet Blue")
    entry.place(x=30,y=150)
    rectangle.create_text(30,200,anchor="nw",justify='center',font='Harrington 25 bold',text="Select your qualification:")
    degrees = ['P.G. diploma','Bachelor of Arts (B.A.)','Bachelor of Engineering (B.E.)','Bachelor of Medicine and Bachelor of Surgery (M.B.B.S.)',
            'Bachelor of Laws (LL.B.)','Bachelor of Technology (B.tech.)','Master of Business Administration (M.B.A.)',
            'Master of Dental Surgery (M.D.S.)','Master of Laws (LL.M.)','Master of Science (M.Sc.)','Master of Arts (M.A.)',
            'Master of Commerce (M.Com.)','Master of Philosophy (M.Phil.)','Doctor of Philosophy (Ph.D.)']
    rectangle.create_text(250,450,anchor="nw",justify='center',font='Harrington 25 bold',text="All the best!!!")
    list = sorted(degrees)
    var = StringVar(root)
    drop = OptionMenu(root,var,*list)
    drop.place(x=30,y=250)
    drop.config(font=('Garamond',(20)),bg="Cadet Blue")
            

    #Image
    image = Image.open("Best.jpg")
    image = image.resize((65,90), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Label(root,image = img)
    panel.place(x=320,y=360)
    #ply = ImageTk.PhotoImage(file='E:\Yamini Engineering\Work\continue.png')
    #b = Button(root, borderwidth=2, text="Click Me", width=160,height=70, pady=5, command=save)
    #b.place(x=635,y=520)
    root.mainloop()

def ending(self):
    self.destroy()
    
def about():
    root=Tk()
    w = 480 
    h = 580 
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2) - 40
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    icon=ImageTk.PhotoImage(file='icon.jpg')
    root.tk.call('wm','iconphoto',root._w,icon)
    root.title("DEGREE HUNT");
    root.option_add("*background","Tan")
    root.attributes("-topmost", True)
    bottomFrame=Frame(root,background='tan')
    bottomFrame.pack(side=BOTTOM)
    button=Button(bottomFrame,text="Cancel",font=('Harrington',20,'bold'),command=root.destroy,height=1,width=10,fg="black",bg="royal blue")
    button.pack()
    root.resizable(width=False,height=False)
    rectangle=Canvas(root,width=1360,height=800)
    rectangle.pack()
    rectangle.create_rectangle(10,10,470,515,fill='light blue')
    #Forte Gabriola
    rectangle.create_text(10,10,anchor="nw",justify='center',font='comicsansms 25',text="               Developers:")
    rectangle.create_text(10,50,anchor="nw",justify='center',font='Harrington 20',text="Aakrati Jain\n"+
                          "   B.tech. Computer Engineering 2018\n"
                          "  ZHCET, Aligarh Muslim University\n"+
                          "   E-mail: aakrati.jain96@gmail.com\n")
    rectangle.create_text(10,190,anchor="nw",justify='center',font='Harrington 20',text="Yamini Saraswat\n"+
                          "B.tech. Computer Engineering 2018\n"+
                          "ZHCET, Aligarh Muslim University\n"+
                          " E-mail: yamini.saraswat111@gmail.com\n")
    rectangle.create_text(10,330,anchor="nw",justify='center',font='comicsansms 25',text="       Under the guidance of:")
    rectangle.create_text(10,370,anchor="nw",justify='center',font='Harrington 20',text="         Miss. Syeda Shira Moin\n"+
                          "        M.tech. Computers\n"+
                          "         Aligarh Muslim University\n")
    rectangle.create_text(30,470,anchor="nw",justify='center',font='comicsansms 25',text="Python:")
    rectangle.create_text(180,470,anchor="nw",justify='center',font='Harrington 20',text="version 2.7.12")
   

    root.mainloop()

def how1():
    root=Tk()
    app=FullScreenApp(root)
    icon=ImageTk.PhotoImage(file='icon.jpg')
    root.tk.call('wm','iconphoto',root._w,icon)
    root.title("DEGREE HUNT")
    root.option_add("*background","Tan")
    root.resizable(width=False,height=False)
    root.attributes("-topmost", True)
    bottomFrame=Frame(root,background='tan')
    bottomFrame.pack(side=BOTTOM)
    button=Button(bottomFrame,text="<< Back",font=('Harrington',20,'bold underline'),command=root.destroy,height=1,width=9,fg="black",bg="royal blue")
    button.pack(side=LEFT)
    rectangle=Canvas(root,width=1360,height=800)
    rectangle.pack()
    rectangle.create_rectangle(10,10,1350,635,fill='light blue')
    #Forte Gabriola
    rectangle.create_text(100,30,anchor="nw",justify='center',font='Harrington 40 bold underline',text="                           HOW TO PLAY ??                       ")
    rectangle.create_line(100,90,1225,90)
    rectangle.create_text(100,90,anchor="nw",justify='left',font='Garamond 30',text="The game consists of several questions which would be asked one after the\n"+
                                                                                    "another.The answers would be referring to a place or a building within the\n"+ 
                                                                                    " A.M.U. campus. So, the player needs to move to that destination and press\n"+
                                                                                    "'Enter' button to confirm th answer.To proceed further the player has to click\n"+
                                                                                    " on the question button again. Each question needs to be answered within the\n"+
                                                                                      " time span of '50 seconds'.A wrong answer would lead to the consumption of\n"+
                                                                                      " a trial.'Time's up' or 'Wrong answer with zero trials' means that the game is\n"+
                                                                                      " over.If the player is successful in answering 8 questions without losing all the\n"+
                                                                                      " trials,it means that the player has found his/her lost degree and he/she WINS\n"+
                                                                                       "the game! So, Let's Play!!")
    

                          
    root.mainloop()

def how2():
    root=Tk()
    app=FullScreenApp(root)
    icon=ImageTk.PhotoImage(file='icon.jpg')
    root.tk.call('wm','iconphoto',root._w,icon)
    root.title("DEGREE HUNT")
    root.resizable(width=False,height=False)
    root.option_add("*background","Tan")
    root.attributes("-topmost", True)
    bottomFrame=Frame(root,background='tan')
    bottomFrame.pack(side=BOTTOM)
    button=Button(bottomFrame,text="<< Back",font=('Harrington',20,'bold underline'),command=root.destroy,height=1,width=9,fg="black",bg="royal blue")
    button.pack(side=LEFT)
    rectangle=Canvas(root,width=1360,height=800)
    rectangle.pack()
    rectangle.create_rectangle(10,10,1350,635,fill='light blue')
    #Forte Gabriola
    rectangle.create_text(30,30,anchor="nw",justify='left',font='Harrington 40 bold underline',text="FOR MOVEMENT:")
    rectangle.create_line(30,90,455,90)
    rectangle.create_text(30,100,anchor="nw",justify='left',font='Garamond 30',text="Keyboard Keys:")
    rectangle.create_text(30,320,anchor="nw",justify='left',font='Harrington 40 bold underline',text="LIMITERS:")
    rectangle.create_line(30,380,280,380)
    rectangle.create_text(30,395,anchor="nw",justify='left',font='Garamond 30',text="Time limit:                                                          Trials:")
    rectangle.create_text(930,460,anchor="nw",justify='left',font='Garamond 20',text="(Three trials available)")
    rectangle.create_text(930,550,anchor="nw",justify='left',font='Garamond 20',text="(Only one trial left)")
    rectangle.create_text(330,470,anchor="nw",justify='left',font='Garamond 20',text="(For each question time limit\n"+"is 50 secs)")

    #Arrow Keys
    mage1 = Image.open("Arrowkeys.png")
    mage1 = mage1.resize((220,150), Image.ANTIALIAS)
    mg1 = ImageTk.PhotoImage(mage1)
    panel = Label(root,image = mg1)
    panel.place(x=100,y=150)
    #Enter Key
    image2 = Image.open("Enter.png")
    image2 = image2.resize((150,90), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image2)
    panel = Label(root,image = img2)
    panel.place(x=400,y=180)
    #Flag1
    image8 = Image.open("Flags.png")
    image8 = image8.resize((40,60), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(image8)
    panel = Label(root,image = img8)
    panel.place(x=735,y=450)
    #Flag2
    image9 = Image.open("Flags.png")
    image9 = image9.resize((40,60), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(image9)
    panel = Label(root,image = img9)
    panel.place(x=800,y=450)
    #Flag3
    image10 = Image.open("Flags.png")
    image10 = image10.resize((40,60), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(image10)
    panel = Label(root,image = img10)
    panel.place(x=865,y=450)
    #No_Flag1
    image11 = Image.open("No_Flags.png")
    image11 = image11.resize((40,60), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(image11)
    panel = Label(root,image = img11)
    panel.place(x=735,y=540)
    #No_Flag2
    image12 = Image.open("No_Flags.png")
    image12 = image12.resize((40,60), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(image12)
    panel = Label(root,image = img12)
    panel.place(x=800,y=540)
    #No_Flag3
    image13 = Image.open("Flags.png")
    image13 = image13.resize((40,60), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(image13)
    panel = Label(root,image = img13)
    panel.place(x=865,y=540)
    #Timer
    mage14 = Image.open("Timer.png")
    mage14 = mage14.resize((280,120), Image.ANTIALIAS)
    mg14 = ImageTk.PhotoImage(mage14)
    panel = Label(root,image = mg14)
    panel.place(x=30,y=450)
    root.mainloop()  
    
pygame.mixer.music.load("mario_music.Ogg")
pygame.mixer.music.play();
lead_x=230
a=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()

    img=pygame.image.load("bab_e_syed.jpg")
    img=pygame.transform.scale(img,(1390,720))
    gameDisplay.blit(img,(0,0))
    player=pygame.image.load("Player_b.jpg")
    player=pygame.transform.scale(player,(60,80))
    gameDisplay.blit(player,(lead_x,310))
    pygame.draw.line(gameDisplay,black,(0,15),(1370,15),3)
    pygame.draw.line(gameDisplay,black,(0,20),(1370,20),3)
    pygame.draw.line(gameDisplay,black,(0,685),(1370,685),3)
    pygame.draw.line(gameDisplay,black,(0,680),(1370,680),3)
    pygame.draw.line(gameDisplay,black,(15,0),(15,700),3)
    pygame.draw.line(gameDisplay,black,(20,0),(20,700),3)
    pygame.draw.line(gameDisplay,black,(1345,0),(1345,700),3)
    pygame.draw.line(gameDisplay,black,(1350,0),(1350,700),3)
        
    if a==0:
        lead_x+=20
    else:
        lead_x-=20
    if lead_x>=1050:
        a=1
    elif lead_x<=230:
        a=0
   
    if music_select!=0:
        if pygame.mixer.music.get_busy()==False:
            if music_select==1:
                pygame.mixer.music.load('merachaman_music.ogg')
                pygame.mixer.music.play()
            elif music_select==2:
                pygame.mixer.music.load('mario_music.Ogg')
                pygame.mixer.music.play()
            elif music_select==3:
                pygame.mixer.music.load('Danger_tone.Ogg')
                pygame.mixer.music.play()
                #pygame.mixer.music.rewind()
        
    logo=pygame.image.load("Logo.jpg").convert()
    logo=pygame.transform.scale(logo,(100,100))
    gameDisplay.blit(logo,(610,36))
    logo=pygame.image.load("DegreeHunt.png").convert()
    logo=pygame.transform.scale(logo,(150,50))
    gameDisplay.blit(logo,(590,236)) 
    button=pygame.image.load("introduction.png").convert()
    button=pygame.transform.scale(button,(120,65))
    gameDisplay.blit(button,(230,400))
    button=pygame.image.load("how_to_play.png").convert()
    button=pygame.transform.scale(button,(120,65))
    gameDisplay.blit(button,(230,520))
    button=pygame.image.load("play_game.png").convert()
    button=pygame.transform.scale(button,(120,65))
    gameDisplay.blit(button,(615,400))
    button=pygame.image.load("about_dev.png").convert()
    button=pygame.transform.scale(button,(120,65))
    gameDisplay.blit(button,(1000,520))
    button=pygame.image.load("button_more.png").convert()
    button=pygame.transform.scale(button,(120,65))
    gameDisplay.blit(button,(1000,400))
    button=pygame.image.load("Music2.jpg").convert()
    button=pygame.transform.scale(button,(70,70))
    gameDisplay.blit(button,(500,590))
    button=pygame.image.load("Music1.jpg").convert()
    button=pygame.transform.scale(button,(70,70))
    gameDisplay.blit(button,(590,590))
    button=pygame.image.load("Music3.jpg").convert()
    button=pygame.transform.scale(button,(70,70))
    gameDisplay.blit(button,(680,590))
    button=pygame.image.load("No_music.jpg").convert()
    button=pygame.transform.scale(button,(70,70))
    gameDisplay.blit(button,(770,590))
    message_to_screen("                   DEGREE HUNT",black,-120,"large")
    message_to_screen("                                                                            SELECT MUSIC:",black,260,"small")

    button_fnc(230,400,120,67,black,action="story")
    button_fnc(230,520,120,67,black,action="how")
    button_fnc(615,400,120,67,black,action="play")
    button_fnc(1000,520,120,67,black,action="about")
    button_fnc(1000,400,120,67,black,action="more")
    button_fnc_on(500,590,36,black,action="Mera_chaman")
    button_fnc_on(590,590,36,black,action="Mario")
    button_fnc_on(680,590,36,black,action="Danger")
    button_fnc_off(770,590,36,black,action="no_music")
    pygame.display.update()
