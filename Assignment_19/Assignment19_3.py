import os

def CopyFiles(src_dir, dst_dir):

    if not os.path.isabs(src_dir):
        src_dir = os.path.abspath(src_dir)

    if not os.path.isabs(dst_dir):
        dst_dir = os.path.abspath(dst_dir)

    if not os.path.exists(src_dir):
        print("Source directory is invalid.")
        return
    
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)    #mkdir is used to make a single directory
        print("Destination directory created at: " + dst_dir)
    else:
        print("Destination directory already exists at: " + dst_dir)

    
    count = 0
    for fname in os.listdir(src_dir):
        src_file = os.path.join(src_dir, fname)
        dst_file = os.path.join(dst_dir, fname)

        if os.path.isfile(src_file):
            fsrc = open(src_file, 'rb')   #rb = read in binary mode
            data = fsrc.read()

            fdst = open(dst_file, 'wb')
            fdst.write(data)

            print("Copied: " + fname)
            count = count  + 1

    print("Total files copied: " + str(count))

def main():
    print("Enter the source directory:")
    src = input()

    print("Enter the destination directory:")
    dst = input()

    CopyFiles(src, dst)

if __name__ == "__main__":
    main()
