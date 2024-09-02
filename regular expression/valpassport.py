    # It should be eight characters long.
    # The first character should be an uppercase alphabet.
    # The next two characters should be a number, but the first character should be any number from 1-9 and the second character should be any number from 0-9.
    # It should be zero or one white space character.
    # The next four characters should be any number from 0-9.
    # The last character should be any number from 1-9.
from re import fullmatch

passport_num=input("enter your passpot number: ")

pattern="[A-Z]{1}[1-9][0-9](\\s|0)?[0-9]{4}[1-9]{1}"
matcher=fullmatch(pattern,passport_num)

print("invalid" if matcher==None  else "valid")
