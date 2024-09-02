text = "abcadd"
rec = {}
first_recurring = None

for w in text:
    if w in rec:
        first_recurring = w
        break
    else:
        rec[w] = 1

print("The first recurring character is:", first_recurring)
