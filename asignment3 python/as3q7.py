class student:
  rno=0
  name=""
  Class=""
  age=0
  gen=""
  def accept(self,rno,name,Class,age,gen):
    self.rno=rno
    self.name=name
    self.Class=Class
    self.age=age
    self.gen=gen


  def display(self):
    print("Student rollno:",self.rno)
    print("Student name:",self.name)
    print("Student class:",self.Class)
    print("Student age:",self.age)
    print("Student gender:",self.gen)


class test(student):
  mar1=0
  mar2=0
  mar3=0
  def acceptt(self,mar1,mar2,mar3):
    self.mar1=mar1
    self.mar2=mar2
    self.mar3=mar3
  
  def displayt(self):
    print("Total marks: ",self.mar1+self.mar2+self.mar3)


stud=[]
n=int(input("Enter no_of_students:"))
for i in range(0,n):
  rno=int(input("Enter student rollno:"))
  name=input("Enter student name:")
  Class=input("Enter student class:")
  age=int(input("Enter student age:"))
  gen=input("Enter student gender:")
  mar1=int(input("Enter marks of subject1:"))
  mar2=int(input("Enter marks of subject2:"))
  mar3=int(input("Enter marks of subject3:"))
  print("\n")
  obj=test()
  obj.accept(rno,name,Class,age,gen)
  obj.acceptt(mar1,mar2,mar3)
print("Displaying student detail along with marks:\n")
for i in range(0,n):
  obj.display()
  obj.displayt()
  print("\n")
