class TooManyPagesReadError(ValueError): # created new error class tha inherit existed class and i'm use it in my programm
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages}, but book has only {self.page_count} pages"
            )
        self.pages_read += pages
        print(f'Yuo have read {self.pages_read} pages out of {self.page_count}')


python_101 = Book('Python 101', 50)

# if delete try and except, you will see message as red error in console
try:
    python_101.read(35)
    python_101.read(50)
except TooManyPagesReadError as e:
    print(e)