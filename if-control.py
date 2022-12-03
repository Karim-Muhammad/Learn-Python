# There is difference between
# == and is (object identity)
o1={"name": "karim"}
o2={"name": "karim"}
print(o1 == o2)
print(o1 is o2) # because both has a different location in memory

object1 = {"name": "karim"};
object2 = object1;

print(id(object1), id(object2))
print(object1 == object2)
print(object1 is object2) # True (has a same location in memory)


# Python doesn't has a switch case

if not o1["name"]:
     print("has no name")

logged_in = False;
if not logged_in:
     print("Please Log in")
else:
     print("Welcome!")


     # 12:00