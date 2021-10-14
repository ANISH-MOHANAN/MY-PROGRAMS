from tkinter import *
root=Tk()

def fun():
    print("click here")
Button(root,text="ok",command=fun).pack()

root.mainloop()