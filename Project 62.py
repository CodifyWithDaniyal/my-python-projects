# This program defines a simple Library class.
# - It maintains a list of books and allows adding new books.
# - The addbook(book) method adds a book to the library.
# - The shownobooks() method prints the total number of books and lists all book titles.
# Example:
#   a = Library()
#   a.addbook("Harry Potter")
#   a.addbook("Harry Potter1")
#   a.shownobooks()
class Library:
    def __init__(self):
        self.books=[]
        self.nobooks=0
    def addbook(self,book):
        self.books.append(book)
    def shownobooks(self):
        print(f"The library has {len(self.books)} books.The books are:")
        for book in self.books:
            print(book)
a=Library()
a.addbook("Harry Potter")
a.addbook("Harry Potter1")
a.shownobooks()