
class Student:
    SchoolName = "Marvellous"    #class variable

    def __init__(self, A, B):
        print("Inside constructor")    

        self.Name = A
        self.roll_no = B      #these 3 are instance variables

    def __del__(self):
        print("Inside destructor")    



def main():

    print("Class variable: " +Student.SchoolName)

    Stud1 = Student('Rohit', 15)

    print("Student name: " +Stud1.Name)
    print("Roll number: ",+Stud1.roll_no)


if __name__ =="__main__":
    main()    


