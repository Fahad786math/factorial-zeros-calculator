import math
n = int(input("Enter a positive whole number: "))
fact_result = math.factorial(n)
print(f"\nThe factorial of {n} is: {fact_result}\n")
zeros = 0
divider = 5
while n // divider > 0:
    zeros = zeros + (n // divider)
    divider = divider * 5  
print(f"Total trailing zeros at the end of {n}! are: {zeros}")
