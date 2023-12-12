def two_positive_numbers(a, b, c):
    # Initialize a counter for positive numbers
    positive_count = 0

    # Check if each number is positive and increment the counter if it is
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two numbers are positive, and False otherwise
    return positive_count == 2

# Test cases
print(two_positive_numbers(2, 4, -3)) 
print(two_positive_numbers(-4, 6, 8)) 
print(two_positive_numbers(4, -6, 9)) 
print(two_positive_numbers(-4, 6, 0)) 
print(two_positive_numbers(4, 6, 10)) 
print(two_positive_numbers(-14, -3, -4)) 