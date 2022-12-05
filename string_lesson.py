# string is immutable (unchangable)
name = "Karim";
# name[0] = "M"; # Error, like a constant

print(name)

# ---------------------------------------------------------------------------- #
#                                  to know length                              #
# ---------------------------------------------------------------------------- #

print(len(name))
print(("Py" "thon" == "Python"));
print(str(b'ello'))
print(name.capitalize())
print(name.casefold(), "Muhammad".casefold(), "Muhammad".lower())
# casefold === lowercase, it help us in comparison
# there is difference between them of course
# in docs


# ---------------------------------------------------------------------------- #
#                                    center                                    #
# ---------------------------------------------------------------------------- #
print("Karim".center(11, "-")) # padding 5(length of name) - 11 (width) = 6 (dashes)

# ---------------------------------------------------------------------------- #
#                                     count                                    #
# ---------------------------------------------------------------------------- #
print("Muhammad".count("m", 2)) # count m , begins count in index 2 to end
print("Muhammad".count("a", 4)) # count a , begins count in index 3 to end


# ---------------------------------------------------------------------------- #
#                                    endwith                                   #
# ---------------------------------------------------------------------------- #
# print("Muhammad".endswith(["w","ad"]))

# ---------------------------------------------------------------------------- #
#                                  expandTabs                                  #
# ---------------------------------------------------------------------------- #
print("Kura".expandtabs(6))
print("K\tu\tr\ta".expandtabs(2))
print("K\tu\tr\ta".expandtabs(6))

# ---------------------------------------------------------------------------- #
#                                      in                                      #
# ---------------------------------------------------------------------------- #
print("Py" in "Python")
print("Python".find("Py")) # return index of first letter

# Note The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator

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

# ---------------------------------------------------------------------------- #
#                                    Access                                    #
# ---------------------------------------------------------------------------- #
name = "Karim Muhammad";
print(name[0]) # "K"
print(name[0:5]) # 0 inclusive and 5 exclusive ===> [0, 5)
print(name[0:5:2]) # 2 refer to "step jump" ==> "Krm"

 

# ---------------------------------------------------------------------------- #
#                                 Documentation                                #
# ---------------------------------------------------------------------------- #
print(dir(str)) # give us all fields, methods of types of "string" (dir() function)
print("10101".isdecimal()) # if all letters is numeric will give us True
print("10.101".isdecimal()) # False! (because it is floating, not decimal)
print("10101k".isnumeric()) # all letters is numeric (Integers as well)
print("10.101".isnumeric()) # False

# If We Want Get Help and knows what is methods doing actually so USE "help()" function
print(help(str)) # to get all docs with explaining
print(help(str.lower)) # Get Information what .lower() methods do!

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #o