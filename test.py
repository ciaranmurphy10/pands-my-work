import datetime

year = datetime.datetime.now().strftime("%Y")
month = datetime.datetime.now().strftime("%b")
day = datetime.datetime.now().strftime("%d")

print(f"Hello, the year is {year} and it is the {day} of {month}.")



try:
  amount1_int = int(amount1)
  amount1_int = int(amount1)

if type(amount1) != int or type(amount2) != int:
  raise "Please enter cent amounts as integers."