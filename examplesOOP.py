class Student:
     def __init__(self, name):
          self.name = name;
          self.marks = [];
          print(f"Welcome {name} to the school");

     def add_marks(self, mark):
          self.marks.append(mark);
     def avg(self):
          return sum(self.marks)/len(self.marks);
     

student1 = Student("Karim");
student1.add_marks(99);
student1.add_marks(100);
student1.add_marks(100);
student1.add_marks(101);

average = student1.avg();

print(average);

# Class Name(): |OR| Class Name:
# in Desktop GUI you use Name()

class calculator:
     def __init__(self, number1, number2):
          self.num1 = number1;
          self.num2 = number2;
     
     def sum(self):
          return self.num1 + self.num2;
     
     def multi(self):
          return self.num1 * self.num2;

calc = calculator(9, 2);
print(calc.sum());
print(calc.multi());