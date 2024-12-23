from hello import fizz


def test_fizz_1():
    assert "1" == fizz(1)


def test_fizz_2():
    assert "2" == fizz(2)


def test_fizz_3():
    assert "fizz" == fizz(3)


def test_fizz_5():
    assert "buzz" == fizz(5)


def test_fizz_6():
    assert "fizz" == fizz(6)


def test_fizz_15():
    assert "fizzbuzz" == fizz(15)
