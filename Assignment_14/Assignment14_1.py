
class Employee:

    def __init__(self, A, B, C):
        print("Inside constructor")    

        self.Name = A
        self.id = B
        self.Salary = C       #these 3 are instance variables

    def __del__(self):
        print("Inside destructor")    



def main():

    emp1 = Employee('Rohit', 101, 50000)
    

    print("Name: " +emp1.Name)
    print("ID: ",+emp1.id)
    print("Salary: ", +emp1.Salary)



if __name__ =="__main__":
    main()    


