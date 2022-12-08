# first-class function help us to understand many term later on
# like "closure", "currying", "higher-order function"


# First-Class Function?
# Programming Languages is said to have a function-class function if it treats function as first-class citizens

# What is First-Class Citizens?
# A First-Class Citizen (Sometimes is called first-class objects) in programming languages is an entity which supports all the operations generally which available t other entities. These operations include being passed as argument, returned from function, assigned to a variable

# 1=> Assign it to a variable

def square(num):
     return num * num;

var1 = square(5);
print(var1) # 25
print(square) # <function x0<location>>

var2 = square;
print(var2) # <function x0<same_location>>

# same behavior as well in Javascript

# 2=> Passing as argument (Higher-order function)

def do_calc(func, num1, num2):
     return func(num1, num2);

print(do_calc(lambda n1,n2: n1+n2, 5, 9)); # => 14
print(do_calc(lambda n1,n2: n1-n2, 5, 9)); # => -4
print(do_calc(lambda n1,n2: n1*n2, 5, 9)); # => 45

def sum(n1, n2):
     return n1 + n2;

print(do_calc(sum, 10, 9)); # => 19

def my_map(func, arg_list):
     result = [];
     for itm in arg_list:
          result.append(func(itm));
     
     return result;
# 
own_map = my_map;
# 
new_list = my_map(lambda a: a*a, [1,2,3]);
print(new_list);

del globals()[my_map.__name__];
# print(my_map(lambda a: a*a, [5,3,7])) # doesn't work 
# print(own_map(lambda a: a*a, [5,3,7])) # works!

# 3 => return from a function (Higher-order function)

def reback(num1):
     def return_body(num2):
          return num1 + num2;

     return return_body;

print(reback(7)); 
print(reback(7)(10)); 
print(reback(3)(10)); 


def html_tag(tag):
     def wrap_text(text):
          return "<{0}> {1} </{0}>".format(tag, text);
     return wrap_text;
heading_tag = html_tag("h1");
parag_tag = html_tag("p");

print(heading_tag("Hello, World"));
print(heading_tag("Heading Tag"));
print(parag_tag("Text Pragraph"))
print(parag_tag("Good"))
# it remember what parameter which passed
# this called "closure", when you call function after while all info remembered


# Returning Function from function might be useful
# and it used in "decorators" term ,so you have to get it.