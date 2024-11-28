#not parametrized constructor
class Library:
    def __init__ (self):
        self.book_name=input()
        self.author_name=input()
    def display_book(self):
        print(f"bookname:{self.book_name}")
        print(f"authorname:{self.author_name}")
my_library=Library()
my_library.display_book()