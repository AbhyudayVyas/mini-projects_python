def gauge(centage):
    if centage<=1:
        return "E"
    elif centage>=99:
        return "F"
    else:
        return f"{centage}%"

def convert(fraction):
    X, Y = fraction.split("/")
    X = int(X)
    Y = int(Y)
    if isinstance(X, int) and isinstance(Y, int) and X<=Y and Y!=0:
        return round((X/Y)*100)
    elif Y==0:
        raise ZeroDivisionError
    else:
        raise ValueError

def main():
   while True:
        frac = input("Fraction: ")
        print(gauge(convert(frac)))
        break
            
if __name__ == "__main__":
    main()

# while True:    
#     try:
#         frac = input("Fraction: ")
#         # X, Y = frac.split("/")
#         # X = int(X)
#         # Y = int(Y)
#     except (ValueError, ZeroDivisionError):
#         continue
#     #if isinstance(X, int) and isinstance(Y, int) and X<=Y and Y!=0:
#         #centage = round((X/Y)*100)
#     print(gauge(convert(frac)))
#     #break
    