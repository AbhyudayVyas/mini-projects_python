name = input()

for c in name:
    if c == c.capitalize():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")