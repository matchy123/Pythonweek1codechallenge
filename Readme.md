Python-Code-Challenge
#Challenge 1: Converting 12-hour time to 24-hour time
#Task
-Write a function that converts a 12-hour time to a 24-hour time.
#Function Signature
def convert_to_24_hour_format(hour, minute, period):
-In this solution, the convert_time function first checks if the period is "am" or "pm". If the period is "am", the function checks if the hour is 12, and if so, convert it to 00. If the period is "pm", the function checks if the hour is less than 12, and if so, converts it to the 12-hour format.
Next, the function converts the hour and minute to strings and checks if each string is a single digit. If so, it adds a leading zero to the string.
Finally, the function concatenates the hour and minute strings to form the 24-hour time.

#Challenge2:Two numbers are positive
#Task
Write a function that takes three integers and returns True if exactly two of them are positive numbers, and False otherwise.
#Function
def two_positive(a, b, c):
#Explanation
-In this solution, the two_positive_numbers function initializes a counter called positive_count to keep track of the number of positive numbers encountered. The function then checks if each of the three integers a, b, and c is greater than zero. If a number is positive, the function increments the positive_count by 1. Finally, the function returns True if the positive_count is equal to 2, and False otherwise.
#Challenge 3: Consonant Value
#Task
-Write a function that returns the highest value of consonant substrings in a lowercase string.
#Function
def solve(s):
 #Explanation
-To solve this problem, we can iterate through the given string and check if each character is a consonant. If it is, we assign it a value according to its position in the alphabet (starting from 1). We then use a dynamic programming approach to keep track of the maximum value of consonant substrings.







