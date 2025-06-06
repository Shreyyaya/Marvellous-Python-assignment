#method overriding

class Vehicle:
    def Start(self):   #overridden method
        print('inside base display')


class Derived(Vehicle):
    def Start(self):    #overrided method
        print('inside Derived display')


def main():
    bobj = Vehicle()
    dobj = Derived()


    bobj.Start()    
    dobj.Start()


if __name__ == "__main__":
    main()      