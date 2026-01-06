class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(self.title)
        print(self.author)
        print(self.pages)

    def __len__(self):
        return self.pages

    def __str__(self):
        return self.title

    def __del__(self):
        print(f"{self.title} book deleted.")