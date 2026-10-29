with open('students.csv') as file:
    for line in file:
        # rstrip strips all the faaltu ke line breaks
        # split(",") splits again but where the line breaks and not the actual ",". why? god knows.
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")