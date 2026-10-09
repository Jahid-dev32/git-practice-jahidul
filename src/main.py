import datetime
from utils import add, subtract

# 1. Print my name
print("Name: Md.Jahidul Islam Bejoy")

# 2. Print today's date
date = datetime.date.today()
print("Today's Date:", date) 

# 3. Call calculator functions
sum = add(32, 97)
sub = subtract(97, 32)

print(f"Total = {sum}")
print(f"Difference = {sub}")