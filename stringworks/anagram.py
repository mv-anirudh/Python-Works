#check souruce_word and target_word is anagrma
source_word="listen"
target_word="silent"
def is_anagram(source_word, target_word):
    source_word = source_word.lower()
    target_word = target_word.lower()
    if len(source_word) != len(target_word):
        return False
    else:
        for i in range(len(source_word)):
            if source_word[i] not in target_word:
                return False
            return True
        
   
      
print(is_anagram(source_word,target_word))
   