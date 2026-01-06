class Book:
    def __init__(self, pages):
        self.pages = pages

    def open(self):
        print("opened the book")



b = Book(100)

print(b.pages)
print(b.open())



class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def masahat(self):
        s = self.pi * self.r**2
        return s

    def mohit(self):
        p = 2 * self.pi * self.r
        return p


c1 = Circle(5)
print(c1.masahat())
print(c1.mohit())