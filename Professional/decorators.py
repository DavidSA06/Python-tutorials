from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):    #*positional arguments,*named arguments
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time =datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds had passed")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

@execution_time
def greeting(nombre = "Cesar"):
    print("Hola " + nombre)

random_func()
sum(5, 5)
greeting("David")