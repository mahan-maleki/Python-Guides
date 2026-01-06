class Book():
    def __init__(self, pages):
        self.pages = pages



mybook = Book(540)

print(mybook.pages)
print(type(mybook))

yourbook = Book(50)

print(mybook.pages)
print(type(mybook))