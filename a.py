class student :
    rno=10#data member
    name="Lohisree"#data member
    grade=7#data member
    def intro(self):#member function
       print("Hi This is",self.name,"and my roll number is",self.rno)
    def det(self):#member function
       print("and I am in grade",self.grade)
o1=student()#object creation
o1.intro()
o1.det()
o2=student()#object creation
o2.intro()
o2.det()

