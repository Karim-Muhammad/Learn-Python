# Constructor is a special method
# which is called automatically when instance is constructed

# __init__(self)

class Student:
     color = "green";

     def __init__(self, name, age) -> None:
          self.name = name; # Instance Attr only
          self.age = age;
          print("Object is constructed!");

     # Class Method (Can used with object ofc)
     def details(self):
          return "{0} my name is {1}, age {2} years old {0}".format("~~~", self.name, self.age);



# Class Attribute & Instance Attribute
# Attributes is a variable in the class accessible through the instance
# instance attribute are also accessible by instance
# when we use this syntax object.attribute, we look up
# the attribute
#    1- first in instance
#    2- second in class itself
#    3- third in the class which class inherit from

# a method on instance passes instance as a first argument
# to a method(self)
# 
# instance have their own data called instance attributes
# variables defined in the class are called class attributes
#  


student1 = Student("Karim", 22);

print(dir(student1));
print("#"* 10)
print(dir(Student));


print(Student.color) # Green
print(student1.color) # first it look up in instance
# not found? so go to parent, it is found with "green" value
# so it will print "green"

student1.color = "purple";
# here i create a attribute for instance (isolated) to parent attribute
# i don't change value of color class, it still as it is

# when i print
print(student1.color); # first look up in instance attribute
# it found? Yeah! it found with value "Purple"
# but it still found in class it self with "Green" Value

print("---"*30);

class Learn:
     class_value = "Class Value";

learn1 = Learn();
print(learn1.class_value);

learn1.class_value="Instance Variable";
print(learn1.class_value);

del learn1.class_value;
print(learn1.class_value);