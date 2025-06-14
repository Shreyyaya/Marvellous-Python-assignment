import time
import schedule

def CheckMail():
    print("Checking for new email...")

def main():
    print("Starting mail checker...")

    schedule.every(10).seconds.do(CheckMail)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
