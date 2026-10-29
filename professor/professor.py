import random

def get_level():
    while True:
            level = int(input("level: "))
            if 0<level<4:
                break
            else:
                raise ValueError
    return level

def generate_integer(level):
    if level == 1: return random.randint(0, 9)
    if level == 2: return random.randint(10, 99)
    if level == 3: return random.randint(100, 999)
    
def main():
    score = 0

    level = get_level()

    for i in range(10):
        cntr = 0
        nX = generate_integer(level)
        nY = generate_integer(level)
        while cntr<3:
            ans = int(input(f"{nX} + {nY} = "))
            if ans == nX + nY:
                score+=1
                break
            else:
                print("wrong answer")
                cntr+=1
        if cntr==3:
            print(nX + nY)

    print(f"Score: {score}")

if __name__ == "__main__":
    main()