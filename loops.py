# 3: 10:30

# for i=0; i<=10; i++:
#      print(i);

# list
list_of_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Kiwi" ];
copy_fruits = [];
# just write key, not value
for i in list_of_fruits:
     print(i);
# another way
print("#"*30);
for i in range(len(list_of_fruits)):
     print(i, list_of_fruits[i]);
     copy_fruits.append(list_of_fruits[i]);

print(copy_fruits);

# this for is used with any iterable data type, like (list, tuple, set, dict, string)
# iterating over a sequence is called "traversal"

# another way: enumerate()
for k,v in enumerate(list_of_fruits):
     print(f"{k} -> {v}");

# enumerate take a iterable data type like list, tuple, set, which keys is zeroth index
# in for .. in you cannot use key, just value(element)
# so that, enumerate help us to convert this collection to enumerate object, add counter as the key

print(list(enumerate(list_of_fruits)))
print(list(enumerate({"name": 'Karim', "age": 20})));
print(dict([("name", "karim"), ("age", 20)]));

# dict is list of tuples ("name", "karim"), ('age', 20) (these are tuples)
# [(), ()]

################################
print("#"*10 + " List "+ "#"*10)
# List
# iterate on elements of list

for k in ["name", "karim"]:
     print(k); # v is kiwi ?!!!

################################
print("#"*10 + " List of lists "+ "#"*10)
# List of lists
# iterate on elements of list

for k, v in [["name", "age"], ["karim", 20]]:
     print(k,v); # v is kiwi ?!!!

################################
print("#"*10 + " Tuple "+ "#"*10)
# Tuple
# like list

for k in ("name", "karim"):
     print(k); # name \n karim

################################
print("#"*10 + " List of tuples "+ "#"*10)
# List of Tuples
# by using "unpacking" way
for k, v in [("name", "karim"), ("age", 20)]:
     print(k, v); # name karim \n age 20
# Why Tuple? to avoid user updating keys (list "name")

################################
print("#"*10 + " List of tuples "+ "#"*10)
# List of Tuples
# iterate on key, value for elements of list
# without "unpacking"
for k in [("name", "karim"), ("age", 20)]:
     print(k); # Get a tuple !!
     print(k[0], k[1]); # Get first, second element in Tuple

################################
print("#"*10 + " Dictionary "+ "#"*10)
# Dictionary
# iterate on keys only (in dictionary)

for k in {"name":"karim"}:
     print(k); # name only

################################

# Unpacking
# 1
name, age = "karim", 20;
print(name, age);

# 2
# unpacking tuple means assigning individual elements of tuple to multiple variables
index, fruit = (0, "apple");
print(index, fruit);

# 3
list1, list2 = ["one", 'two'];
print(list1, list2);

# ValueError: not enough values to unpack (expected 2, got 1)
# key, value = {"name": "karim"};
# print(key, value);

# range()
# range is return a sequence of numbers, begins with 0 by default and increasing by one by default and stop before specified number
print(range(10))
print(list(range(10)))

for x in range(10):
     print(x)


# While Loop (not common much)
# Why While loop is dangerous? because of Infinite Loop
# While loop doesn't repeat blocks of codes specified number, no it depend on condition
# if condition is true, it will execute block, if not true, it exit from loop
counter = 0;
while counter < 10:
     print("While Loop : ", counter);
     counter+=1;
     # counter ++; Wrong in python

while int(input("Enter Positive number only")) > 0:
     print("continue");

# otherwise(enter negative) will break loop


# 3: 46: 05 (Practice)

numbers = [1,2,3,4,5,6,7];
dbl_numbers = [];
for number in numbers:
     dbl_numbers.append(number * 2);

print(dbl_numbers)

# Count Letters

#def count_letters(string: str) -> int:
     # map = {};
     # for word in string:
     #      # map[word] = 1 if type(map[word]) == None else map[word];
     #      map[word] = {True: 1, False: map[word]}[type(map[word]) == "None"];
     # return map;

#print(count_letters("Karimm"));

# Count Words
def count_words(sentence: str)-> int:
     arr = sentence.split(" ");
     print(arr)
     return len(arr);
def count_words_by_manual(sentence: str)-> int:
     counter = 0;
     for letter in sentence:
          counter += 1 if letter == " " else 0;
     return counter + 1;

print(count_words("Hi, My name is Karim, Bye"));
print(count_words_by_manual("Hi, My name is Karim, Bye"));

# 4: 07: 40
