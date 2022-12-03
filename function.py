# Function is some instructions packaged together that perform specific task

# In Python You Can leave function blank without throw any errors by using "pass"

# ---------------------------------------------------------------------------- #
#                                Blank Function                                #
# ---------------------------------------------------------------------------- #
def blank_func():
     pass;

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #

# When you use function without Parentheses you refer to function in location
print(blank_func)
# To Execute this function we use parentheses
blank_func(); # execute body of function, no return will appear
print(blank_func()) # you execute function, and return value will appear

#DEF Difference between function, method, lambda

# function is used when you will reuse it through program many times and cen be do generic action

# method is used for specific object or data

# lambda is used when we want do some action in specific place, not entire program
# like we want do this actions on this array only, then it should be removed

# ---------------------------------------------------------------------------- #
#                              Default Parameters                              #
# ---------------------------------------------------------------------------- #
def sum(a, b):
     return a + b;

# print(sum()) # Wrong, You Must Pass 2 Parameters (required)
print(sum(1,2))

# If you want 2 parameters not must, you should make them default, to fall back it
def sum2(a=0,b=0):
     return a + b;

print(sum2())
print(sum2(1,2))

# *args, **kwargs
# args(Argument) refer to positional argument which you pass, without "key"
# and stored as tuple

# kwargs (Keyword Argument) refer to Named Arguments and stored as Dictionary (key, value)
# NOTE actually not have to be "args" or "kwargs" you can call them anything else
# but that is convention

# and it is like rest rest, spread operator in Javascript
# when you don't know how many arguments you want pass, you can use this way
def main(*args, **kwargs):
     print(args)
     print(kwargs)

main("Karim", "Muhammad", age="20", job="Student");

# If i want pass list, dictionary or list, whatever collection
# and i want pass their element individually, so you can unpacking with this way
# like we did in defination

def spread(*args):
     for arg in args:
          print(arg);

# One Pack
spread(["Karim", "Muhammad", "Zeyad", "Murad", "Abdo"])
# Unpack
spread(*["Karim", "Muhammad", "Zeyad", "Murad", "Abdo"])
# Like in Javascript we use Spread operator ... (triple dots) => ...array


# ---------------------------------------------------------------------------- #
#                                     TEST                                     #
# ---------------------------------------------------------------------------- #
courses = ["C++", "Java", "Javascript", "Python"];
# courses.append(*["Golang", "React", "Rust"]); Error
courses.extend(["Golang", "React", "Rust"]); # Correct way
print(courses)

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #
print(*["Hello", "World"], sep="-");

# print(**{"name": "karim"}); Error


# ---------------------------------------------------------------------------- #
#                                    Example                                   #
# ---------------------------------------------------------------------------- #
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

def is_leap(year):
     # """return True for leap years, False for non-leap years"""
     # docstring for document function or class
     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0);
     # no matter how leap year is calculated, what matter is how to code this

def days_in_month(year, month):
     """Return number of days in that month in that year"""
     if not 1<=month<= 12:
          return "Invalid Month";
     
     if month == 2 and is_leap(year):
          return 29;
     
     return month_days[month];

print(days_in_month(1900, 2)); # True
print(days_in_month(1904, 2)); # False