class Student:
    def getStudentDetails(self):
        self.rollno=input("Enter Roll Number : ")
        self.name = input("Enter Name : ")


    def printResult(self): 
        print(self.rollno,self.name)

S1=Student()
S1.getStudentDetails()
