#longest palindromic substring from given string

string="RACECAR"
longest_pal=""
for i  in range(0,len(string)):
    left,right=i,i
    while(left>=0 and right<len(string)and string[left]==string[right]):
        current_pal=string[left:right+1]
        if len(current_pal)>len(longest_pal):
            longest_pal=current_pal
        left-=1
        right+=1
print(longest_pal)
    
        
    
            



        
        

       
        
        
    
    
    