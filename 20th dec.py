import re 
 
class Member: 
    def __init__(self, name, email): 
        self.name = name 
        self.email = email 
        self.member_id = self.generate_member_id() 
 
        if not self.verify_email_format(): 
            raise ValueError(f"Invalid email format: {self.email}") 
 
    def generate_member_id(self): 
        id_number = 1000   
        id_number += 1 
        return f"LIB{id_number}" 
 
    def verify_member_id(self, member_id): 
        if re.match(r"^LIB\d{4}$", member_id): 
            return True 
        return False 
 
    def verify_email_format(self): 
        if re.match(r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$", self.email): 
            return True 
        return False 
 
class Library(Member): 
    def __init__(self): 
        self.books = {} 
        self.members = {} 
        self.borrowed_books = {} 
 
    def add_book(self, book_id, title, author): 
        if book_id in self.books: 
            raise ValueError("Book ID already exists.") 
        self.books[book_id] = {"title": title, "author": author, "available": True} 
 
    def register_member(self, name, email): 
        member = Member(name, email) 
        if member.member_id in self.members: 
            raise ValueError("Member ID already exists.") 
        self.members[member.member_id] = member 
        return member.member_id 
 
    def borrow_book(self, member_id, book_id): 
        if member_id not in self.members: 
            raise ValueError("Invalid Member ID.") 
        if book_id not in self.books: 
            raise ValueError("Book not found.") 
        if not self.books[book_id]["available"]: 
            raise ValueError("Book is already borrowed.") 
        self.books[book_id]["available"] = False 
        self.borrowed_books[book_id] = member_id 
 
    def return_book(self, book_id): 
        if book_id not in self.borrowed_books: 
            raise ValueError("Book not borrowed.") 
        self.books[book_id]["available"] = True 
        del self.borrowed_books[book_id] 
 
library = Library() 
 
library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald") 
library.add_book("B002", "1984", "George Orwell") 
member_id = library.register_member("Alice", "alice@example.com") 
print(f"Member Registered: {member_id}") 
library.borrow_book(member_id, "B001") 
print("Book borrowed successfully.") 
library.return_book("B001") 
print("Book returned successfully.")