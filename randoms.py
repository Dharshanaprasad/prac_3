import random

# Running each line multiple times to observe the outputs
print(random.randint(5, 20))  # line 1
# Observations:
# - This will print a random integer between 5 and 20 inclusive.
# - The smallest number that can be seen is 5.
# - The largest number that can be seen is 20.

print(random.randrange(3, 10, 2))  # line 2
# Observations:
# - This will print a random number from the sequence 3, 5, 7, 9.
# - The smallest number that can be seen is 3.
# - The largest number that can be seen is 9.
# - Line 2 cannot produce a 4 because the step is 2, starting from 3.

print(random.uniform(2.5, 5.5))  # line 3
# Observations:
# - This will print a random floating-point number between 2.5 and 5.5.
# - The smallest number that can be seen is 2.5.
# - The largest number that can be seen is 5.5.

# Code to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
