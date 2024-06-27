import csv
def printLoginMenu():
    print("1. Student")
    print("2. Faculty")
    m=input("Enter your choice :- ")
    if m=="1":
        r=input("Enter the roll number :- ")       
        s1=Student(r)
        s1.getDisplay()
    elif m=="2":
        print("1. Add Student")
        print("2. Update Student")
        print("3. Get Student Details")
        x=input("Enter your choice :- ")
        if x=="1":
            f1=Faculty()
            f1.addStudent()
        elif x=="2":
            r=input("Enter the Roll Number :- ")       
            f1=Faculty()
            f1.updateStudent(r)
        elif x=="3":
            r=input("Enter the Roll Number :- ")
            f1=Student(r)
            f1.getDisplay()
class Student:
    def __init__(self,roll):
        self.rollnumber = roll
        file=open("project.csv")
        self.dbReader=csv.reader(file)
    def getDeatils(self,roll):
        def search(x):
            if x[2]==roll:
                return x
        data = list(self.dbReader)
        myData=list(filter(search,data))
        return myData[0]
    def getDisplay(self):
        details=self.getDeatils(self.rollnumber)
        print(details)
class Faculty(Student):
    def __init__(self):
        file=open("project.csv")
        self.dbReader=csv.reader(file)
        
    def addStudent(self):
        fp=open("project.csv","a",newline="\n")
        dbWriter=csv.writer(fp)
        Name=input("Enter the Name :- ")
        Email=input("Enter the Email :- ")
        Roll_No=input("Enter the Roll No :- ")
        data=[Name,Email,Roll_No]
        dbWriter.writerow(data)
        fp.close()
        print("Student Added Successfully")
        
    def updateStudent(self,roll):
        data=list(self.dbReader)
        #print(*data,sep="\n")
        for row in data:
            if row[2]==roll:
                row[0]=input("Enter the Name :- ")
                row[1]=input("Enter the Email :- ")
                break
        fp=open("project.csv","w",newline="\n")
        dbWriter=csv.writer(fp)
        dbWriter.writerows(data)
        fp.close()
        print("Student Updated Successfully")
printLoginMenu()