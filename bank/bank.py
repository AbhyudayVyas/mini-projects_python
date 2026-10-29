
def main():
    greet = input("Greeting: ").lower()
    print(f"${value(greet)}")



def value(greet):    
    if greet.startswith("h"):
        if greet.startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()