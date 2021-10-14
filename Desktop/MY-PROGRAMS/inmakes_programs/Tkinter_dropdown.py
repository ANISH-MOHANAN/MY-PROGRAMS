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

root.mainloop()