class overlaoding:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __mul__(self, other):
        a=self.a+other.a
        b=self.b+other.b
        return overlaoding(a,b)
    def __str__(self):
        return "({0},{1})".format(self.a,self.b)
p1=overlaoding(2,4)
p2=overlaoding(6,8)
print(p1*p2)