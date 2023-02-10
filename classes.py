
class Book:
    def __init__(self, title, author, numberofpages, publisher):
        self.title = title
        self.author = author
        self.numberofpages = numberofpages
        self.publisher = publisher


myBook = Book("Coding is art", "Becky", 435, "OC")

print("Book title "+myBook.title +" Book author" +myBook.author)

class team:
    def __init__(self,country, name, type):
        self.country = country
        self.name = name
        self.type = type


player1 = team("Pakistan", " Muhammad Yousaf", " Batsman")
print(player1.country+player1.type+player1.name)