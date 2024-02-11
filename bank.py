# Request the user to enter an amount in cent and save it to the variable amount1. 
# This variable will be of type string, even if the user types an integer.
amount1 = input("Enter amount1(in cent): ") 

# Try to convert the amount entered to an integer. If it can't be converted, request the user to enter an integer. 
try:
  amount1_int = int(amount1)
except TypeError:
  print("It looks like you haven't entered an amount in cent. Please run the script again and enter an integer.")
  raise

# Request the user to enter an amount in cent and save it to the variable amount2. 
# This variable will be of type string, even if the user types an integer.
amount2 = input("Enter amount2(in cent): ")

# Try to convert the amount entered to an integer. If it can't be converted, request the user to enter an integer. 
try:
  amount2_int = int(amount2)
except TypeError:
  print("It looks like you haven't entered an amount in cent. Please run the script again and enter an integer.")

# Add the two integer amounts together and save the sum to the variable sum_in_cent.
sum_in_cent = amount1_int + amount2_int 

# Use floor division to find the euro amount of the ent amount. 
sum_euro_part = sum_in_cent // 100

# Use modulo to find the cent amount of the cent amount.
sum_cent_part = sum_in_cent % 100

# Use f strings to print the euro and cent amount in a human readable format. 
print(f"The sum of these is €{sum_euro_part}.{sum_cent_part}")