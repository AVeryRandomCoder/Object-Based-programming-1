class student:
  grade = int(input("Input a grade: "))
  name = input("Input a name: ")
  
  def introduction(self):
    print("Hi I am student")
    
  def details(self):
    print("My name is", self.name)
    print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()
