# ---------------------------------------------------------------------------- #
#                                     List                                     #
# ---------------------------------------------------------------------------- #
list1 = [9,2,1,5,3,5,9,1,2,10,0];
s_list1 = sorted(list1); # Ascending Order

print(list1, "Sorted-> ", s_list1);

# Sort Original

# list1.sort(); # it returns None!!
# print(list1)

# Descending Order
desc_list = sorted(list1, reverse=True);
print(desc_list);

# Using sorted() function than .sort() method Recommended
# because there are data structures haven't mainly .sort method own like "tuple"


# ---------------------------------------------------------------------------- #
#                                     Tuple                                    #
# ---------------------------------------------------------------------------- #

# if we sorted Tuple? 

tuple1 = (1,2,3,4,5,6,7);
# tuple1.sort() // haven't
s_tuple1 = sorted(tuple1)
print(s_tuple1); # return sorted list! not sorted tuple!!!


# ---------------------------------------------------------------------------- #
#                                  Dictionary                                  #
# ---------------------------------------------------------------------------- #


# if we sorted Dict?
dict1 = {"name":"karim", "age": 20,"job": "student"};
s_dict1 = sorted(dict1); # it sort keys only!!
s_dict1 = sorted(dict1.items()); # solution!

print(s_dict1);

# ---------------------------------------------------------------------------- #
#                                      Set                                     #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                              By Custom Criteria                              #
# ---------------------------------------------------------------------------- #

# custom
custom_list = [-5,-1,-7, 1,6,4];
custom_sorted = sorted(custom_list, key=abs) # compare based on their absolute values
print(custom_sorted);


class Employee():
     def __init__(self, name, job, salary):
          self.name = name;
          self.job = job;
          self.salary = salary;
     
     def __repr__(self) -> str:
          return f"[Name]: {self.name}, [Job]: {self.job}, [Salary]: {self.salary}\n"

e1 = Employee("Karim", "Engineer", 8000);
e2 = Employee("Muhammad", "SoftWare Engineer", 10000);
e3 = Employee("Ahmed", "Doctor", 19000);

employees = [e1, e2, e3];
# sorted_emp1 = sorted(employees); Error, unorderable type 'Employee() < Employee()'
sorted_emp2 = sorted(employees, key=lambda e:e.name);
# sort based on name of object
# print(sorted_emp1);
print(sorted_emp2);

# key takes a function which accept one parameter which it is each element of array

# import inspect;
# import builtins;
# print()

from operator import attrgetter
sorted_emp3 = sorted(employees, key=attrgetter("name"))
print(sorted_emp3);