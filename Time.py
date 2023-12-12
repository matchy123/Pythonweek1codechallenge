def convert_time(hour, minute, period):
    # Check if period is am or pm
    if period == "am":
        # If hour is 12, convert it to 00 (midnight)
        if hour == 12:
            hour = 0
    elif period == "pm":
        # If hour is less than 12, convert it to 12-hour format (afternoon)
        if hour < 12:
            hour += 12

    # Convert hour and minute to strings
    hour_str = str(hour)
    minute_str = str(minute)

    # If hour or minute is a single digit, add a leading zero
    if len(hour_str) == 1:
        hour_str = "0" + hour_str
    if len(minute_str) == 1:
        minute_str = "0" + minute_str

    # Concatenate hour and minute to form the 24-hour time
    return hour_str + minute_str

# Test cases
print(convert_time(8, 30, "am")) 
print(convert_time(8, 30, "pm")) 
print(convert_time(12, 0, "am")) 
print(convert_time(12, 0, "pm")) 
