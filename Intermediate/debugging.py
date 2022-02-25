def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Write a number: "))
        if num < 1:
            raise ValueError("Cannot get divisors from this number")
        print(divisors(num))
        print("Program finished")
    except ValueError:
        print ("You must write an integer number greater than 0")
    finally:
        print("Finally instruction used, usually an 'f.close ()' is implemented")


if __name__ == "__main__":
    run()