# Learn From Docs

# classic print
print("Hello People :>");

# Don't interpret special character
# test
print("C\karim\name");
# \n is considered as special character "new line";

# to stop interpreter translate these special use "r" before quotes
print(r"C\karim\name");

# something is similar, and it is "f" which help us format our string
name = "Karim Muhammad";
print(f"Hello, {name}");

# print Multiple lines
print("""\
Who am I?\
My Name is Karim Muhammad\
my age is 20 years old
I'm a  Muslim
""")

# in javascript you cannot using * (multiplication) with strings, it return NaN
# but in Python which is more smart :>
# it repeat string numbers of times

print(3 * "hey " + "Hello");


# to store multiple lines within variable, without Triple Quotation, or Concatenation
text = (
     'Put several strings within parentheses \n'
     'It is very useful feature to use it \n'
     "So Fantasitic!"
)

print(text);

# Watch out!
# you cannot do this (3 * "hi" "concated") (cannot use it with expressions)
# You can do this ("hi" "concated") only

# you cannot use this with "variables" as well like this
# 
prefix = "hola";
# print(prefix "karim"); #invalid syntax

word = "Python";
print(word[0], word[5]); # count from begin
print(word[-6], word[-1]); # count from last
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2]) # count from begin (0) to 2 excluded
print(word[2:]); # begins with index 2 to "end"
print(word[-2:]) # begins with index 4 (before last) to the end (last) (-1)

# to concate separated indices with together
#  word[:i] + word[i:] (general pattern)
#  word[:2] + word[2:] [use this pattern]