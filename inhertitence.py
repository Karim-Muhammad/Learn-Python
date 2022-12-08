# the class can access attributes of inherited parent class


class Calculator:
     def __init__(self, x, y):
          self.x = x;
          self.y = y;
     
     def sum(self):
          return self.x + self.y;
     def subs(self):
          return self.x - self.y;
     
calc1 = Calculator(1,2);
print(calc1.sum())

class Scientific(Calculator):
     # def __init__(self, x,y,z):
     #      super()
     def prod(self):
          return self.x * self.y;

     def div(self):
          return self.x / self.y;

calc2 = Scientific(3,4);
print(calc2.div);

closu = calc2.div;
print(closu()) # Works, unlike javascript which give us undefined



# Example 2

class animal(object):
     def __init__(self, name) -> None:
          self.name = name;
     def eat(self, food):
          print("{} is eating {}".format(self.name, food))

class dog(animal):
     def fetch(self, thing):
          print("{} fetching {}".format(self.name, thing))

class cat(animal):
     # @override
     def eat(self, food):
          print("Cat is eating {}".format(food));

     def cat_eat(self, food):
          print("{} is eating {}".format(self.name, food));


# Example 3

class Date(object):
     def get_date(self):
          return "2022/10/19";
     
class Time(Date):
     def get_time(self):
          return "9:08:00";

d = Date();
print(d.get_date());

t = Time();
print(t.get_date())
print(t.get_time())



# This vs. Self

class Context:
     def __init__(self, name, age):
          self.name = name;
          self.age = age;
     
     def toString(self):
          return (
               f"I'm {self.name}, Iam from Egypt\n"
               f"my age is {self.age} years old."
          )
     
info = Context("Karim", 21);

method = info.toString;

print(method())

# if you did this in Javascript
# you will find Error, no name property of undefined!

# Example

class Polygon:
     def __init__(self, num_of_sides):
          self.num_sides = num_of_sides;
          self.sides_len = [0 for i in range(num_of_sides)];

     def set_sides(self):
          self.sides_len = [
               float(input(f"Enter Degree of Side {i+1} : ")) for i in range(self.num_sides)
          ]

     def display_sides(self):
          for i in range(self.num_sides):
               print(f"Degree Side {i+1}: {self.sides_len[i]}");

poly1 = Polygon(6);
# poly1.set_sides();
# poly1.display_sides()




class Triangle:
     def __init__(self):
          Polygon.__init__(self, 3);
          # became 
     # def findArea():
     #      return

triangle1 = Triangle();
print(triangle1)
print(dir(triangle1))
print(triangle1.num_sides) # 3
# Works but not visible in help
print("Instance?")
print(isinstance(triangle1, Triangle)) # True
print("is Subclass?")
print(issubclass(Triangle, Polygon)) # False
# Another Perspective
class Triangle2(Polygon):
     pass;


# triangle2 = Triangle2(); Error
triangle2 = Triangle2(8);
print(triangle2) # Check the properties
print(triangle2.num_sides)

print("Is Subclass2?")
print(issubclass(Triangle2, Polygon)) # True

# 3#

class Triangle3(Polygon):
     def __init__(self):
          Polygon.__init__(self, 3);
          # became derived class
 
     def findArea(self):
          a, b, c = self.sides_deg; # unpacking

          return

triangle3 = Triangle3();
print(triangle3) # Check the properties
print(triangle3.num_sides)

# 

# triangle3.set_sides();
print(triangle3.sides_len)

class Triangle4(Polygon):
     def __init__(self, num=3, deg=90):
          super().__init__(3);
          self.state = deg;
          # Polygon.__init__(self, 3)
     def details(self):
          super().display_sides();
          
#  First Check if derived class contains constructor so it will be executed
# if not, will execute constructor Super Class

triangle4 = Triangle4();
print(triangle4.num_sides)
triangle4.details();
print("-"*50)
triangle41 = Triangle4(5, 90);
triangle41.details()
print(triangle41.state)


