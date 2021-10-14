class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name: ")
        self.mark=int(input("enter your mark: "))
    def putdetails(self):
        print(self.name,self.mark)
class teacher():
    def display(self):
        print("am derived class1")
class parent():
    def printdetails(self):
        print("am derived class 2")
class admin(student,teacher,parent):
    def newfun(self):
        print("am derived class 3")
obj=admin('','')
obj.getdetails()
obj.putdetails()
obj.display()
obj.printdetails()
obj.newfun()