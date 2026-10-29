groc_list = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break

    if item in groc_list:
        groc_list[item] += 1
    else:
        groc_list[item] = 1

print()
for item in groc_list:
    print(f"{groc_list[item]} {item}")
