from tkinter import *
root=Tk()

l1=Label(root,text="username")
l2=Label(root,text="mobile number")
l3=Label(root,text="email id")
l4=Label(root,text="age")
l5=Label(root,text="password")
l6=Label(root,text="confirm password")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)
entry6=Entry(root)

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
l3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
l4.grid(row=3,column=0)
entry4.grid(row=3,column=1)
l5.grid(row=4,column=0)
entry5.grid(row=4,column=1)
l6.grid(row=5,column=0)
entry6.grid(row=5,column=1)


button1=Button(root,text="login")
button2=Button(root,text="cancel")

button1.grid(row=6,column=0)
button2.grid(row=6,column=1)

root.mainloop()