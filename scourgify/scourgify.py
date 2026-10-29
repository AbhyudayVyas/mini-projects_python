import csv
import sys

try:
    if sys.argv[1].endswith('.csv'):
        if len(sys.argv)>3:
            sys.exit('too many arguments')
        try:
            with open(sys.argv[1], mode='r', newline='') as file:
                linereader = csv.DictReader(file)
                whole = []
                for line in linereader:
                    first_name, last_name = line['name'].split(', ')
                    #nesting dict in list is 🤞
                    whole.append({'first_name': first_name,
                                  'last_name': last_name,
                                  'house': line['house']})
            with open(sys.argv[2], 'w', newline='') as newfile:
                write = csv.DictWriter(newfile, fieldnames=['first_name','last_name', 'house'])
                write.writeheader()
                for row in whole:
                    write.writerow(row)
        except FileNotFoundError:
            sys.exit(f'could not read file {sys.argv[1]}')
    else:
        sys.exit('not a csv file')
except IndexError:
    if len(sys.argv)>3:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')