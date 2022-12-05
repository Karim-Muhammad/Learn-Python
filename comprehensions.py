# list comprehension

nums = [1,2,3,4,5,6,7,8,9,10];

# 1# Way
# ex_list = [];

# for num in nums:
#      ex_list.append(num)

# print(ex_list);

# # 2#
# ex_list=[];
# ex_list=[num for num in nums];

# print(ex_list);


################################# 

# 1# Way

# ex_list = [];

# for num in nums:
#      ex_list.append(num * num)
# print(ex_list);

# 2# Way
# ex_list=[];
# ex_list=[num*num for num in nums];

# print(ex_list)

# 3# Way (using map()) (Declarative Way)
def func(el):
     return el*el;

# 1-> Works (using lambdas)
ex_list = map(lambda el: el*el, nums);

# 2-> Works As Well (using reference of function)
# ex_list = map(func, nums);

print(ex_list);
print(list(ex_list));

# Wrong Order
# def extract(*args, m) -> None:

# Correct
def extract(m, *args) -> None:
     print(m, args);

extract([1,2,3], [4,4,4,5]);
print("--------")
extract(*[1,2,3], *[4,4,4,5]);

# Using map() no longer needed because we have list comprehension which is more readable

######################################################
# Dictionary Comprehension
dictionary1 = {
     "name":"karim",
     "job":"student",
}

copy_dict = {key:dictionary1[key] for key in dictionary1}

print(copy_dict)


# Complex Example
# I want "n" for each "n" in "nums" if "n" is even

test_numbers = [1,2,3,4,5,6,7,8,9,10,11];
copied_list = [];

# Imperative Way
for num in test_numbers:
     if num % 2 == 0:
          copied_list.append(num);

print(copied_list)


copied_list2 = [[n, None][(n%2!=0)] for n in test_numbers];
print(copied_list2);

# Correct Precise Way
copied_list3 = [n for n in nums if n%2==0]
# append "n" for each "n" in "nums" if that "n" his mod% equal to zero


copied_list4 = filter(lambda el: el%2==0, test_numbers);
print(copied_list4);
print(list(copied_list4));

# I Have a Question, Way "map()" accept (*iterable), and "filter()" accept just (iterable) [without *] ???


# I want a (letter, number) pair for each letter in 'abcd' and each number in '0123'
# q3 refer to question number 3
q3_list = [];
# count = 0;

for lett in "abcd":
     for num in range(4):
          q3_list.append((lett, num ))

print(q3_list);


# List Comprehension
q3_list2 = [(lett, num) for lett in "abcd" for num in range(4)]
print(q3_list2)


# zip()

names = ["bruce", 'peter', "John", "Max", "speed"];
heros = ["Fighter", "SpiderMan", "unknown", "Knight", "Flash"];
# copied_dict1 = [];
copied_dict1 = {};

# What is function zip(iter1, iter2)? Try out
print(zip(names, heros))
print(list(zip(names, heros)))


for name, hero in zip(names, heros):
     # copied_dict1.append({name:hero}); for list
     
     # for dictionary
     copied_dict1[name] = hero;

print(copied_dict1);

copied_dict2 = {name: hero for name, hero in zip(names, heros)};
print(copied_dict2)

# if not equal to peter
copied_dict3 = {name: hero for name, hero in zip(names, heros) if name != "peter"}
print(copied_dict3)
# Exception from our dict name "peter"


# Set
duplicate_nums = [11,2,2,2,3,4,5,5,5,6,7,7,7,8,9,9,10];
set1 = set();
for num in duplicate_nums:
     set1.add(num);

print(set1);

set2 = set([n for n in duplicate_nums if n%2==0]);

# Works as well
# set3 = {n for n in duplicate_nums if n%2==0}
print(set2)


# Generator Expressions
# I want to yield "n*n" for each "n" in "nums"
# 
nums_again = [1,2,3,4,5,6,7,7,8,9,10];

def generate_n(list):
     for n in list:
          yield n*n;

my_gen_element = generate_n(nums_again);
for n in my_gen_element:
     print(n);


# Generator Function use yield in each loop, that's for loop
# doesn't work at a one time like previous loop
# it does each iterate, and each calling function

# like this small example
l = ["k", 'm', "u", "r", "z"];
def gen_sm(list):
     for el in list:
          yield el;

print(gen_sm(l));
print(gen_sm(l));
print(gen_sm(l));
print(gen_sm(l));
print(gen_sm(l));

for e in gen_sm(l):
     print(e);


# I want yield (Generate) each calling function new element
# is used for example in "read more" or "show more" in websites