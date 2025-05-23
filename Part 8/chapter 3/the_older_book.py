class Book:
    def __init__(self, name: str, author: str,genre: str ,year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if book1.year > book2.year:
        print(f"High Adventure is older, it was published in {book2.year}")
    elif book2.year < book1.year:
        print(f"High Adventure is older, it was published in {book1.year}")
    else:
        print(f"{book1.name} and {book2.name} were published in {book2.year}")

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)