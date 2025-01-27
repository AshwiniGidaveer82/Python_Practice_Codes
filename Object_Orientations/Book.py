class Book:
    
    def __init__(self, title, author):

        self.title = title

        self.author = author

        self.is_available = True

 

    def display_info(self):

        if self.is_available:

            status = "Available" 

        else:

            status = "Borrowed"

        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

 

    def mark_borrowed(self):

        if self.is_available:

            self.is_available = False

            print(f"{self.title} has been marked as borrowed.")

        else:

            print(f"{self.title} is already borrowed.")

 

book = Book("1984", "George Orwell")

book.display_info()

book.mark_borrowed()

book.display_info()