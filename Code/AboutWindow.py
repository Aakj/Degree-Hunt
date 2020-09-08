from Tkinter import *
from PIL import ImageTk, Image
import os

def ending():
    root.destroy()
    
root=Tk()
w = 480 
h = 580 
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 40
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap('c:\Python27\DLLs\icon.ico')
root.title("DEGREE HUNT");
root.option_add("*background","Tan")
bottomFrame=Frame(root,background='tan')
bottomFrame.pack(side=BOTTOM)
button=Button(bottomFrame,text="Cancel",font=('Harrington',20,'bold'),command=ending,height=1,width=10,fg="black",bg="royal blue")
button.pack()
root.resizable(width=False,height=False)
rectangle=Canvas(root,width=1360,height=800)
rectangle.pack()
rectangle.create_rectangle(10,10,470,515,fill='light blue')
#Forte Gabriola
rectangle.create_text(10,10,anchor="nw",justify='center',font='comicsansms 25',text="               Developers:")
rectangle.create_text(10,50,anchor="nw",justify='center',font='Harrington 20',text="Aakrati Jain\n"+
                      " B.tech. Computer Engineering 2018\n"
                      "ZHCET, Aligarh Muslim University\n"+
                      "E-mail: aakrati.jain96@gmail.com\n")
rectangle.create_text(10,190,anchor="nw",justify='center',font='Harrington 20',text="Yamini Saraswat\n"+
                      "B.tech. Computer Engineering 2018\n"+
                      "ZHCET, Aligarh Muslim University\n"+
                      " E-mail: yamini.saraswat111@gmail.com\n")
rectangle.create_text(10,330,anchor="nw",justify='center',font='comicsansms 25',text="       Under the guidance of:")
rectangle.create_text(10,370,anchor="nw",justify='center',font='Harrington 20',text="         Miss. Syeda Shira Moin\n"+
                      "        M.tech. Computers\n"+
                      "         Aligarh Muslim University\n")

root.mainloop()
