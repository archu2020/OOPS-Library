#Create a libary class
# display book
# land book
# add book
# return book
# harriLabary =libary(listbook,libary_name)
# dictionary - (book-name of person)
# create a main function and run infinate while loop asking user input
class Library:
    def __init__(self,booklist, name):
        self.booklist=booklist
        self.name=name
        self.LandDict={}


    def DisplayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def LanDictBook(self,user,book):
        if book not in self.LandDict.keys():
            self.LandDict.update({book:user})
            print("Lander book has been update you can take the book now")
        else:
            print(f" book is alredy use by {self.LandDict[book]}")

    def AddBook(self,book):
        self.booklist.append(book)
        print("Book has been added in the book list")

    def ReturnBook(self,book):
        self.LandDict.pop(book)
        print("book has been removed from the Landict book list")

if __name__ == '__main__':
    Archana=Library(["Python","You can Atchive more","C++","Java","Algorithom"],"DreamSuccess")

    while(True):
        print(f"Welcome Our {Archana.name} Library, Enter your choce to continue")
        print("1: Display Book")
        print("2: Land Book")
        print("3: Add Book")
        print("4: Return Book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Not a valid option")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            Archana.DisplayBook()

        elif user_choice==2:
            book=input("Enter the book you want to land: ")
            user=input("Enter your name: ")
            Archana.LanDictBook(user,book)

        elif user_choice==3:
            book=input("Enter the book you want add: ")
            Archana.AddBook(book)

        elif user_choice==4:
            book=input("Enter the book you want to return: ")
            Archana.ReturnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quet and c to continue")
        user_choice2=""
        user_choice2=input()
        if user_choice2=="q":
            exit()
        elif user_choice2=="c":
            continue
        else:
            print("not a valid input")



