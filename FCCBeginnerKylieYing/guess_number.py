import random


def guess(x):
    print(f'Guess a number between 0 and {x}')
    rnum = random.randint(1, x)

    while True:
        a = int(input('Try: '))
        if a < rnum:
            print('Low')
        elif a > rnum:
            print('High')
        else:
            print('Good job!')
            break


if __name__ == '__main__':
    x = int(input('Numbers from 0  to: '))
    guess(x)
