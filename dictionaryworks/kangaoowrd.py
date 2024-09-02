source_word="chicken"

targeet_word="hen"

word_count={}

for ch in source_word:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
    
is_kangaro_word=True
        
for ch in targeet_word:
    if ch in word_count and word_count.get(ch)>0:
        word_count[ch]-=1
    else:
        is_kangaro_word=False
        
        break
        
print(is_kangaro_word)
        