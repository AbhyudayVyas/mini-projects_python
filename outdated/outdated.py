months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]

while True:
    try:
        date = input("date: ")
        datearr = []              
        datearr = date.split(" ")
        if datearr[0] in months:
            monthd, y = date.split(",")
            month, d = monthd.split(" ")
            m = months.index(month) + 1
        else:
            m, d, y = date.split("/")
        m, d, y = int(m), int(d), int(y)
        if m>12 or d>31:
            continue
        break
    except ValueError:
        continue
print(f"{y}-{m:02d}-{d:02d}")