text="the quick brown fox jumps over a lazy dog"
text=text.casefold()
is_Panagram=True
alpha="abcdefghijklmnopqrstuvwxyz"

for ch in alpha:
    if text.count(ch)==0:
        is_Panagram=False
        break
print(is_Panagram)

