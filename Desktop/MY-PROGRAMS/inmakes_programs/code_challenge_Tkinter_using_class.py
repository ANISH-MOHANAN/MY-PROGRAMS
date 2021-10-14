from tkinter import *
class school:
    def __init__(self,details):
        frame = Frame(details)
        frame.pack()

        self.lable1=Label(frame,text="principal")
        self.lable1.pack()
        self.pbutton=Button(frame,text="click",command=self.pmsg)
        self.pbutton.pack()

        self.lable2 = Label(frame, text="teacher")
        self.lable2.pack()
        self.pbutton2 = Button(frame, text="click here", command=self.printmsg)
        self.pbutton2.pack()

        self.lable3 = Label(frame, text="student")
        self.lable3.pack()
        self.qbutton3=Button(frame,text="quit",command=frame.quit)
        self.qbutton3.pack()

    def pmsg(self):
        print("clicked")
    def printmsg(self):
        print("clicked here")

root=Tk()
obj=school(root)
root.mainloop()