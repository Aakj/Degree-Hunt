x = 0
y = 25
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import pygame, sys
import time
import csv
import Fonting
import easygui
import random
import array
from pygame.sprite import Sprite
from Tkinter import *
from PIL import ImageTk, Image
from tileC import process

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("audio/merachaman_music.Ogg")
pygame.mixer.music.play();
pygame.display.set_icon(pygame.image.load('C:\Python27\DLLs\icon.ico'))

black=(0,0,0)
red=(255,0,0)
green=(67,233,94)
grey=(128,128,128)
blue=(0,0,255)
white=(255,255,255)
f=0
coor_x=0
coor_y=0
count=0
success=0
music=0
h=125
start_ticks=0

co_y=array.array('i',(0 for i in range(0,29)))
co_x=array.array('i',(0 for i in range(0,29)))
visited=array.array('i',(0 for i in range(0,29)))
strs = ["" for x in range(29)]

display_width=1370 #720
display_height=700 #440

gameDisplay=pygame.display.set_mode((display_width,display_height),0,32)

pygame.display.set_caption('DEGREE HUNT')
gameDisplay.fill(grey)
pygame.display.update()

gameExit=False

lead_x=display_width/2-20
lead_y=display_height-80
lead_x_change=0
lead_y_change=0
flag_lr=0
flag_ud=0


clock=pygame.time.Clock()
FPS=10
block_size=5
img_player=pygame.image.load("images/Player.jpg")
img_player=pygame.transform.scale(img_player,(50,50))

img_tree=pygame.image.load("images/sycus.jpg")
img_tree=pygame.transform.scale(img_tree,(50,50))

img_gate=pygame.image.load("images/gate.png")
img_gate=pygame.transform.scale(img_gate,(40,50))

img_lib=pygame.image.load("images/lib.jpg")
img_lib=pygame.transform.scale(img_lib,(50,50))

img_foot=pygame.image.load("images/football2.png")
img_foot=pygame.transform.scale(img_foot,(70,60))

img_art=pygame.image.load("images/Build9.png")
img_art=pygame.transform.scale(img_art,(70,60))

img_zakir=pygame.image.load("images/Build30.png")
img_zakir=pygame.transform.scale(img_zakir,(70,60))

img_elec=pygame.image.load("images/Build15.png")
img_elec=pygame.transform.scale(img_elec,(70,60))

img_civ=pygame.image.load("images/Build16.png")
img_civ=pygame.transform.scale(img_civ,(70,60))

img_comp=pygame.image.load("images/Build21.png")
img_comp=pygame.transform.scale(img_comp,(70,60))

img_poly_boys=pygame.image.load("images/Build6.jpg")
img_poly_boys=pygame.transform.scale(img_poly_boys,(70,60))

img_bed=pygame.image.load("images/Build19.png")
img_bed=pygame.transform.scale(img_bed,(70,60))

img_phe=pygame.image.load("images/Build17.jpg")
img_phe=pygame.transform.scale(img_phe,(70,60))

img_sn=pygame.image.load("images/Hostel1.png")
img_sn=pygame.transform.scale(img_sn,(70,60))

img_bb=pygame.image.load("images/Hostel2.png")
img_bb=pygame.transform.scale(img_bb,(70,60))

img_ques=pygame.image.load("images/question.jpg")
img_ques=pygame.transform.scale(img_ques,(70,60))

img_sul=pygame.image.load("images/hos_sul.png")
img_sul=pygame.transform.scale(img_sul,(70,60))

img_canteen=pygame.image.load("images/canteen.png")
img_canteen=pygame.transform.scale(img_canteen,(70,60))

img_ath_grnd=pygame.image.load("images/ath_grnd.png")
img_ath_grnd=pygame.transform.scale(img_ath_grnd,(70,60))

img_zoo=pygame.image.load("images/dept_zoo.png")
img_zoo=pygame.transform.scale(img_zoo,(70,60))

img_dept_comp=pygame.image.load("images/dept_comp.jpg")
img_dept_comp=pygame.transform.scale(img_dept_comp,(70,60))

img_wo_poly=pygame.image.load("images/wo_poly.png")
img_wo_poly=pygame.transform.scale(img_wo_poly,(70,60))

img_comp_cent=pygame.image.load("images/comp_cent.png")
img_comp_cent=pygame.transform.scale(img_comp_cent,(70,60))

img_minto=pygame.image.load("images/minto.png")
img_minto=pygame.transform.scale(img_minto,(70,60))

img_dept_chem=pygame.image.load("images/dept_chem.png")
img_dept_chem=pygame.transform.scale(img_dept_chem,(70,60))

img_flag=pygame.image.load("images/flag.png")
img_flag=pygame.transform.scale(img_flag,(30,40))

img_flag_change=pygame.image.load("images/flag_change.png")
img_flag_change=pygame.transform.scale(img_flag_change,(30,40))

img_tree3=pygame.image.load("images/tree3.jpg")
img_tree3=pygame.transform.scale(img_tree3,(100,100))

img_tree2=pygame.image.load("images/tree2.jpg")
img_tree2=pygame.transform.scale(img_tree2,(100,100))

img_tree1=pygame.image.load("images/tree1.jpg")
img_tree1=pygame.transform.scale(img_tree1,(100,100))


font=pygame.font.SysFont("Calibri",25,True,False)

def message_to_screen(msg,color,x,y,h):
    myfont=pygame.font.SysFont("monospace",h)
    screen_text=myfont.render(msg,True,color)
    gameDisplay.blit(screen_text,[x,y])

def question():
    global music
    music=1
    global f
    global start_ticks
    start_ticks=pygame.time.get_ticks()
    f=1
    with open('ques.csv') as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')
        rando=random.randrange(1,28,1)
        while visited[rando]==1:
            rando=random.randrange(1,28,1)
        k=0
        for row in readCSV:
            strs[k]=row[0]
            co_x[k]=int(row[1])
            co_y[k]=int(row[2])
            k=k+1
        easygui.msgbox('Question:'+strs[rando], title="Question")
        global coor_x
        coor_x=co_x[rando]
        global coor_y
        coor_y=co_y[rando]
        visited[rando]=1;
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds>10:
            pygame.mixer.music.load("audio/cheap_thrills.Ogg")
            pygame.mixer.music.play();
        
        
      
def button_fnc():
    cur = pygame.mouse.get_pos()
    if 100>cur[0]>50 and 680>cur[1]>625 :
        question()

    
    
        
def main_game(enter_x,enter_y):
    global count
    global success
    if enter_x-20<=coor_x<=enter_x+20 and enter_y-20<=coor_y<=enter_y+20 :
        img_flag_change=pygame.image.load("images/flag_change.png")
        img_flag_change=pygame.transform.scale(img_flag_change,(60,70))
        gameDisplay.blit(img_flag_change,(500,350))
        pygame.display.update()
        pygame.time.delay(500)
        img_flag_change=pygame.image.load("images/flag_change.png")
        img_flag_change=pygame.transform.scale(img_flag_change,(100,110))
        gameDisplay.blit(img_flag_change,(495,340))
        pygame.display.update()
        pygame.time.delay(500)
        img_flag_change=pygame.image.load("images/flag_change.png")
        img_flag_change=pygame.transform.scale(img_flag_change,(180,190))
        gameDisplay.blit(img_flag_change,(490,330))
        pygame.display.update()
        pygame.time.delay(500)
        success=success+1
        
    else:
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(60,70))
        gameDisplay.blit(img_flag_change_copy,(500,350))
        pygame.display.update()
        pygame.time.delay(500)
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(100,110))
        gameDisplay.blit(img_flag_change_copy,(495,340))
        pygame.display.update()
        pygame.time.delay(500)
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(180,190))
        gameDisplay.blit(img_flag_change_copy,(490,330))
        pygame.display.update()
        pygame.time.delay(500)
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(30,40))
        gameDisplay.blit(img_flag_change_copy,(h,650))
        count=count+1

while not gameExit:
    if music==0:
        pygame.mixer.music.load("audio/merachaman_music.Ogg")
        pygame.mixer.music.play();
        music=1
         
    
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if seconds==40 and f==1:
            pygame.mixer.music.load("audio/cheap_thrills.Ogg")
            pygame.mixer.music.play();
    
    if f==1:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds>50:
            root=Tk()
            icon=ImageTk.PhotoImage(file='icon.jpg')
            root.tk.call('wm','iconphoto',root._w,icon)
            root.title("DEGREE HUNT")
            w = 850 
            h = 600 

            ws = root.winfo_screenwidth() 
            hs = root.winfo_screenheight() 

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)

        
            root.geometry('%dx%d+%d+%d' % (w, h, x, y))

            root.option_add("*background","tomato")
            rectangle=Canvas(root,width=850,height=600)
            rectangle.pack()
            root.resizable(width=False,height=False)
            ply = ImageTk.PhotoImage(file='E:\Yamini Engineering\Work\pygame\images\out.jpg')
            ply_i=rectangle.create_image(400,340,image=ply)
            rectangle.create_text(100,50,anchor="nw",justify='left',font='Garamond 50',text="Time Up!!!")
            f = open('time.txt','r')
            line = f.readline()
            rectangle.create_text(100,50,anchor="nw",justify='left',font='Garamond 50',text=line)
            root.mainloop()
            count=count+1
            start_ticks=0
            f=0
    if start_ticks==0:
        pygame.mixer.music.load("audio/merachaman_music.Ogg")
        pygame.mixer.music.play();
         
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
            
            
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0 
            elif event.key==pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0 
            elif event.key==pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key==pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
            elif event.key==pygame.K_RETURN:
                enter_x=lead_x
                enter_y=lead_y
                if f==1:
                 seconds=(pygame.time.get_ticks()-start_ticks)/1000
                 if seconds>50:
                    easygui.msgbox('Time Up!!!', title="Question")
                 else:   
                    main_game(enter_x,enter_y)
                f=0
                

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                lead_x_change = 0
            if event.key==pygame.K_UP   or event.key==pygame.K_DOWN:
                lead_y_change = 0

    pre_loc_x=lead_x+lead_x_change
    pre_loc_y=lead_y+lead_y_change
    
    if pre_loc_x+50>=display_width:
        lead_x_change=0
        lead_y_change=0
    elif pre_loc_x<50:
        lead_x_change=0
        lead_y_change=0
    elif pre_loc_y>=display_height-50:
        lead_y_change=0
        lead_x_change=0
    elif pre_loc_y<0:
        lead_y_change=0
        lead_x_change=0
    elif pre_loc_x==660 and pre_loc_y<=750  and pre_loc_y>=556 and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_x==670 and pre_loc_y<=750  and pre_loc_y>=360 and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_y==560 and pre_loc_x<=655  and pre_loc_x>=290 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_y==550 and pre_loc_x<=655  and pre_loc_x>=330 and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_x==330 and pre_loc_y<=550  and pre_loc_y>=440 and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_y==440 and pre_loc_x<=660  and pre_loc_x>=330 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_x==660 and pre_loc_y<=550  and pre_loc_y>=440 and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_x==320 and pre_loc_y<=600  and pre_loc_y>=500 and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_y==430 and pre_loc_x<=660  and pre_loc_x>=330 and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_y==360 and pre_loc_x<=840  and pre_loc_x>=670 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_x==840 and pre_loc_y<=750  and pre_loc_y>=360 and event.key==pygame.K_LEFT:
        lead_x_change+=block_size

    elif pre_loc_y==550 and pre_loc_x<=1400 and pre_loc_x>=855 and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_y==560 and pre_loc_x<=1400 and pre_loc_x>=855 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size

    elif pre_loc_y==350 and pre_loc_x<=840  and pre_loc_x>=670 and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_x==850 and pre_loc_y<=750 and pre_loc_y>=560  and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_x==850 and pre_loc_y<=550 and pre_loc_y>=360  and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_y==360 and pre_loc_x<=1400 and pre_loc_x>=850 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_y==350 and pre_loc_x<=1400 and pre_loc_x>=850 and event.key==pygame.K_UP:
        lead_y_change+=block_size

    elif pre_loc_x==840 and pre_loc_y<=350 and pre_loc_y>=20   and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_x==850 and pre_loc_y<=350 and pre_loc_y>=230  and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_x==850 and pre_loc_y<=220 and pre_loc_y>=0    and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size

    elif pre_loc_y==20 and pre_loc_x<=835 and pre_loc_x>=60    and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_y==10 and pre_loc_x<=850 and pre_loc_x>=50    and event.key==pygame.K_UP:
        lead_y_change+=block_size

    elif pre_loc_x==60 and pre_loc_y<=490 and pre_loc_y>=20    and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size
        
    elif pre_loc_x==50 and pre_loc_y<=540 and pre_loc_y>=0     and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_y==490 and pre_loc_x<=320 and pre_loc_x>=60   and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_y==500 and pre_loc_x<=320 and pre_loc_x>=0    and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_x==660 and pre_loc_y<=430 and pre_loc_y>=200  and event.key==pygame.K_LEFT:
        lead_x_change+=block_size
        
    elif pre_loc_x==670 and pre_loc_y<=350 and pre_loc_y>=160  and event.key==pygame.K_RIGHT :
        lead_x_change-=block_size    

    elif pre_loc_y==190 and pre_loc_x<=710 and pre_loc_x>=320  and event.key==pygame.K_UP:
        lead_y_change+=block_size
        
    elif pre_loc_y==200 and pre_loc_x<=660 and pre_loc_x>=330  and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_x==330 and pre_loc_y<=430 and pre_loc_y>=200  and event.key==pygame.K_RIGHT:
        lead_x_change-=block_size
        
    elif pre_loc_x==320 and pre_loc_y<=490 and pre_loc_y>=160  and event.key==pygame.K_LEFT:
        lead_x_change+=block_size

    elif pre_loc_y==230 and pre_loc_x<=1400 and pre_loc_x>=850 and event.key==pygame.K_DOWN:
        lead_y_change-=block_size
        
    elif pre_loc_y==220 and pre_loc_x<=1400 and pre_loc_x>=850 and event.key==pygame.K_UP:
        lead_y_change+=block_size
       
    lead_x+=lead_x_change
    lead_y+=lead_y_change
        
    gameDisplay.fill(grey)
    
   
  
    gameDisplay.blit(img_player,(lead_x-40,lead_y))

 
    pygame.draw.rect(gameDisplay, green, (670,400,140,500),0)
    pygame.draw.rect(gameDisplay, green, (330,480,300,80),0)
    pygame.draw.rect(gameDisplay, green, (330,240,300,200),0)
    pygame.draw.rect(gameDisplay, green, (670,60,140,300),0)
    pygame.draw.rect(gameDisplay, green, (60,60,230,440),0)
    pygame.draw.rect(gameDisplay, green, (290,60,390,140),0)
    pygame.draw.rect(gameDisplay, green, (850,20,520,210),0)
    pygame.draw.rect(gameDisplay, green, (850,400,520,160),0)
    pygame.draw.rect(gameDisplay, green, (850,270,520,90),0)
    pygame.draw.rect(gameDisplay, green, (850,600,520,100),0)
    pygame.draw.rect(gameDisplay, green, (0,0,1370,20),0)
    pygame.draw.rect(gameDisplay, green, (0,0,20,700),0)
    pygame.draw.rect(gameDisplay, green, (20,540,270,70),0)
    pygame.draw.rect(gameDisplay, green, (20,600,610,100),0)
    pygame.draw.circle(gameDisplay, white,[400,670] ,25,2)
    pygame.draw.circle(gameDisplay, white,[400,670] ,20,2)
    pygame.draw.circle(gameDisplay, red,[400,670] ,19,0)
    message_to_screen("Timer",white,380,630,15)
    if f==1:
        message_to_screen(str((pygame.time.get_ticks()-start_ticks)/1000),white,395,660,15)
    gameDisplay.blit(img_tree,(400,300))
    gameDisplay.blit(img_gate,(630,650))
    gameDisplay.blit(img_lib,(540,480))
    gameDisplay.blit(img_flag,(635,480))
    gameDisplay.blit(img_foot,(400,480))
    gameDisplay.blit(img_flag,(400,440))
    gameDisplay.blit(img_art,(680,550))
    gameDisplay.blit(img_flag,(635,560))
    gameDisplay.blit(img_zakir,(730,400))
    gameDisplay.blit(img_flag,(740,360))
    gameDisplay.blit(img_civ,(850,470))
    gameDisplay.blit(img_flag,(815,480))
    gameDisplay.blit(img_elec,(920,490))
    gameDisplay.blit(img_flag,(920,560))
    gameDisplay.blit(img_comp,(1050,410))
    gameDisplay.blit(img_flag,(1070,360))
    gameDisplay.blit(img_poly_boys,(1200,490))
    gameDisplay.blit(img_flag,(1210,560))
    gameDisplay.blit(img_bed,(850,290))
    gameDisplay.blit(img_flag,(860,360))
    gameDisplay.blit(img_phe,(1220,160))
    gameDisplay.blit(img_flag,(1230,230))
    gameDisplay.blit(img_sn,(850,140))
    gameDisplay.blit(img_flag,(815,160))
    gameDisplay.blit(img_bb,(730,100))
    gameDisplay.blit(img_flag,(815,100))
    gameDisplay.blit(img_sul,(340,330))
    gameDisplay.blit(img_flag,(295,320))
    gameDisplay.blit(img_canteen,(550,270))
    gameDisplay.blit(img_flag,(635,270))
    gameDisplay.blit(img_ath_grnd,(710,240))
    gameDisplay.blit(img_flag,(815,240))
    gameDisplay.blit(img_wo_poly,(850,30))
    gameDisplay.blit(img_flag,(815,30))
    gameDisplay.blit(img_zoo,(550,120))
    gameDisplay.blit(img_flag,(550,200))
    gameDisplay.blit(img_dept_comp,(450,120))
    gameDisplay.blit(img_flag,(450,200))
    gameDisplay.blit(img_comp_cent,(350,120))
    gameDisplay.blit(img_flag,(350,200))
    gameDisplay.blit(img_minto,(100,120))
    gameDisplay.blit(img_flag,(25,120))
    gameDisplay.blit(img_dept_chem,(100,320))
    gameDisplay.blit(img_flag,(25,350))
    gameDisplay.blit(img_tree3,(190,220))
    gameDisplay.blit(img_tree2,(1000,50))
    gameDisplay.blit(img_tree2,(1100,50))
    gameDisplay.blit(img_tree2,(1200,50))
    gameDisplay.blit(img_tree1,(1200,600))
    gameDisplay.blit(img_tree1,(1100,600))
    gameDisplay.blit(img_tree1,(1000,600))
    gameDisplay.blit(img_tree1,(900,600))

    if success==1:
        pygame.mixer.music.load("audio/firework.Ogg")
        pygame.mixer.music.play();
        root=Tk()
        icon=ImageTk.PhotoImage(file='icon.jpg')
        root.tk.call('wm','iconphoto',root._w,icon)
        root.title("DEGREE HUNT")
        w = 850 
        h = 600 

        ws = root.winfo_screenwidth() 
        hs = root.winfo_screenheight() 

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        root.option_add("*background","light blue")
        rectangle=Canvas(root,width=850,height=600)
        rectangle.pack()
        root.resizable(width=False,height=False)
        plyi = ImageTk.PhotoImage(file='E:\Yamini Engineering\Work\pygame\images\doit.jpg')
        ply_ir=rectangle.create_image(500,400,image=plyi)
        ply = ImageTk.PhotoImage(file='E:\Yamini Engineering\Work\pygame\images\deg.jpg')
        ply_i=rectangle.create_image(150,340,image=ply)
        rectangle.create_text(100,50,anchor="nw",justify='left',font='Garamond 30',text="Congrats")
        f = open('student.txt','r')
        line = f.readline()
        rectangle.create_text(100,50,anchor="nw",justify='left',font='Garamond 30',text=line)
        line = f.readline()
        rectangle.create_text(100,100,anchor="nw",justify='left',font='Garamond 30',text=line)
        line = f.readline()
        rectangle.create_text(100,150,anchor="nw",justify='left',font='Garamond 30',text=line)

        
        root.mainloop()
        gameExit=True
       
    if count==1:
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(30,40))
        gameDisplay.blit(img_flag_change_copy,(125,650))
        gameDisplay.blit(img_flag,(180,650))
        gameDisplay.blit(img_flag,(235,650))
    elif count==2:
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(30,40))
        gameDisplay.blit(img_flag_change_copy,(125,650))
        gameDisplay.blit(img_flag_change_copy,(180,650))
        gameDisplay.blit(img_flag,(235,650))
    elif count==3:
        img_flag_change_copy=pygame.image.load("images/flag_wrong.png")
        img_flag_change_copy=pygame.transform.scale(img_flag_change_copy,(30,40))
        gameDisplay.blit(img_flag_change_copy,(125,650))
        gameDisplay.blit(img_flag_change_copy,(180,650))
        gameDisplay.blit(img_flag_change_copy,(235,650))

    elif count==4:
        root=Tk()
        icon=ImageTk.PhotoImage(file='icon.jpg')
        root.tk.call('wm','iconphoto',root._w,icon)
        root.title("DEGREE HUNT")
        w = 650 
        h = 600 

        ws = root.winfo_screenwidth() 
        hs = root.winfo_screenheight() 

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        root.option_add("*background","light blue")
        rectangle=Canvas(root,width=650,height=600)
        rectangle.pack()
        root.resizable(width=False,height=False)
        ply = ImageTk.PhotoImage(file='E:\Yamini Engineering\Work\pygame\images\playersad.png')
        ply_i=rectangle.create_image(300,350,image=ply)
        
        f = open('lost.txt','r')
        line = f.readline()
        rectangle.create_text(100,50,anchor="nw",justify='left',font='Garamond 30',text=line)
        line = f.readline()
        rectangle.create_text(100,100,anchor="nw",justify='left',font='Garamond 30',text=line)
        line = f.readline()
        rectangle.create_text(100,150,anchor="nw",justify='left',font='Garamond 30',text=line)
        root.mainloop()
        gameExit=True
    else:
        
        gameDisplay.blit(img_flag,(125,650))
        gameDisplay.blit(img_flag,(180,650))
        gameDisplay.blit(img_flag,(235,650))

   
    gameDisplay.blit(img_ques,(30,630))
    click = pygame.mouse.get_pressed()
    cur=pygame.mouse.get_pos()
    if click[0]==1 and 0<=cur[0]<=100 and 600<=cur[1]<=700 and f==0:
        button_fnc()

    #text
    message_to_screen("Department of Chemistry",black,80,380,15)
    message_to_screen("Minto Circle",black,80,200,15)
    message_to_screen("Computer Centre",black,320,180,15)
    message_to_screen("Computer Department",black,400,100,15)
    message_to_screen("Zoology Department",black,500,180,15)
    message_to_screen("Bibi Fatima",black,710,170,15)
    message_to_screen("Sarojini Naidu Hall",black,850,200,15)
    message_to_screen("Womens Polytechnic",black,860,90,15)
    message_to_screen("Maulana Azad Library",black,450,540,15)
    message_to_screen("Football",black,340,510,15)
    message_to_screen("Ground",black,340,530,15)
    message_to_screen("Atheletic Ground",black,670,230,15)
    message_to_screen("PHE Department",black,1220,140,15)
    message_to_screen("Sulaiman Hall",black,330,400,15)
    message_to_screen("Civil Department",black,850,440,15)
    message_to_screen("Electrical Department",black,965,540,15)
    message_to_screen("Faculty of Arts",black,670,620,15)
    message_to_screen("Education Department",black,850,345,15)
    message_to_screen("Boys polytechnic",black,1180,540,15)
    message_to_screen("Canteen",black,550,330,15)
    message_to_screen("Computer Department",black,990,400,15)
    message_to_screen("Zakir Husain",black,675,460,15)
    message_to_screen("College of",black,675,480,15)
    message_to_screen("Engineering and",black,675,500,15)
    message_to_screen("Technology",black,675,520,15)

    process(gameDisplay)
    pygame.display.update()
    clock.tick(FPS)
    

pygame.display.update()
time.sleep(2)
pygame.quit()
sys.exit()
quit()
