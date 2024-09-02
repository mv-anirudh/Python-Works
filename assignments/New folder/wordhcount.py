str=input("enter the string")

def count_words(s):
    return len(s.split())
print(f"The string contains {count_words(str)} words")
