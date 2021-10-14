class computer:
    def __init__(self,dispaly_size,ram,memory,graphics,price):
        self.display_size=dispaly_size
        self.ram=ram
        self.memory=memory
        self.graphics=graphics
        self.price=price
    def getspecs(self):
        self.display_size=float(input("enter the display size in inches: "))
        self.ram=int(input("enter the ram size in gb: "))
        self.memory=int(input("enter the size of memory in gb: "))
        self.graphics=int(input("enter the size of graphics in gb: "))
        self.price=int(input("enter the price in inr: "))
    def displayspecs(self):
        print("display size is:",self.display_size,"inches",
              "\nram is:", self.ram,"gb",
              "\nmemory is:", self.memory,"gb",
              "\ngraphics is:", self.graphics,"gb",
              "\nprice is:", self.price,"inr")
class desktop(computer):
    def getspecs_desktop(self):
        self.smps=input("enter yes or no if there is any smps: ")
    def displayspecs_desktop(self):
        print(self.smps)
class laptop(computer):
    def getspecs_laptop(self):
        self.weight=int(input("enter the weight of laptop in kg: "))
    def displayspecs_laptop(self):
        print("the weight of laptop is:",self.weight,"kg")

obj1=desktop('','','','','')
obj1.getspecs()
obj1.displayspecs()
obj1.getspecs_desktop()
obj1.displayspecs_desktop()

obj=laptop('','','','','')
obj.getspecs()
obj.displayspecs()
obj.getspecs_laptop()
obj.displayspecs_laptop()


