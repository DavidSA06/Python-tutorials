def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Write a number: ")
    assert num.isnumeric() and num > 0, "You must write an integer number greater than 0"
    print(divisors(int(num)))
    print("Program finished")

if __name__ == "__main__":
    run()