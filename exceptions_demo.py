

# Answers to the questions:
# 1. A ValueError will occur if the input for the numerator or the denominator is not a valid integer.
# 2. A ZeroDivisionError will occur if the denominator is zero when attempting the division.
# 3. To avoid the possibility of a ZeroDivisionError, the code can be modified to check if the denominator is zero before performing the division.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for zero denominator before attempting the division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")