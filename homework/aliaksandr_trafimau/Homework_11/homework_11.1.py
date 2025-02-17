class Book:
    material_book = 'Paper'
    text = True

    def __init__(self, name_of_book, author, number_of_pages, isbn, is_reserved):
        self.name_of_book = name_of_book
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def reservation(self):
        return 'Reserved' if self.is_reserved else ''

    def __str__(self):
        reservation_info = self.reservation()
        if reservation_info:
            reservation_info = ', ' + reservation_info
        return (f"name: {self.name_of_book}, author: {self.author}, "
                f"pages: {self.number_of_pages}, ISBN: {self.isbn}, "
                f"material: {self.material_book}{reservation_info}")


book1 = Book("1984", "George Orwell", 328, "978-0451524935", False)
book2 = Book("Pride and Prejudice", "Jane Austen", 279, "978-1503290563", True)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "978-0743273565", False)
book4 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 309, "978-0590353427", True)
book5 = Book("To Kill a Mockingbird", "Harper Lee", 281, "978-0446310789", False)

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)


class SchoolBook(Book):
    building = True

    def __init__(self, name_of_book, author, number_of_pages, isbn, is_reserved, subject, class_):
        super().__init__(name_of_book, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.class_ = class_

    def __str__(self):
        reservation_info = self.reservation()
        if reservation_info:
            reservation_info = ', ' + reservation_info
        return (f"name: {self.name_of_book}, author: {self.author}, "
                f"pages: {self.number_of_pages}, subject: {self.subject}, class: {self.class_}, "
                f"ISBN: {self.isbn}, material: {self.material_book}{reservation_info}")


school_book1 = SchoolBook('Algebra', 'Ivanov', 667, '988-213214312', False, 'Mathematics', '4')
school_book2 = SchoolBook('Nuclear Physics', 'Ivanov', 667, '988-213214312', True, 'Physics', '2')

print(school_book1)
print(school_book2)
