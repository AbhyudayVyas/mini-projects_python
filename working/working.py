import re

def main():
    print(convert(input("Enter Time:")))

def convert(s):
    matches = re.search(r'^(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)$',s)
    if matches:
        shour = int(matches.group(1))

        if matches.group(2) == None:
            smin = 0
        else:
            smin = int(matches.group(2))

        ehour = int(matches.group(4))

        if matches.group(5) == None:
            emin = 0
        else:
            emin = int(matches.group(5))

        if shour<12 and smin<60 and ehour<12 and emin<60:
            if matches.group(3) == 'PM': 
                shour+=12
            if matches.group(6) == 'PM': 
                ehour+=12 
            return f"{shour:02}:{smin:02} to {ehour:02}:{emin:02}"
        else:
            raise ValueError
            #return None
    else:
        raise ValueError

if __name__ == '__main__':
    main()