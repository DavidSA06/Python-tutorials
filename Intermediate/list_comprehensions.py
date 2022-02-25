def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1,101) if i % 3 != 0]

    # print(squares)

    list = [i**2 for i in range(1,101) if i**2 % 4 == 0 and i**2 % 6 == 0 and i**2 % 9 == 0 and i**2 < 10000]
    print (list)


if __name__ == '__main__':
    run()