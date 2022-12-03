# List (unordered collection)
# We will spend more time with list because it has more functionality than others
# ---------------------------------------------------------------------------- #
#                                     List[]                                   #
# ---------------------------------------------------------------------------- #
import math;
print("----------ADDING-------------")

courses = ["JS", "HTML/CSS", "Python", "Nodejs", "Reactjs"];
print(courses)
courses.append("TailwindCSS")
print(courses)
courses.insert(0, "Bootstrap"); # Shifting
print(courses)

# Extends is used when you have a multiple values you want append them into array
courses.extend(["JQuery", "Material UI"]);
print(courses)

cours1 = ["HTML", "CSS"];
cours2 = ["Javascript", "JQuery"];
cours3 = [4,1,2,6,3,2];
print(cours1 + cours2); # Concate arrays

print("-----------REMOVE-------------")

# Remove
print(cours1.remove("HTML"));
print(cours1)
print(cours2.pop(0)) # by default it remove last element -1
# Pop uses index to remove unlike "remove()" which uses value
print(cours2)

print("-----------SORT vs Reverse--------------")

# Reverse
courses.reverse()
print(courses)
courses.sort()
print(courses)

courses.append("Zbrush");
courses.append("Redux");
courses.append("SASS");

courses.sort(); # Alphabetically Order
print(courses)

cours3.sort();
print(cours3); # Ascending Order

# if you want descending? Do Sorted first then Reverse |Or| Use only Sort methods with param reverse=True
cours3.sort(reverse=True);
print(cours3);
print("-------------------------")

# if you notice all methods alter our original array!
# and we don't want change or alter our array
# so we have to use functions! not methods  
cours3.reverse();
print("-----------altered version------------")
print(sorted(cours3, reverse=False));
print("-----------Original-----------")
print(cours3);
print("------------reverse fn----------")
print(reversed(cours3))
print(list(reversed(cours3)))
print("------------Original----------")
print(cours3); # didn't changed

# Max, Min, Sum, Prod, Factorial
print(max(cours3))
print(min(cours3))
print(sum(cours3)) # summation of all elements
print(math.prod(cours3)) # multiplication of all elements

print(cours1)
print(cours1.index("CSS"));
# print(cours1.index("HTML/CSS"));

# If we want check if element in our list, dict, set we use "in" operator
print("HTML" in cours1);

# For Loop

for_courses = courses[:]; # create new list
# We not use parenthese at all! (Watch out!)
for cours in for_courses:
     print(cours);

# to access the index as well, we habve to use enumerate function
for id, cours in enumerate(for_courses, start=0):
     # enumerate return for each element tuple has (index, value)
     # you can check that when you use one variable as left-hand
     # Third arg (start=) for start index with how if you typed "one" so it will
     # make id start with 1 not 0
     print(id, cours)

# 1#
courses_str = str.join(", ", courses);
print(str.join(", ",courses))
print(courses_str.split(", ")) # back our string to list as it was
# 2#
print("||".join(courses));
# "self" like "this" in JS

# NOTE this example
list1 = [1,2,3];
list2 = list1
list3 = list1[:]

print(list1, list2, list3)

list1[0] = 10;
print(list1, list2, list3);

# NOTE what is you note?
# when you change "list1" that is reflect on another variable "list2" but not affected on "list3"
# because list2 refer to location of list1 in memory
# but "list3" not refer to same location, but it create new list
# 


# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                     Tuple()                                  #
# ---------------------------------------------------------------------------- #
# The only difference between it and List, Tuple immutable (like primitive) you cannot modify
# because tuple immutable (cannot changeable) for that, no nearly many methods like list for tuple
# because most of methods which we cover in list, it was mutate our list
# and Tuple cannot mutated, so that have not same methods
tuple = ("Karim", "Muhammad", "Zeyad", "Murad");
# Accessing
print(tuple[:]);  
print(tuple[-1]);  
# Looping
for t in tuple: print(t)

# cannot change
# tuple[0] = "Mariam"; Error

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                          Set{} (unordered collection)                        #
# ---------------------------------------------------------------------------- #
# Set unordered structure, and non-duplicate
set1 = {"wow", "WOW", "wow", "memes", 1,1,2};
set2 = {"wow", "memo", "hi", "hey", "bye"};
print(set1)
#NOTE printed output not ordered as we added them! so that we call him (unordered) like dict
# Each execution change his order!
# Tuple doesn't care about his order at all
# because we use it for just remove duplication, and check elements
# Membership test means check if value is part of set or not
# Tuple do that efficiently than tuple, list

print("wow" in set1 ); # True
# You can do this with tuple, list, BUT Set is more optimized with this

# Another thing is useful for using Set it is
# check if element is share with other sets or not

# which found in set2 and not found in set1
print(set2 - set1)

# which found in set1 and not found in set2
print(set1 - set2)
# same
print(set1.difference(set2));

# Do intersection (check common elements which found in both sets)
print(set1.intersection(set2))

# Do union
print(set1.union(set2));

# GOOD to know Sets Very important in Probability and Statists as we saw

# To Create Set you use only
se1 = set()
# NOT
# se2 = {} Wrong, this refer to dict not set
# dictionary = {} correct

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                             Dictionary{} (ordered)                           #
# ---------------------------------------------------------------------------- #
# Hashmaps || Associative array || map || object

# Dictionary contains key, value pair
# key can be any immutable datatype (like primitive, tuple)
# value can be anything

dict = {1:"id","name": "karim", "age": 21, "courses": ["math", "DS", "Algo"]}
# dict.items[ (1, "id"), ("name", "karim"), ("age", 21), ("courses", ["math", "DS", "Algo"]) ]
print(dict)

# Accessing
print(dict["name"])
# using integers as key
print(dict[1])

# print(dict["phone"]) # KeyError accessing with key not found, will throw an error
# if you don't want throw an error if you typed wrong key, so use .GET() method

print(dict.get("name"))
print(dict.get("phone")) # None

# if i want specify return value if key not found, we pass second arg with custom msg
print(dict.get("phone", "not found"))

# Setting (Updating)
# dict["age"]= 22;

# if you wanted many things at a time
dict.update({"age": 22, "phone":"333-33-33"});
# .update() method accept dictionary
print(dict)

# if i wanted check first before update or adding new field
dict["age"] = 22 if dict.get("age") == None else dict["age"]

# Deleting with `del` operator
# del dict["age"]

# but if we want value of deleted key, we should use .pop() method
removed_value = dict.pop("age");

for info, v in dict.items():
     print(info, v)
# ########################################
for info in dict.keys():
     print(info, dict[info])

# ---------------------------------------------------------------------------- #
#                                      END                                     #
# ---------------------------------------------------------------------------- #

