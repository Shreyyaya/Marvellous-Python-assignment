import time
import schedule

def minutes():
    timestamp = time.ctime()
    Border = "-" * 54

    fobj = open("Marvellous.txt", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log entry of Marvellous automation script\n")
    fobj.write(Border + "\n")
    fobj.write("Time: " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    fobj.close()

def main():
    print("Logging time every 5 minutes to Marvellous.txt...")

    schedule.every(5).minutes.do(minutes)
    minutes() 

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
