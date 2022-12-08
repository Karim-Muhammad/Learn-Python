class A(object):
     def dothis(self):
          print("Do This in Class A");

class B(A):
     pass;

class C(object):
     def dothis(self):
          print("Do This in Class C");

class D(B, C):
     # order or parameters is important!
     # becuase determine instance D() inherit from who first
     pass;

# method resolution order that's why object Take from A not C

# to know this order use .mro()


d1 = D();
d1.dothis();

print(D.mro())
# first from D then B, A, C in last in <class 'object'>


