class hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin=admin
        self.doctor=doctor
        self.sister=sister
        self.department=department
    def getdetails(self):
        self.admin=input("enter the admin name: ")
        self.doctor=input("enter the doctor name: ")
        self.sister=input("enter the sister name: ")
        self.department=input("enter the department name: ")
class department(hospital):
    def putdetails(self):
        print(self.admin,self.doctor,self.sister,self.department)
class patientward:
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
    def patientdetails(self):
        self.name=input("enter patient name: ")
        self.age=input("enter the patient age: ")
        self.disease=input("enter the disease: ")
    def printpatient(self):
        print(self.name,self.age,self.disease)
obj=department('','','','')
obj.getdetails()
obj.putdetails()
obj=patientward('','','')
obj.patientdetails()
obj.printpatient()



# #if we use multiple inheritance
# class anything(hospital,department,patientward):
#     def something(self):
#         print("anything")
# obj=anything('','','','','','','')
# obj.getdetails()
# obj.putdetails()
# obj.patientdetails()
# obj.printpatient()
