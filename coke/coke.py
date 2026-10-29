def main():
    amtd = 50
    print(f"Amount Due: {amtd}")

    while amtd> 0:
        entamt = int(input("Insert Coin: "))
        if entamt in [25, 10, 5]:
            amtd-=entamt
            if amtd<0:
                break
            print(f"Amount Due: {amtd}")

    print(f"Change Owed: {abs(amtd)}")

main()