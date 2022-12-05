import builtins


# scope variables means
# where our variables can be accessed in our program
# and what values that variables holds in different context

#  Using Python scope will help you avoid or minimize bugs related to name collision as well as bad use of global names across your programs.

# LEGB -> L: Local, E: Enclosing, G: Global, B: Built-in
# This summarizes not only the Python scope levels but also the sequence of steps that Python follows when resolving names in a program.

# What is Scope in Python, How it works

# Why it's important to know Scope in Python

# What the LEGB rule is and how Python uses it to resolve names

# How to modify the standard behavior of Python scope using global and nonlocal

# What scope-related tools Python offers and how you can use them


#NOTE Compare:
# Global scope: The names that you define in this scope are available to all your code.

# Local scope: The names that you define in this scope are only available or visible to the code within the scope.
# 

# x = "global x"; # Try to Comment this line, and see what will happen

def loc():
     global x;
     # make variable x global even it is not defined outside
     y='local y';
     x='local x';
     print(y) # local
     print(x); # local

# print(x)
loc();

# print(y); Error, 'y' is not defined
# is function re-assign variable 'x'? no, it create new variable with name x, but not relate to "global x"
# x hasn't been overwritten within `loc()` function
# means variable x which within loc() function has been created as new variable
# 
# SOO, How to access global variable
# by explicitly define variable x with "global" 
print(x)


# global x; make this function loc() not pure function
# and oure function is function has not side-effect, doesn't affect on outside env

# so don't over use "global", try to avoid it

print(dir(builtins))
# will ou
# dir give us attributes of a given object


# if we name some function as name of built-ins error in python? not error

def min(iterable):
     print(iterable)
print(min([1,2,3,4,5,5,-1]))

# so built-ins min function won't work? Yeah
# because python see first Local Scope, Enclosing, Global, then lastly Builtins

# but there is one way to use builtin function
# 
print(builtins.min([1,2,3,4,-1]))


# Enclosing
# when you has nested function, or nested block within function, or another block


def outer():
     x = "outer x";
     def inner():
          # nonlocal x;
          x = "inner x";

          print(x); # [L]EGB
          # if we commented x = "inner x", will use L[E]GB
          # this means -> it will look up it in outer block

          # if i want re-assign "x" variable, not create new brand?
          # i should using global?
          # not, it will change the global variable which its name "x"
          
          # We should use "nonlocal" to access enclosing variables
  
     inner();
     print(x); # [L]EGB

outer();

#nonlocal is used often unlike global
# because it is useful to use for change state of closure, and decorators

# Wrap
# python will look up if he finds in Local -> Enclosing -> Global if doesn't found, will see in built=ins, if doesn't found as well
# it will throw an error