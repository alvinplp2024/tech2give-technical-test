#QUESTION 4
def reverse_integer(n):
    #I Convert integers to string, then reverse them, and handle negative sign if needed
    reversed_str = str(n)[::-1] if n >= 0 else "-" + str(n)[:0:-1]
    #I Convert back to integer and I can remove any leading zeros
    return int(reversed_str)

# Test cases
print(reverse_integer(500))# 5
print(reverse_integer(-56))# -65
print(reverse_integer(-90))# -9
print(reverse_integer(91))# 19
print(reverse_integer(991))#199
print(reverse_integer(917))#719
