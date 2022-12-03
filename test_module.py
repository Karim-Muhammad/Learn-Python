# ---------------------------------------------------------------------------- #
#                           ------------------------                           #
# ---------------------------------------------------------------------------- #

# import module
# print(module.find_index("history",["math", "science", "history"]));

# help(module.find_index)
# ---------------------------------------------------------------------------- #
#                                --------------                                #
# ---------------------------------------------------------------------------- #

# if we habe hunderds codes which we use module many time
# is there another way to use short way? Yeah
# we can use `as` to rename our module

# import module as mo;
# print(mo.find_index(1, [2,2,3,1,1]));
# ---------------------------------------------------------------------------- #
#                               ----------------                               #
# ---------------------------------------------------------------------------- #

# if we don't want any module name then dot, we want just name of function
# we can use from <module> import <function>

# from module import find_index;
# print(find_index(target=[11,1,2,35,5], to_search=2));
# ---------------------------------------------------------------------------- #
#                                ---------------                               #
# ---------------------------------------------------------------------------- #

# if we want import many things not only function "find_index"?
# we use from <module> import <function | variable>, <function | variable>

# from module import find_index as findex, test;

# we can still rename our imported things by "as"

# ---------------------------------------------------------------------------- #
#                                  -----------                                 #
# ---------------------------------------------------------------------------- #
# if we want import every thing by "from" statment
# we can use * to import everything

from module import *
print(test);

# But it doesn't required at all
# for many reasone,
# first, we don't know any function came from module or any function doesn't came from module
# when you encounter bug for example, you have to track your function, variables where they came

# How to handle paths for modules
# how system know where is module?
# it checks multiple locations, and these locations
# within list of sys.path, import sys first
# 
import sys;
print(sys.path) 
# These directories on machine which Python look at to modules
# and it check in these in order, if found first, so stop, if didn't
# go next location, so etc...

# first location is our current dir, which script is running
# second is location of directories which in Python Environment Variable
# Third is location of standard of library
# so that we can import libraries of python
# Fourth locations of Third-party packages
# 
# 
# many ways to add our paths to import module 8:00 

import math

print(math.sin(math.radians(90)))

# how python could import math?
# because its location is stored within list of sys.path


# 
import datetime
import calendar
# have a similarities but there are different
print(datetime.date.today())
# print(int(datetime.date.year))
# print(calendar.isleap(datetime.date.year))

# Another Module is important is os
import os
print(os.getcwd); # to get "current working directory(cwd)"
# allow us to create file, delete file, scan files, ...


# if you want know where is location of file located, use __file__

print(datetime.__file__)
# print(math.__name__, math.__file__)
print(os.__file__)

# Dunder File means underscores

days = datetime.MINYEAR;
print(days)

# NOTE There are things you can use it after import , there are not
# all things which declared with underscore first, is considered as private variable or function
# and all things which not declared with underscore first, you can use it  

# import module
# import module as _module;

# print(_module._private_var)
# print(_module.__accessable)

# ---------------------------------------------------------------------------- #
#                                    ------                                    #
# ---------------------------------------------------------------------------- #

from module import *;
print(public)
print(_private_var)
print(__accessable)