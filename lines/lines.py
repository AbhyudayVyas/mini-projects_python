import sys

i = 0

try:
    if sys.argv[1].endswith(".py"):
        if len(sys.argv)>2:
            sys.exit('too many arguments')
        try:
            with open(sys.argv[1], 'r') as code:
                for line in code:
                    if line.lstrip().startswith('#'):
                        continue
                    i+=1
                print(i)
        except FileNotFoundError:
            sys.exit('file not found')
    else:
        sys.exit("not a python file")
except IndexError:
    if len(sys.argv)>2:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')
