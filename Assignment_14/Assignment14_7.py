
class Person:

    def __init__(self, A, B):
        print("Inside Person constructor")

        self.Name = A
        self.Age = B     #base class


class Teacher(Person):
    def __init__(self, A, B):
        print("Inside Teacher constructor")
        super().__init__(A, B)    #derived class 


def main():
    obj = Teacher("Mohit", 28)

    print("Name is:", obj.Name)
    print("Age of Teacher is:", obj.Age)


if __name__ == "__main__":
    main()    