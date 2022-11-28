# List []

fruits = ["apple", "banana", "orange", "blueberry"];

# accept only one object (string)
print(fruits)

# ---------------------------------------------------------------------------- #
#                                  Equivalent                                  #
# ---------------------------------------------------------------------------- #
# list.append(x) === list.insert(len(list), x) === list[len(list):] = [x]
################################################################################
fruits.append("strawbarry") # Equivalent to fruits[len(fruits):] = ["strawbarry"] === a.insert(len(a), x).
fruits[len(fruits):] = ["kiwi"]; # grouped together
fruits[len(fruits):] = "kiwi"; # each letter separtaly
print(fruits)

# accept iterable (list, tuple)
fruits.extend(["fruit1", "fruit2"])
print(fruits)

# like .push() in Javascript

# insert
fruits.insert(0, "First")
fruits.insert(1, "Second")
print(fruits);

# this method like .splice(start_position, 0 || many, new_element) in Javascript
# if you typed 0 so you won't remove this position, if you typed many, so you remove
# insert in begining like .unshift() in JS

# removes
fruits.remove("Second");
print(fruits)

fruits.insert(2, "Third");
fruits.pop(); # by default, removes last item
print(fruits)

fruits.pop(0); # removes first item, first index(0)
print(fruits)

# index
print(fruits.index("orange")) # 3
print(fruits[3]) # orange


# QUESTION
# How to GET last item in LIST in Python???
# Use Negative index, yahooo
print(fruits[-1]);

# Javascript doesn't support this, but it HAS a Method to do exactly the same thing
# It is `.at()` fruits.at(-1);


# step
# by default it is 1, foward
print(fruits[0: :2]) # step by 2,

# trick
# when i make steb by negative value, starts with back(backward)
print(fruits[::-1]) # reverse array
# fruits.reverse();
# print(fruits)

# lists in python has a many tricks to do

# 2 : 21: 10

print(fruits[::-2]) # same :: 2 but that's from "backward"

# ---------------------------------------------------------------------------- #
#                                     Index                                    #
# ---------------------------------------------------------------------------- #
print(fruits.index("kiwi"))
# print(fruits.find(["kiwi"])) # find method for strings only