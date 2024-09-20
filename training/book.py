class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def get_description(self):
        return f"{self.title}-{self.autor}"
