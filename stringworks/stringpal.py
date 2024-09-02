# create a function is_palinfrome(word)return true if word is a palinodrome string
# otherwise return false
def is_palindrome(word):
    rev_word = word[::-1]
    return word ==rev_word
print(is_palindrome("madam"))
    
