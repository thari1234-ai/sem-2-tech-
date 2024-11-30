class Book:
    def __init__(self,book_name,book_author,book_genre):
        self.book_name=book_name
        self.book_author=book_author
        self.book_genre=book_genre
    def display_book(self):
        print(self.book_name)
        print(self.book_author)
        print(self.book_genre)
        
class Member:
    def __init__(self,Name,Age,phone_num):
        self.Name=Name
        self.Age=Age
        self.phone_num=phone_num
    def display_member(self):
        print(self.Name)
        print(self.Age)
        print(self.phone_num)

class Librarymanagement(Book,Member):
    def __init__(self,book_name,book_author,book_genre,Name,Age,phone_num):
        super().__init__(book_name,book_author,book_genre)
        Member.__init__(self,Name,Age,phone_num)
    def display_librarymanagement(self):
        self.display_book()
        self.display_member()
t=Librarymanagement('Maths','karthika','education','Tharini','17',0000000000)
t.display_librarymanagement()


        

    