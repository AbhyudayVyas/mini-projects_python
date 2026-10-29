import inflect
p = inflect.engine()

list_names = []

while True:
    try:
        name = input("Name:")
        list_names.append(name)
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(list_names)}")