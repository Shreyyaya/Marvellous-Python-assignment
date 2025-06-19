import psutil
import os
import time
import smtplib
import getpass
import schedule
from email.message import EmailMessage

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName) 

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "_")
    timestamp = timestamp.replace(":", "_")
    timestamp = timestamp.replace("/", "_")

    FileName = os.path.join(FolderName, "ProcessLog_%s.log" % timestamp)

    fobj = open(FileName, "w")

    border = "-" * 90
    fobj.write(border + "\n")
    fobj.write("\tMarvellous Infosystems - Process Log File\n")
    fobj.write("\tLog created at: %s\n" % time.ctime())
    fobj.write(border + "\n")
    fobj.write("PID\t\tProcess Name\t\tUsername\n")
    fobj.write(border + "\n")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            fobj.write("%s\t\t%-20s\t%s\n" % (str(info['pid']), str(info['name']), str(info['username'])))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    fobj.write(border + "\n")
    fobj.close()

    return FileName

def SendMail(sender_email, sender_password, receiver_email, attach_path):
    msg = EmailMessage()
    msg['Subject'] = 'Scheduled Process Log File'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the scheduled process log file.')

    f = open(attach_path, 'rb')
    file_data = f.read()
    file_name = os.path.basename(attach_path)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Mail sent to %s" % receiver_email)
    except Exception as e:
        print("Error sending mail: %s" % str(e))

def Job(FolderName, EmailID, SenderEmail, SenderPass):
    LogFile = CreateLog(FolderName)
    SendMail(SenderEmail, SenderPass, EmailID, LogFile)

def main():
    FolderName = input("Enter the directory name to store log files: ")
    EmailID = input("Enter the recipient email ID: ")
    Interval = int(input("Enter time interval (in minutes): "))

    print("\nEnter your Gmail credentials to send email.")
    SenderEmail = input("Enter your Gmail address: ")
    SenderPass = getpass.getpass("Enter your APP password: ")

    # Schedule
    schedule.every(1).minutes.do(Job, FolderName, EmailID, SenderEmail, SenderPass)

    print("Scheduled to run every minute")


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
