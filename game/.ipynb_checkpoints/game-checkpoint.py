import random
while True:
    try:
        level = int(input("level: "))
        rand_num = random.randrange(1, level+1)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("guess: "))
        if guess > rand_num:
            print("too large!")
        elif guess < rand_num:
            print("too small!")
        else:
            print("just right!!")
            break
    except ValueError:
        continue