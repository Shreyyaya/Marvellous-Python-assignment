import time
import schedule

def backup():
    timestamp = time.ctime()
    Border = "-" * 54

    source = open("original.txt", "r")
    content = source.read()
    source.close()

    dest = open("Backup_log.txt", "w")
    dest.write(content)
    dest.close()


    fobj = open("Backup_log.txt", "a")
    fobj.write(Border + "\n")
    fobj.write("This is a log entry of backup script\n")
    fobj.write(Border + "\n")
    fobj.write("Backup performed at: " + timestamp + "\n")
    fobj.write(Border + "\n\n")
    fobj.close()


def main():
    print("Performing file backup every hour and logging in Backup_log.txt...")

    schedule.every().hour.do(backup)
    backup() 

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
