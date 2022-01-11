import os
import sys

def exploit(file):
    print("[*] Process started.")
    os.system("xattr -d com.apple.quarantine " + file)
    print("[*] Process finished.")

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("[*] No arguments given.")
        print("[*] Example: python ./main.py <file>")
        sys.exit(1)
    
    # if not os.path.isfile(args[0]):
    #     print("[*] File not found.")
    #     print("[*] Example: python ./main.py <file>")
    #     sys.exit(1)
    
    print("[*] File found.")

    exploit(args[0])

    print("[*] Process finished successfully.")

if __name__ == "__main__":
    main()