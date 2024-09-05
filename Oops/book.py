class Book:
    title:str
    author:str
    price:int
    language:str
    
    
    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language
        
    def display(self):
        print(f"title:{self.title}\n author:{self.author}\n price:{self.price}\n language:{self.language}")
        
    def __str__(self):          #string representation 
        return self.title
        

book=Book("hi","jj",80,"mal")
book.display()

print(book)


