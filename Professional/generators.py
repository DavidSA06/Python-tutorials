import time

def fibo_gen(max = None):
    n1: int = 0
    n2: int = 1
    counter: int = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if max == None or aux <= max:
                yield aux
            else:
                break

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(.25)