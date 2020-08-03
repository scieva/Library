class Book:
    def __init__(self, author, title, isbn):
        # initialising the class its self with the needed attributes
        self.author = author
        self.title = title
        self.ISBN = isbn

    def __str__(self):
        # a simple method to printing the object attributes as a string
        return "%s : %s - %s" % (self.ISBN, self.author, self.title)


class Row:
    def __init__(self, id, books):
        self.ID = id
        self.books = books

    def inventorylist(self):
        print("\t\tRow with ID " + str(self.ID) + " has the following books:")
        for book in self.books:
            print("\t\t\t" + book.__str__())

    def findbook(self, isbn):
        flag = False
        for book in self.books:
            if book.ISBN == isbn:
                flag = True
                print("The book with ISBN: " + str(isbn) + ", is on the row with ID: " + str(self.ID), end="")
        return flag


class Bookshelf:
    def __init__(self, id, rows):
        self.ID = id
        self.rows = rows

    def inventorylist(self):
        print("\tBookshelf with ID " + str(self.ID) + " has the following rows:")
        for row in self.rows:
            row.inventorylist()

    def findbook(self, isbn):
        flag = False
        for row in self.rows:
            if row.findbook(isbn):
                flag = True
                print(", that's on the bookshelf with ID: " + str(self.ID), end="")
        return flag


class Room:
    def __init__(self, id, bookshelves):
        self.ID = id
        self.bookshelves = bookshelves

    def inventorylist(self):
        print("Room with ID " + str(self.ID) + " has the following bookshelves:")
        for bookshelf in self.bookshelves:
            bookshelf.inventorylist()

    def findbook(self, isbn):
        flag = False
        for bookshelf in self.bookshelves:
            if bookshelf.findbook(isbn):
                flag = True
                print(", in the room with ID: " + str(self.ID) + ".")
        return flag


class Library:
    def __init__(self, rooms):
        self.rooms = rooms

    def findbook(self, isbn):
        flag = False
        for room in self.rooms:
            if room.findbook(isbn):
                flag = True
        if not flag:
            print("A book with ISBN: " + str(isbn) + " does NOT exist in this library.")
        return flag

    def printbooks(self):
        print("This library has the following rooms:")
        for room in self.rooms:
            room.inventorylist()

    def insertbook(self, book):
        flag = False
        for room in self.rooms:
            for bookshelf in room.bookshelves:
                for row in bookshelf.rows:
                    for b in row.books:
                        if b.ISBN == book.ISBN:
                            print("Unable to add book - a book with ISBN " + str(book.ISBN) + " already exists!")
                            return False
                    if str(row.ID) == str(book.ISBN)[0:3]:
                        flag = True
                        row.books.append(book)
        if not flag:
            newrow = Row(int(str(book.ISBN)[0:3]), [book])
            newbookshelf = Bookshelf(int(str(book.ISBN)[0:2]), [newrow])
            newroom = Room(int(str(book.ISBN)[0]), [newbookshelf])
            self.rooms.append(newroom)
        return book.ISBN


l = []
for i in range(1, 4): # we will have 3 rooms
    ro = []
    for j in range(1, 4): # each room filled with 3 bookshelves
        b = []
        for x in range(1, 4): # each bookshelf filled with 3 rows
            r = []
            for y  in range(1, 4): # each row filled with 3 books
                writer = "John " + str(y) + " Doe"
                book = "The Book: " + str(y)
                book = Book(writer, book, (i*1000 + j*100 + x*10 + y))
                r.append(book)
            row = Row((i*100 + j*10 + x*1), r)
            b.append(row)
        bookshelf = Bookshelf((i*10 + j), b)
        ro.append(bookshelf)
    room = Room(i, ro)
    l.append(room)
    library = Library(l)

print("Testing finding a book in the library:")
library.findbook(1223)
library.findbook(5678)
print()

print("Testing inserting a book in the library:")
test1 = Book("George Orwell", "1984", 4111)
library.insertbook(test1)

test2 = Book("John Steinbeck", "The Grapes of Wrath", 3112)
library.insertbook(test2)

test3 = Book("John Steinbeck", "The Grapes of Wrath", 1115)
library.insertbook(test3)
print()

print("Finally printing all the books in the library:")
library.printbooks()