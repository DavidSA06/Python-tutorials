def factorial(n):
    f = 1
    for i in range(n):
        f *= i + 1
    return f
        
if __name__ == "__main__":
    number = int(input("Write a number"))
    f = factorial(number)
    print(f)