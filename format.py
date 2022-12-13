# ---------------------------------------------------------------------------- #
#                                    format %
#                                    InterPolation                             #
# ---------------------------------------------------------------------------- #

# format with .format(method)
print("{0} + {1} is equal {2}".format(1, 2, 3)) # 1 + 2 is equal to 3
print("{} + {} is equal {}".format(1, 2, 3)) # Works as well (without counting placeholders)
print("My name is {0}".format("Karim"))
# format with %
print("My age is %d %s" % (20, "old")); # like c-programming

person = {
     'name':"karim",
     'level': 3,
}
langs = ["HTML", "CSS", "JS", "Django", "PyQT"];


# Format
print("my name is {}, my level in college is {}".format(person["name"], person["level"]))
print("my name is {0[name]}, my level in college is {1[level]}".format(person, person))

# enhanced
print("my name is {0[name]}, my level in college is {0[level]}".format(person))

# Using UnPacking
print("my name is {name}, my level in college is {level}".format(**person))

# print("my name is {0.name}, my level in college is {0.level}".format(person)) Error
print("Skill 1 {0[0]}, Skill 2 {0[1]}".format(langs)) # doesn't work with dict

class Person():
     def __init__(self, name, level):
          self.name = name;
          self.level = level;
person1 = Person("Karim", 3);

# works with object
print("my name is {0.name}, my level in college is {0.level}".format(person1)) # isn't error after this
# it is works (with Object of Class NOT with literal Object)


# Formating with Numbers

for i in range(1, 11):
     sentence = "The Value is {:02}".format(i);
     print(sentence)


PI = 3.149489;
print("{:.3}".format(PI))
# 3 digits only


print("{:.2f}".format(PI))
# 2 float digits only

BigNum = 100000000;
# print("{:.1}".format(BigNum)) ValueError: Precision not allowed in integer format specifier

# 3
print("{:,}".format(BigNum))
# separated between tens with comma

# 4 Mix
print("{:,.2f}".format(BigNum))
# separated between tens with comma and limit decimal part with 2 only


# Date
import datetime;
date1 = datetime.datetime(2001, 10, 16, 10,30,39);
print(date1)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print("{:%B %m, %d(%A) == %H-%M-%S}".format(date1))