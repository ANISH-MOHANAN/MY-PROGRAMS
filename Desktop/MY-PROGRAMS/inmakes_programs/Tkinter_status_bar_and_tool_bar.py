from tkinter import *
root=Tk()

def fun():
    print("changes are reverted")
mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new project")
submenu.add_command(label="new scratch file")
submenu.add_separator()
submenu.add_command(label="open")
submenu.add_command(label="save as")
newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo",command=fun)

#adding toolbar and button inside toolbar
toolbar=Frame(root,bg="pink")
inbutton=Button(toolbar,text="crop")
inbutton.pack(side=LEFT,padx=2,pady=2)
inbutton1=Button(toolbar,text="paste")
inbutton1.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#setting status bar
statusbar=Label(root,text="this is status bar",relief=SUNKEN,bd=2,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)
root.mainloop()
