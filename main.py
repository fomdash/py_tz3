import pytest

def read_file(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            for n in line.split(' '):
                data.append(int(n))
    return data


def list_sum(lst):
    summa = 0
    for a in lst:
        summa += a
    return summa


def list_mult(lst):
    mult = 1
    for a in lst:
        mult *= a
    return mult


def tz3():
    lst = read_file("data.txt")
    print(lst)

    minnumb = min(lst)
    print(f'Минимальное: {minnumb}')

    maxnumb = max(lst)
    print(f'Максимальное: {maxnumb}')

    summa = list_sum(lst)
    mult = list_mult(lst)

    print(f'Сумма: {summa}')
    print(f'Произведеие: {mult}')

def test_min():
    lst = [1, 4, 2, 3]
    minnumb = min(lst)
    assert minnumb == 1

def test_max():
    lst = [1, 4, 2, 3]
    maxnumb = max(lst)
    assert maxnumb == 4

def test_read_file():
    lst = read_file("data.txt")
    assert lst == [1, 4, 2, 3]


def test_mult():
    lst = [1, 4, 2, 3]
    mult = list_mult(lst)
    assert mult == 1 * 4 * 2 * 3


def test_sum():
    list = [1, 4, 2, 3]
    mult = list_sum(list)
    assert mult == 1 + 4 + 2 + 3


if __name__ == '__main__':
    tz3()
