word1 = "pqrst"
word2 = "abc"
smallest_word = word1 if len(word1) < len(word2) else word2
merged_string = ""

for i in range(len(smallest_word)):
    merged_string += word1[i] + word2[i]

if len(word1) > len(word2):
    balance = word1[len(smallest_word):]
else:
    balance = word2[len(smallest_word):]

merged_string += balance

print(merged_string)
