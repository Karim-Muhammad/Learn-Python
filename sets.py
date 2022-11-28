# 2: 50: 00
# Sets {}
print({1,2,3,4,5,5,5}) # set
print({"name": "karim"}) # dict
print({"name": "karim", "name": "muhammad"}) # just take last one (similar to way of set) ( both are use {} )
###############################
print("\n")
programming_languages1 = ["ruby", "python", 'javascript'];
programming_languages2 = ["ruby", "SQL", 'JAVA', "C++", "python"];

# >>> [1,2] + [2,3] # [1,2,2,3]
# in Javascript it will convert both to string, then concate them as a one string, unlike python
total = set(programming_languages1 + programming_languages2)

print(total) # remove duplicate
# print(total[1]) cannot access sets
# and this might be make sense, because this sets which we see now, is not final result, final one, will do some process to remove duplication
print(list(total)) # from {} to []
##################################

# set object is not subscriptable which means, you cannot get 0th element
# set is an unordered collection data type that's iterable, mutable, no duplicate
# sets is best data strcture to search, and look at specific element really quickly

# array_within_set = {[1,2,3]} # Error, cannot insert unhashable element(iterable) to set, just individual element
# print(array_within_set);
# array_set1 = set([1,2,3, [1,2]]); # Error
array_set2 = set([1,2,3]);
print(array_set2);


def unique(_list: list) -> list:
     '''
     remove duplicate items in a list
     >>> unique([1,2,2,2,3,4])
     [1,2,3,4]
     '''
     return list(set(_list));
# another way
uniq = lambda _list: list(set(_list));
print( unique([1,5,5,5,6]) );
print( uniq([1,5,5,5,6,7,7,7]) );
