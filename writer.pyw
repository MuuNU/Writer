from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox as mb
import os


def refresh():
    titles = os.listdir()
    S=(box.size() - 1)
    box.delete(0,S)
    for i in titles:
        box.insert(END,i)

def btn1Pressed():
    titles = os.listdir()
    num = 1+ (len(titles))
    txtf = 'New_Text_' + str(num)
    while os.path.isfile(txtf) == 1:
        num = num+1
        txtf = 'New_Text_' + str(num)

    thsFile = open(txtf, 'a+')
    thsFile.close
        
    refresh()


#def btn1Pressed():
#    titles = os.listdir()
#    num = 1+ (len(titles))
#    txtf = 'New_Text_' + str(num)
#    if ((os.path.isfile(txtf)) == 1):  
#        thsFile = open(txtf, 'a+')
#        thsFile.close
#    else:
#        while os.path.isfile(txtf) == 0:
#            num = num+1
#        num = 1+ (len(titles))
#        txtf = 'New_Text_' + str(num)
#        thsFile = open(txtf, 'a+')
#        thsFile.close
#    refresh()






def btn2Pressed():
    index = box.curselection()
    name = (box.get(index))
    os.remove(name)
    refresh()
    
def boxSelected(*args):
    global name
    global f
    index = box.curselection()
    name = (box.get(index))
    title.configure(text=name)
    f = open(name, 'r+')
    text = f.read()
    txt.delete(0.0, END)
    txt.insert(0.0, text)
    f.close()


def btnRenPressed():
    global name
    index = box.curselection()
    ReW = Tk()  
    ReW.title("Enter new name")
    window.geometry('500x600')
    frameRename=Frame(ReW,bd=2)
    frameButtons12=Frame(ReW,bd=2)
    frameRename.pack(side='top')
    frameButtons12.pack(side='bottom')
    entryRe=Entry(frameRename)


    entryRe.insert(0,name)

    
    entryRe.pack()
    compBut=Button(frameButtons12, text="Rename", command=lambda: BSave(entryRe, name))
    compBut.pack(side="left")
    noButton=Button(frameButtons12, text="Exit", command=ReW.destroy)
    noButton.pack(side='right')
    ReW.mainloop()

def BSave(entryRe, name):
    
    nName = entryRe.get()
    if os.path.isfile(nName) == 0:       
        os.rename(name,nName)
    refresh()

def btnSVPressed():
    global name
    
    f = open (name, 'r+')
    text = txt.get(0.0, END)
    f.write(text)


def myf():
    if mb.askokcancel("Quit", "Do you want to quit? You can lost all unsaved data"):
        window.destroy()


name = None

os.chdir('texts')
titles = os.listdir()
window = Tk()  
window.title("msin")
window.minsize(640,480)
window.geometry('1000x800')
window.protocol('WM_DELETE_WINDOW', myf)

# Главный фрейм
mainFrame=Frame(window,bd=5)
mainFrame.pack(fill="both", expand="true")

# Левый и правый фреймы
leftFrame=Frame(mainFrame,bd=2)
leftFrame.pack(side='left',fill=Y)
rightFrame=Frame(mainFrame,bd=2)
rightFrame.pack(side='right',fill="both", expand="true")

# Содержимое левого фрейма
btnFrame=Frame(leftFrame,bd=8)
boxFrame=Frame(leftFrame,bd=2)

# Содержимое правого фрейма
txtFrame=Frame(rightFrame,bd=5)
topFrame=Frame(rightFrame,bd=2)
topFrame.pack(side='top')

# Содержимое верхнего фрейма
titleFrame=Frame(topFrame,bd=2)
titleFrame.pack(fill="both", expand="true")

# Содержимое заголовочного фрейма
saveFrame=Frame(titleFrame,bd=2)
saveFrame.pack(side='left',fill="both")

btnRen = Button(saveFrame, text="Rename",command=btnRenPressed)
btnSave = Button(saveFrame, text="Save",command=btnSVPressed)
btnRen.pack(side='left')
btnSave.pack(side='right')

# Лейбл с полем ввода заголовка
title = Label(titleFrame, width=50, bd=2)
title.pack(fill="both", expand="true")

# Листбокс
box = Listbox(boxFrame, bd=2, selectmode=BROWSE)
for i in titles:
    box.insert(END,i)
box.bind('<<ListboxSelect>>', boxSelected)
box.pack(expand=True, fill=Y)
boxFrame.pack(side='bottom',expand=True,fill=Y)

# Кнопка
btn1 = Button(btnFrame,text="New",command=btn1Pressed)
btn1.pack(side='left')

btn2 = Button(btnFrame,text="Del",command=btn2Pressed)
btn2.pack(side='right')
btnFrame.pack(side='top')


# Поле ввода текста
txt = scrolledtext.ScrolledText(txtFrame, bd=2)
txt.pack(fill="both", expand="true")
txtFrame.pack(side="bottom",fill="both", expand="true")




window.mainloop()
