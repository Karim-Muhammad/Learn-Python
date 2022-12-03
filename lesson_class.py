class car():
     wheels = 4;
     color = "green";

     def open_door(self):
          print(self)
          print("Open The Door");
     def close_door(self):
          # 'self' -> refer to object which called method
          print(self.wheels)
          print("Close The Door");
     def test_self(self):
          print(self);


car1 = car();
print(car1.color)
car1.color = "gray";
print(car1.color)

# Call Methods

# car1.open_door();
# These forms can make you understand the logic
car1.test_self(); 
# car.test_self();  Error
car.test_self(car1);
# Classes themselves considered as object in Python
print(car.color)

# Methods is a function defined within class
# callable attribute
# Every Method is a attribute, but not every attribute is a method

# NOTE
# Python Always pass a variable to class as parameter
# and every method as well, if it hasn't any params
# but it accepts one param mendatory
# and this param is <name_of_object>

# Self is placeholder for created object

# self like "this"
# this instance will be placed into "self"

class cons():
     def __init__(self, name, age, job)-> None:
          self.name = name;
          self.age = age;
          self.job = job;
          self.get = lambda inf: self.__getattribute__(inf);
          # print(self.__getattribute__("name"))
     def get_birth_year(self):
          return 2022 - self.age;


obj1 = cons("karim", 21, "student");
print(obj1.get("job"));

# subscriptable -> means accept [index, key] or not

print(obj1.get_birth_year())