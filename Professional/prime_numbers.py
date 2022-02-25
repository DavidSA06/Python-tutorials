def prime_number(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    return False

def run():
    n: int = int(input('Write a number'))
    if prime_number(n):
        print("It is prime")
    else:
        print("It is not prime")

if __name__ == '__main__':
    run()