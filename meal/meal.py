def main ():
    tim = input("What time is it? ")
    if 7 <= convert(tim) <= 8:
        print("breakfast")
    elif 12 <= convert(tim) <= 13:
        print("lunch")
    elif 18 <= convert(tim) <= 19:
        print("dinner")
    else:
        return 0

def convert(time):
    hr, minutes = time.split(":")
    minutes = float(minutes)
    hr = float(hr)
    ttime = hr + minutes/60
    return ttime

if __name__ == "__main__":
    main()
