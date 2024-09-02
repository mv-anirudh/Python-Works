f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\news.txt","r")

word_list=[w for line in f for w in line.rstrip("\n").split(" ")]
word_count={}
for w in word_list:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1

counts = sorted(word_count.items(), key=lambda kv: kv[1],reverse=True)
most_common_word = counts[0]
count_X=word_count.get(counts[0])



        