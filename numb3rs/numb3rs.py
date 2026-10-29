import re
import sys

def main():
    print(validate(input("ipv4 address: ").strip()))

def validate(ip):
    if re.search("[0-9].[0-9].[0-9].[0-9]", ip):
        for a in ip.split('.'):
            if int(a)>255 or (str(a).startswith('0') and len(a)>1):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()