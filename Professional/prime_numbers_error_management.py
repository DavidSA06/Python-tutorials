def prime_number(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    return False

def run():
    n: int = 0
    while n <= 1:
        n: int = int(input('Write a positive integer'))
        try:            
            if n < 1:
                raise ValueError("I cannot determine the primality of this number")
            if prime_number(n):
                print("It is a prime number")
            else:
                print("It is not a prime number")
        except ValueError:
            print ("You must write a number greater than 0")
        finally:
            print("'finally' instruction used, usually a 'f.close ()' is implemented")        
    

if __name__ == '__main__':
    run()
    