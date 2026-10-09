import datetime
from utils import add, subtract,multiply,divide

# 1. Print my name
print("Name: Md.Jahidul Islam Bejoy")

# 2. Print today's date
date = datetime.date.today()
print("Today's Date:", date) 
print("\n") 

# 3. Call calculator functions
a=97
b=0
sum = add(a, b)
sub = subtract(a, b)
mult= multiply(a, b)
div=divide(a,b)

print(f"Total = {sum}")
print(f"Difference = {sub}")
print(f"Multiply = {mult}")
print(f"Division = {div}")