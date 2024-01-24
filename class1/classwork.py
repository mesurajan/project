"""wap in python to input any two numbers ,namely "num1"and "num2"and find :
--->FIRST NUMBER being num1 and second number being num2
---->sum of two numbers
---->subtraction of two number
---->Division  of two number
---->multiplicatiopn of two number
----> POWER of two number
----> floor division
#Bonus tasks 
--->find the greatest between two if you know conditions in python 
print("f the sum of {a}and {b} is {sum_ab}")
"""
import math

num1 = input("Enter the  first  number :\n")
num2 = input("enetr the second number:\n")
sum_ab = int(num1) + int(num2)
subtraction_ab = int(num1) - int(num2)
multiplication_ab = int(num1) * int(num2)
divide_ab = int(num1) / int(num2)
power_ab = int(num1) ** int(num2)
floor_division_ab = int(num1) // int(num2)
print(f"First number :{num1}")
print(f"Second number :{num2}")
print(f"The sum of {num1} and {num2} is :{sum_ab}")
print(f"The subtraction of {num1} and {num2} is :{subtraction_ab}")
print(f"The multiplication of {num1} and {num2} is :{multiplication_ab}")
print(f"The division of {num1} and {num2} is :{divide_ab}")
print(f"The power  of {num1} and {num2} is :{power_ab}")
print(f"The floor division  of {num1} and {num2} is :{floor_division_ab}")
# Bonus tasks
greatest = max(num1, num2)
num_ceil = math.ceil(divide_ab)
print(f"The greatest  among  {num1} and {num2} is :{greatest}")
print(f"The ceil division of  {num1} and {num2} is :{num_ceil}")
# testing......
