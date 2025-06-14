import schedule
import time

def print():
    print("Namaskar..")

def main():
    schedule.every().day.at("09:00").do(print)

    print("Scheduler started... Waiting for 9:00 AM.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
