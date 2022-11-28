# There is two types of numbers in Python
# Integers and Float
# Integers is Whole numbers without floating-point
# Float is Whole Decimal numbers (integers and floating)
import math;
# Another Way
# from math import <methods>
int_num = 7;
float_num = 7.6;

print(type(int_num)) # int
print(type(float_num)) # float

# Arithmetic Operations
print("---Arithmetic Operations---")
print( 30 + 30 ) # 60
print( 15 - 30 ) # -15
print( 50 / 30 ) # (divide)
print( 50 // 30 ) # (floor division)
print( 50 % 30 ) # (mod)
print( 50 * 2 ) # multiplication
print( 50 ** 2 ) # exponential

# To Force precedence somehow use parentheses ()
print( 3+3 * 3) # first * then + so (-> 12)
print( (3+3) * 3) # first () then * so (-> 18)

# Built-in functions
print("---Built-in functions---")
print(abs(-30))
# 30 (absolute convert negative to positive)
# ---------------------------------------------------
print(round(3.25)) # 3
print(round(3.55)) # 4
# round do "round" for number if below .5 floor it else ceil it

# 
print(round(3.25, 1)) # 3.2
print(round(3.26, 1)) # 3.3 (here i wanna round first digit after decimal)
print(round(3.55, 2)) # 3.55 (here i wanna round second digit)

# Math Library
print("---Math Library---")
# trunc
print(math.trunc(100.1919));
# print(math.cbrt(3))
print(math.pi)
print(math.nan) # like NaN in Javascript
print(math.nan == math.nan) # false
print(math.prod([1,2,3,4], start=1)); # >>> 1 * 2 * 3 * 4 = 24
print(math.fsum([1,2,3,4])) # 1 + 2 + 3 + 4 = 10
print(math.factorial(5)) # 120
print(math.floor(2.6)) # 2
print(math.ceil(2.3)) # 3
# ---------------------------------------------------
# Comparison
print("---Comparison---")
num1 = 10;
num2 = 20;

print(num1 > num2) # False
print(num1 <= num2) # True
print(num1 == num2) # False

# data number in string form! like that >>> "10"
# NOTE this might happen when you read file for example, or scrap from web, read CSV(EXCEL)
lucky_number = "77";

print(int(lucky_number))
# print(type(input("Enter Your Lucky Number: "))) # str
# print(type(int(input("Enter Your Lucky Number: ")))) # int

# Built-in methods
