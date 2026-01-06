class Book:
    def __init__(self, page, name):
        self.page = page
        self.name = name

    def open(self):
        print(f"opened the {self.name} which has {self.page} pages")



b1 = Book(234, "The Compound Effect")
b1.open()



class Darsi(Book):
    def __init__(self, reshte, payeh, page, name):
        Book.__init__(self, page, name)

        self.reshte = reshte
        self.payeh = payeh

        print('a new darsi book')


d = Darsi('tajrobi', 12, 234, 'the compound effect')
d.open()