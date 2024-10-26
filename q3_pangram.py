#QUESTION 3
def is_pangram(text):
    #I Convert the text to lowercase and create characters
    text = text.lower()
    #I Create a set of all lowercase alphabet letters
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    #I Check if all alphabet letters are in the text
    return alphabet.issubset(set(text))

# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))#True
print(is_pangram("Hello world"))#False
print(is_pangram("Pack my box with five dozen liquor jugs"))#True
