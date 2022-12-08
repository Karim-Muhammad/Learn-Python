# In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function[a] together with an environment.[1] The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.


# Closures are also frequently used with callbacks, particularly for event handlers, such as in JavaScript, where they are used for interactions with a dynamic web page. 


greeting = "Hi!";

# Question 1
def salam1(name):
     greeting = "Hello!";
     def greet():
          return f"{greeting}, {name}";
     return greet;

print(salam1("karim")())

# Question 2
def greet(name):
     return f"{greeting}, {name}";

def salam2(name):
     greeting = "Hola!"; # Not free variable
     return greet(name);

print(salam2("karim")); # Hi! NOT Hola!

# free variable means, variable located in outer function, and inner function trying to access it

# https://youtu.be/swU3c34d2NQ?t=289

# closure is inner function remember and access to variable of outer function


import logging
logging.basicConfig(filename="example.log", level=logging.INFO);

def logger(func):
     def log_func(*args):
          logging.info("Running '{}' with arguments {}".format(func.__name__, args))
          print(func(*args));

     return log_func;
     
def sum(x, y):
     return x + y;

def sub(x, y):
     return x - y;

add_logger = logger(sum);
sub_logger = logger(sub);

add_logger(1,2);
sub_logger(9, 3);
# add_logger(1,2,3,4,5); Error

# We can get benefit of closures in many many things
# decorators, event-handlers, callbacks, higher-order functions

