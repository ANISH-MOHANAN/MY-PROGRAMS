class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name: ")
        self.mark=int(input("enter your mark: "))
    def putdetails(self):
        print(self.name,self.mark)
class teacher(student):
    def display(self):
        print("am derived")

obj=teacher('','')
obj.getdetails()
obj.putdetails()
obj.display()
