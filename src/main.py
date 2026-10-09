import datetime
from utils import add, subtract,multiply

# 1. Print my name
print("Name: Md.Jahidul Islam Bejoy")

# 2. Print today's date
date = datetime.date.today()
print("Today's Date:", date) 
print("\n") 

# 3. Call calculator functions
sum = add(32, 97)
sub = subtract(97, 32)
mult= multiply(32, 9)


print(f"Total = {sum}")
print(f"Difference = {sub}")
print(f"Multiply ={mult}")