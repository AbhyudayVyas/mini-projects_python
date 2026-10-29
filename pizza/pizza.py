from tabulate import tabulate 
import sys
import csv

def main():
    try:
        if sys.argv[1].endswith('.csv'):
            if len(sys.argv)>2:
                    sys.exit('too many arguments')
            try:
                with open(sys.argv[1], 'r', newline='') as file:
                    tab = []
                    for line in file:
                        row = line.split(',')
                        tab.append(row)
                    #headers = tab[0]
                    print(tabulate(tab, tablefmt="grid"))
            except FileNotFoundError:
                sys.exit('file not found')
        else:
            sys.exit('not a csv file')
    except IndexError:
        if len(sys.argv)>2:
            sys.exit('too many arguments')
        else:
            sys.exit('too few arguments')

if __name__ == "__main__":
    main()
