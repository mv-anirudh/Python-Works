def poll(age):
    if age<18:
        raise Exception("invalid age") 
#raise Exception("invalid age") is used to raise an exception with the message "invalid age".

    else:
        print("vaild age")
        
try:
    poll(15)
    
except Exception as e:
    print(e)
    