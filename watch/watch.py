import re
import sys

def main():
    print(parse(input('HTML: ')))

def parse(s):
    matches = re.search(r'src=\"http.://www\.youtube\.com/embed/(.{11})', s)
    if matches:
        lcode = matches.group(1)
        return 'https://youtu.be/'+lcode
    else:
        return None

if __name__ == '__main__':
    main()
