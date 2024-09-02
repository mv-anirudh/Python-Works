text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowel="aeiou"
vowel_count=0
consonats_count=0
for i in text:
    # if vowel.count(i)!=0:
    # v_count+=text.count(i)
    if i in vowel:
        vowel_count+=1
    else:
        consonats_count+=1
print(vowel_count)
print(consonats_count)

   