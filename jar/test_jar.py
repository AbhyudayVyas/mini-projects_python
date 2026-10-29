from jar import Jar


def test_init():
    ...


def test_str():
    jar = Jar()
    print(jar.size)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    print(jar.size)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    print(jar.size)
    assert jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

def main():
    test_str()
    test_deposit()
    test_withdraw()

if __name__ == '__main__':
    main()