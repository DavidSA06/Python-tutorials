def prime_number(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    return False

def run():
    n: int = 0
    while n <= 1:
        n: int = int(input('Escribe un número entero positivo'))
        try:            
            if n < 1:
                raise ValueError("No puedo determinar la primalidad de este número")
            if prime_number(n):
                print("Es primo")
            else:
                print("No es primo")
        except ValueError:
            print ("Debes escribir un número mayor a 0")
        finally:
            print("Instrucción Finally usada, usualmente un 'f.close ()' es implementado")        
    

if __name__ == '__main__':
    run()
    