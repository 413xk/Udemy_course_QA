class Book:
    TYPES = ('Hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, {self.weight}>'

    @classmethod
    def hardcover(cls, name, page_weight): # cls = Book = object, you can chance cls to Book, it's the same
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover('Harry Potter', 1500)
book1 = Book.paperback('Harry Potter', 1500)

print(book)
print(book1)




