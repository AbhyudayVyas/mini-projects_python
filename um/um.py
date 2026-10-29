import re
import sys

def main():
    print(count(input("string: ")))

def count(s):
    i = 0
    if re.search(r"um\b", s, re.IGNORECASE):
        matches = re.findall(r'\bum\b', s, re.IGNORECASE)
        return len(matches) 
    else:
        return 'oopsie' 

if __name__ == "__main__":
    main()