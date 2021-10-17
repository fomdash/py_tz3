import pytest
import random
import time
import os


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
    try:
        for a in lst:
            mult *= a
    except:
        mult = -1
    return mult



def process_all_steps(file_name):
    lst = read_file(file_name)
    print(lst)

    minnumb = min(lst)
    print(f'Минимальное: {minnumb}')

    maxnumb = max(lst)
    print(f'Максимальное: {maxnumb}')

    summa = list_sum(lst)
    mult = list_mult(lst)

    print(f'Сумма: {summa}')
    print(f'Произведение: {mult}')

def tz3():
    process_all_steps("data.txt")
    time_test_run()


def write_random_file(file_name, size):
    my_list = random.sample(range(1, 1000000), size)
    with open(file_name, 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


def time_test(file_name, size):
    write_random_file(file_name, size)
    t0 = time.time()
    process_all_steps(file_name)
    t1 = time.time()
    print(f'size {size} time {t1-t0} s')

def time_test_run():
    test_file_name = "test.txt"
    time_test(test_file_name, 100)
    time_test(test_file_name, 1000)
    time_test(test_file_name, 10000)
    os.remove(test_file_name)



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


def test_overload():
    file_name = "overload.txt"
    write_random_file(file_name, 100000)
    lst = read_file(file_name)
    os.remove(file_name)
    assert list_mult(lst) == -1




if __name__ == '__main__':
    tz3()
