from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    print(convert(str(input('Enter BirthDate: '))))

def convert(din):
    tdate = date.today()
    try:
        din = date.fromisoformat(din)
    except ValueError:
        sys.exit("wrong value")

    diff = ((tdate - din)*24*60).days

    return p.number_to_words(diff) 

if __name__ == '__main__':
    main()