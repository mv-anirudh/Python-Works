class Book:
    def __init__(self, title, author, price, language):
        self.title = title
        self.author = author
        self.price = price
        self.language = language
        
    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\nLanguage: {self.language}")
        
    def __str__(self):          # String representation 
        return self.title

        
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display()
            print('')  


book1 = Book("hi", "jj", 80, "mal")
book2 = Book("The Alchemist", "Paulo Coelho", 300, "English")
book3 = Book("Think and Grow Rich", "Napoleon Hill", 500, "English")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
