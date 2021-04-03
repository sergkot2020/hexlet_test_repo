import prompt


def func2():
    c = 3
    n = 7
    n / 0
    return n - c


def test_function():
    a = 5
    b = 4
    for i in range(100):
        pass
    func2()
    return a + b


if __name__ == '__main__':
    print(test_function())
