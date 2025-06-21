import os
import time
import sys
import hashlib
import smtplib
import getpass
from email.message import EmailMessage


def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path, 'rb')

    hobj = hashlib.md5()  #md5 is an algo

    buffer = fobj.read(BlockSize)  
    while(len(buffer) > 0):
        hobj.update(buffer) 
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)      


    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The path is invalid")            
        exit()
    

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is valid but the target is not a directory")   
        exit()

    Duplicate = {}    
    TotalFiles = 0
    
    for FolderName, SubFolderNames, Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            try:
                fname = os.path.join(FolderName, fname)
                checksum = CalculateChecksum(fname)
                TotalFiles = TotalFiles + 1

                if checksum in Duplicate:
                    Duplicate[checksum].append(fname)
                else:
                    Duplicate[checksum] = [fname]
            except:
                pass

    return Duplicate, TotalFiles           



def WriteLog(Duplicate, TotalFiles, StartTime):
    filename = "MarvellousLog%s.log" % StartTime.replace(" ", "_").replace(":", "_")
    with open(filename, "w") as fobj:
        Border = "-" * 54
        fobj.write(Border + "\n")
        fobj.write("This is a log file of marvellous automation script\n")
        fobj.write("This is a directory cleaner script\n")
        fobj.write(Border + "\n")
        fobj.write("File is created at: %s\n" % StartTime)
        fobj.write("Total files scanned: %d\n" % TotalFiles)

        result = list(filter(lambda x: len(x) > 1, Duplicate.values()))
        dup_count = sum(len(group) - 1 for group in result)
        fobj.write("Duplicate files found: %d\n" % dup_count)
        fobj.write(Border + "\n")

        for value in result:
            for subvalue in value:
                fobj.write(subvalue + "\n")
            fobj.write(Border + "\n")

    return filename, dup_count


def SendMail(sender_email, sender_password, receiver_email, attachment_path, start_time, total_files, dup_count):
    msg = EmailMessage()
    msg['Subject'] = 'Duplicate File Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    body = (
        "Duplicate File Scan Report:\n\n"
        "Start Time: %s\n"
        "Total Files Scanned: %d\n"
        "Duplicate Files Found: %d\n\n"
        "Please find the attached log file for details."
        % (start_time, total_files, dup_count)
    )

    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Mail sent successfully to %s" % receiver_email)
    except Exception as e:
        print("Failed to send email: %s" % str(e))




def main():
    border = "-" * 54
    print(border)
    print("----------------Marvellous Automation-----------------")
    print(border)

    if len(sys.argv) != 2:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : used to display help")
        print("--u : used to display the usage")
        return

    DirectoryName = sys.argv[1]

    if DirectoryName in ["--h", "--H"]:
        
        print("This is the log file attachemnet to mail automation script")
        return

    if DirectoryName in ["--u", "--U"]:
        print("Use the given script as ")
        print("ScriptName.py NameOfDirectory")
        print("Please provide valid absolute path")
        return

    EmailID = input("Enter recipient email ID: ")
    SenderEmail = input("Enter your Gmail address: ")
    SenderPass = getpass.getpass("Enter your app password (not Gmail password): ")

    StartTime = time.ctime()
    Duplicate, TotalFiles = FindDuplicate(DirectoryName)
    LogFile, DupCount = WriteLog(Duplicate, TotalFiles, StartTime)
    SendMail(SenderEmail, SenderPass, EmailID, LogFile, StartTime, TotalFiles, DupCount)

    print(border)
    print("-----------Thank you for using our script-------------")
    print("---------------Marvellous Infosystems-----------------")
    print(border)


if __name__ == "__main__":
    main()    