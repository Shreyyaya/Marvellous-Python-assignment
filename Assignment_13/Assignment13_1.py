class BookStore:
    NoOfBooks = 0 #class var initialised at 0 

    def __init__ (self, A, B):  #instance method
        print("inside constructor")

        self.Name = A
        self.Author = B
        BookStore.NoOfBooks = BookStore.NoOfBooks+1   #increment by 1
 
    def __del__(self):
        print("Inside destructor")

    def Display(self): #the print statement
        print(self.Name, "by", self.Author, "No of Books:", BookStore.NoOfBooks)


def main():
    obj1 = BookStore("Linux programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C programming", "Dennis Ritchie")
    obj2.Display()

    obj3 = BookStore(input("Name of book:"), input("Name of author:"))
    obj3.Display()   #user defined input


if __name__ == "__main__":
    main()    
