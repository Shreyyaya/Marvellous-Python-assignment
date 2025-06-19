import psutil

def CheckProcess(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == name:
            print("The process is running")
            return
    print("The process is not running")

def main():
    CheckProcess(input("Enter the actual name of process with extension:"))  

if __name__ == "__main__":
    main()
