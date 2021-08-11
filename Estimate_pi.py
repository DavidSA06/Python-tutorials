import random
import math

def point(radius = 1):
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    return (x, y)

def distance(x, y):
    return (x**2 + y**2)**.5

def condition(distance):
    return distance <= 1

 

def question():
    iterations = 0
    while iterations <= 0:
        iterations = input("How many iterations do you want?")
        try:
            iterations = int(iterations)
            if iterations <= 0:
                print("Choose a positive integer")
            else:
                print("Very well")
        except:
            print("That is not a number")
            iterations = 0
    sum = 0

    for i in range(iterations):
        (x, y) = point()
        if condition(distance(x, y)):
            sum += 1
    average = 4. * sum/iterations
    print(average)

if __name__ == "__main__":
        question()
