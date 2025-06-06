class Product:

    def __init__(self, A, B):
        print("Inside constructor")    
        self.Name = A
        self.Price = B  # instance variable


    def __eq__(self, other):
        print("Inside __eq__ method")    
        return self.Price == other.Price   #eq method to compare the prices


def main():

    pro1 = Product('Bag', 50000)
    pro2 = Product('Kettle', 50000)

    if pro1 == pro2:
        print("Prices are equal")
    else:
        print("Prices are not equal")

if __name__ == "__main__":
    main()
 


