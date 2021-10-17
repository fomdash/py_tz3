


def read_file():
    data = []
    with open("data.txt") as f:
        for line in f:
            line_list = [int(x) for x in line.split(' ')]
            data.extend(line_list)
    return data


def list_sum(lst):
    summa = 0
    for a in lst:
        summa = summa + a

    return summa


def list_mult(lst):
    mult = 1
    for a in lst:
        mult = mult * a
    #
    return mult


def tz3():
    lst = read_file()
    print(lst)

    minnumb = min(lst)
    print(f'Минимльное: {minnumb}')

    maxnumb = max(lst)
    print(f'Максимальное: {maxnumb}')

    summa = list_sum(lst)
    mult = list_mult(lst)

    print(f'Сумма: {summa}')
    print(f'Произведеие: {mult}')


def test_read_file():
    lst = read_file()
    assert lst == [1, 4, 2, 3]


def test_mult():
    lst = [1, 4, 2, 3]
    mult = list_mult(lst)
    assert mult == 1 * 4 * 2 * 3


def test_sum():
    list = [1, 4, 2, 3]
    mult = list_sum(list)
    assert mult == 1 + 4 + 2 + 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tz3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/