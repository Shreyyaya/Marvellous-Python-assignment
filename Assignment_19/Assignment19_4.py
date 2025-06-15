import os

def CopyAnExtension(src_dir, dst_dir, extension):

    if not os.path.isabs(src_dir):
        src_dir = os.path.abspath(src_dir)
    if not os.path.isabs(dst_dir):
        dst_dir = os.path.abspath(dst_dir)


    if not os.path.exists(src_dir):
        print("Source directory is invalid.")
        return


    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir) #makedirs is used to make multiple directories
        print("Destination directory created at: " + dst_dir)
    else:
        print("Destination directory already exists at: " + dst_dir)

    count = 0
    for fname in os.listdir(src_dir):
        src_file = os.path.join(src_dir, fname)
        if os.path.isfile(src_file) and fname.endswith(extension):
            dst_file = os.path.join(dst_dir, fname)

            fsrc =  open(src_file, 'rb')
            data = fsrc.read()

            fdst = open(dst_file, 'wb')
            fdst.write(data)

            print("Copied: " + fname)
            count += 1

    if count == 0:
        print("No files with extension '" + extension + " found in source directory")
    else:
        print("\nTotal files copied: " + str(count))

def main():
    print("Enter the source directory:")
    src = input()

    print("Enter the destination directory:")
    dst = input()

    print("Enter the file extension to copy:")
    ext = input()

    CopyAnExtension(src, dst, ext)

if __name__ == "__main__":
    main()
