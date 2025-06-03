class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter name: ")
        self.Amount =float(input("Enter the balance: "))   #2 instance variables name and amount
        

    def Deposit(self, A):
        self.Amount = self.Amount + A   #deposited money gets added to the existing balance and updates it
        print("Updated balance: ", +self.Amount)

    def Withdraw(self, B):
        self.Amount = self.Amount - B    #withdrawed money will get substracted from updated balance
        print("Remaining balance: " ,+self.Amount)


    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100     #interest fromula to find the interest
        print("Interest is: ", interest)
        return interest

    def Display(self):
        print("account holder name:" +self.Name)
        print("Total Remaining Balance:" ,+self.Amount)     #remianing amount after intrest

def main():
    acc1 = BankAccount()

    A = float(input("Enter an amount to deposite: "))
    acc1.Deposit(A)    #user defined input

    B = float(input("Enter amount to withdraw: "))
    acc1.Withdraw(B)

    acc1.CalculateInterest()
    acc1.Display()

if __name__ == "__main__":
    main()     

