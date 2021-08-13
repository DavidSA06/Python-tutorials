def question():
    iterations = 0
    while iterations <= 2:
        iterations = input("How big do you want the list?")
        try:
            iterations = int(iterations)
            if iterations <= 2:
                print("Choose an integer greater than 2")
            else:
                print("Very well")
        except:
            print("That is not a number greater than 2")
            iterations = 0


    fib = [0, 1]
    for i in range(iterations - 2):
        fib.append(fib[i] + fib[i + 1])
    print(fib)


if __name__ == "__main__":
    question()