#QUESTION 2
def is_palindrome(text):
    # I Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    # I Check if cleaned text is equal to its reverse text
    return cleaned_text == cleaned_text[::-1]

# Test cases calling the function to check if it palindrome
print(is_palindrome("madam"))# True
print(is_palindrome("kayak"))# True
print(is_palindrome("racecar"))# True
print(is_palindrome("nurses run"))# True
print(is_palindrome("hello"))# False
print(is_palindrome("hell"))# False
