# Dictionary {}

# dictionary is a map in other programming languages like c++, java or called associative memories, associative arrays
# dictionary is indexed by "key" not by "number" like array (list here)
# and the key can be any immutable type like "strings"(common) or number and Tuples can be as key!
# so why not list?
# becuase list hold data from different data types, string, number, list, tuple, dict
# while Tuples hold Immutable data which has one only data type, only string Or only Number only Tuples NOT only List
# Tuples like string and number is immutable, you cannot change any element within tuple, unlike list
# so that, if Tuples hold data mutable directly or not, it cannot used as a key, because it now is called "list" not "Tuple"


# like an object literal in javascript
# key value pair, key is unique identifier for some item of data
# and the value, is either data that's is idenified or a pointer to the location of that data

tel = {
     "Karim": 6077,
     "Muhammad": 4044
}
print(tel)
tel["New Value"]= "10001";
print(tel)
del tel["New Value"]
print(tel)
tel["last_item"] = "9087"

print("Karim" in tel) # True
print("Marim" in tel) # False
print("Marim" not in tel) # True

print(list(tel))
# return keys in dictionary as list
# like Object.keys() in Javascript
# <dictionary_name>.values() equivalent to Object.values() in Javascript
# <dictionary_name>.items equivalent to Object.entires() in Javascript

# if you have associtive array and you want convert it to dict do following:
# dict function accept (array, indiviadual parameters with default)
# 1
way1 = dict([("Karim", 797), ("Muhammad", 777), ("Zeyad", 987)])
# 2
way2 = dict(sape=4139, guido=4127, jack=4098)

print(way1, way2)

# advanced way
way3 = {x: x**2 for x in (2,4,6,8,10)}
print(way3)
print(way1.items()) # convert dictionary from simpler structure to associtive array, to get key, value
print(way1); # simpler structure

# Iteration
for key, value in way1.items():
     print(f"{key}: {value} in dict way1");
for x in [1,2,3]:
     print(x);
for x in (1,2,3):
     print(x);

# to iteration on dictionary, now allowed use "value", only "key"
# like using for x in list(way1) then iterate
# but if you want get values as well, you can use name of dict with key `dict[key]`
for x in way1:
     # print(x, v); Error
     print(x, way1[x]);

def big_greet(person: dict)-> None:
     person = {
          "name": "karim",
          "age":20,
     }
     print(f"Hey! {person['name']}" f"Your age is {person['age']}")
     # Watch out, Type key of dict opposite of double quoation, if string single, so type it double

####################
def introducer(person: dict) -> None:
     print(f"Hi {person['name']}, your age is {person['age']}, Good luck!")

introducer(person={"name": "karim", "age": 20});

####################
person2 = {
     "salary": 10000,
     "bill": 200,
     # "new_worth": salary - bill # you cannot do like this, because it hasn't defined yet!
     # "new_worth": lambda sa, bi: sa - bi,
     "new_worth": lambda: person2["salary"] - person2["bill"], #sa - bi
     # def calc():
     #      return person["salary"] - person["bill"]; 
}

print(person2["new_worth"]());

# 2: 43::15
# IMPORTANT note:
# list is ordered, dictionary in python used to un-ordered but in version 3.8+ it became ordered
# and this unlike most of programming langauges, map(dictionary) is un-ordered

# 𝗙𝗼𝗿 𝘆𝗲𝗮𝗿𝘀, Python dictionaries were unordered data structures. Python developers were used to this fact, and they relied on lists or other sequences when they needed to keep their data in order. With time, developers found a need for a new type of dictionary, one that would keep its items ordered.Back in 2008, PEP 372 introduced the idea of adding a new dictionary class to collections. 𝙄𝙩𝙨 𝙢𝙖𝙞𝙣 𝙜𝙤𝙖𝙡 𝙬𝙖𝙨 𝙩𝙤 𝙧𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙩𝙝𝙚 𝙤𝙧𝙙𝙚𝙧 𝙤𝙛 𝙞𝙩𝙚𝙢𝙨 𝙖𝙨 𝙙𝙚𝙛𝙞𝙣𝙚𝙙 𝙗𝙮 𝙩𝙝𝙚 𝙤𝙧𝙙𝙚𝙧 𝙞𝙣 𝙬𝙝𝙞𝙘𝙝 𝙠𝙚𝙮𝙨 𝙬𝙚𝙧𝙚 𝙞𝙣𝙨𝙚𝙧𝙩𝙚𝙙. That was the origin of OrderedDict.(https://realpython.com/python-ordereddict/)OrderedDict was added to the standard library in Python 3.1. Its API is essentially the same as dict. However, 𝙊𝙧𝙙𝙚𝙧𝙚𝙙𝘿𝙞𝙘𝙩 𝙞𝙩𝙚𝙧𝙖𝙩𝙚𝙨 𝙤𝙫𝙚𝙧 𝙠𝙚𝙮𝙨 𝙖𝙣𝙙 𝙫𝙖𝙡𝙪𝙚𝙨 𝙞𝙣 𝙩𝙝𝙚 𝙨𝙖𝙢𝙚 𝙤𝙧𝙙𝙚𝙧 𝙩𝙝𝙖𝙩 𝙩𝙝𝙚 𝙠𝙚𝙮𝙨 𝙬𝙚𝙧𝙚 𝙞𝙣𝙨𝙚𝙧𝙩𝙚𝙙. If a new entry overwrites an existing entry, then the order of items is left unchanged. If an entry is deleted and reinserted, then it will be moved to the end of the dictionary.

names = {"karim":100, "muhammad":200, "zeyad":300, "murad":400, "ahmed":500}
print(reversed(names));
print(list(reversed(names)));
print(list(reversed(names.keys())));
print(list(reversed(names.values())));
print(list(reversed(names.items())));

# before this version, you had to take dict out of dictionary and put in array to order it, or search, sort, <algorithm>


# How to Merge Multiple Dict
# mergedDict = {**dict1, **dict2};