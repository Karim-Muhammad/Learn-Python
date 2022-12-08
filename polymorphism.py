# 2 classes has same interface means(has a same name of method)

class Class1:
     def display(self):
          print("Class 1");
     
class Class2(Class1):
     # Override
     def display(self):
          print("Class 2");
          
class Class3(Class1):
     # No Override
     pass;


c1 = Class1();
c1.display(); # Class 1

c2 = Class2();
c2.display(); # Class 2

c3 = Class3();
c3.display(); # Class 1

