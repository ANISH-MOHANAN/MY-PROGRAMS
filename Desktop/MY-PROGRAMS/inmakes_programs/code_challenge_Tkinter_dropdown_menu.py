from tkinter import *
root=Tk()

def fun():
    print("this is new project")
def fun1():
    print("this is new file")
def fun2():
    print("this is new scratch file")
def fun3():
    print("opening file")
def fun4():
    print("saving file as")
def fun5():
    print("opening recent file")


def fun6():
    print("undoing typed")
def fun7():
    print("redoing typed")
def fun8():
    print("cutting file ")
def fun9():
    print("copying file")
def fun10():
    print("copying file path")
def fun11():
    print("pasting file")

def fun12():
    print("opening tool windows")
def fun13():
    print("changing appearances")
def fun14():
    print("giving quick definitions")
def fun15():
    print("giving quick type definitions")
def fun16():
    print("doing quick documentation")
def fun17():
    print("showing parameter information")

def fun18():
    print("navigating backwards")
def fun19():
    print("navigating forward")
def fun20():
    print("seraching everywhere")
def fun21():
    print("navigating to class")
def fun22():
    print("navigating to file")
def fun23():
    print("navigating to given symbol")

def fun24():
    print("overriding methods")
def fun25():
    print("implementing methods")
def fun26():
    print("generating code")
def fun27():
    print("completing code")
def fun28():
    print("inserting live templates")
def fun29():
    print("surrounding with")

def fun30():
    print("refactoring this file")
def fun31():
    print("renaming this file")
def fun32():
    print("changing signature")
def fun33():
    print("moving file ")
def fun34():
    print("copying file")
def fun35():
    print("deleting safely")

mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)

submenu.add_command(label="new project",command=fun)
submenu.add_command(label="new",command=fun1)
submenu.add_separator()
submenu.add_command(label="new scratch file",command=fun2)
submenu.add_command(label="open",command=fun3)
submenu.add_separator()
submenu.add_command(label="save as",command=fun4)
submenu.add_command(label="open recent",command=fun5)
submenu.add_separator()
submenu.add_command(label="Exit",command=root.quit)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)

newmenu.add_command(label="undo",command=fun6)
newmenu.add_command(label="redo",command=fun7)
newmenu.add_separator()
newmenu.add_command(label="cut",command=fun8)
newmenu.add_command(label="copy",command=fun9)
newmenu.add_separator()
newmenu.add_command(label="copy path",command=fun10)
newmenu.add_command(label="paste",command=fun11)

newmenu2=Menu(mymenu)
mymenu.add_cascade(label="view",menu=newmenu2)

newmenu2.add_command(label="Tool Windows",command=fun12)
newmenu2.add_command(label="Appearence",command=fun13)
newmenu2.add_separator()
newmenu2.add_command(label="Quick definition",command=fun14)
newmenu2.add_command(label="Quick documentation",command=fun15)
newmenu2.add_separator()
newmenu2.add_command(label="Parameter info",command=fun16)
newmenu2.add_command(label="Type info",command=fun17)

newmenu3=Menu(mymenu)
mymenu.add_cascade(label="Navigate",menu=newmenu3)

newmenu3.add_command(label="Back",command=fun18)
newmenu3.add_command(label="Forward",command=fun19)
newmenu3.add_separator()
newmenu3.add_command(label="Search everywhere",command=fun20)
newmenu3.add_command(label="Class",command=fun21)
newmenu3.add_separator()
newmenu3.add_command(label="File",command=fun22)
newmenu3.add_command(label="Symbol",command=fun23)

newmenu4=Menu(mymenu)
mymenu.add_cascade(label="Code",menu=newmenu4)

newmenu4.add_command(label="Override methods",command=fun24)
newmenu4.add_command(label="Implement methods",command=fun25)
newmenu4.add_separator()
newmenu4.add_command(label="Generate",command=fun26)
newmenu4.add_command(label="Code completion",command=fun27)
newmenu4.add_separator()
newmenu4.add_command(label="Insert live template",command=fun28)
newmenu4.add_command(label="Surround with",command=fun29)

newmenu5=Menu(mymenu)
mymenu.add_cascade(label="Refactor",menu=newmenu5)

newmenu5.add_command(label="Refactor this",command=fun30)
newmenu5.add_command(label="Rename",command=fun31)
newmenu5.add_separator()
newmenu5.add_command(label="Change signature",command=fun32)
newmenu5.add_command(label="Move file",command=fun33)
newmenu5.add_separator()
newmenu5.add_command(label="Copy file",command=fun34)
newmenu5.add_command(label="Safe delete",command=fun35)

root.mainloop()