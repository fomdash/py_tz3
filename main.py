# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def read_file():
    data = []
    with open("data.txt") as f:
        for line in f:
            line_list = [int(x) for x in line.split(' ')]
            data.extend(line_list)
    return data

def list_sum(list):
    summa = 0
    for a in list:
        summa = summa + a

    return summa


def list_mult(list):
    mult = 1
    for a in list:
        mult = mult * a

    return mult

def tz3():

    list = read_file()
    print(list)


    minnumb = min(list)
    print(f'min: {minnumb}')

    maxnumb = max(list)
    print(f'max: {maxnumb}')

    summa = list_sum(list)
    mult = list_mult(list)

    print(f'summa: {summa}')
    print(f'mult: {mult}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tz3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
