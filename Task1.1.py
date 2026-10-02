""" #Task 1.1
crazyFunction = lambda x, y: x * y
meaningOfLife = crazyFunction(6, 7)
print(meaningOfLife)

#The code creates a lambda function that multiplies two numbers. When we call `crazyFunction(6, 7)`, it calculates `6 * 7`, which equals `42`. The result is stored in `meaningOfLife` and then printed on the screen. """

#Task 1.2
animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]

sortedAnimals = sorted(animalsCounts, key=lambda animal: animal[1])

print()
print("Task 1.2")
print(sortedAnimals)

#Task 1.3
""" list(filter(lambda x: x > 10, [3.14, 101, 42, 666, -1]))

#The `filter()` function keeps only the numbers greater than 10. The lambda function checks each number, so the output is `[101, 42, 666]`. """

#Task 1.4
""" [*enumerate([42, 3, 4, 18, 3, 10])]

#It will show the index and the value. """

#Task 1.5
def check_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(check_even, numbers))

print()
print("Task 1.5")
print(even_numbers)

#Task 1.6
fruits = ['apple', 'banana', 'kiwi', 'pear']

result = list(filter(lambda word: len(word) <= 4, fruits))

print()
print("Task 1.6")
print(result)

#Task 1.7
temperatures = [-10, 0, 17.6, 28, 100]

fahrenheit = list(map(lambda c: c * 9/5 + 32, temperatures))

print()
print("Task 1.7")
print(fahrenheit)

#Task 1.8
first_names = ["Jackie", "Chuck", "Arnold", "Sylvester"]
last_names = ["Stallone", "Schwarzenegger", "Norris", "Chan"]
magic = [*zip(first_names, last_names[::-1])]
print()
print("Task 1.8")
print(magic[0])
print(magic[1][0])
print(magic[1][1])

#The code reverses the `last_names` list and uses `zip()` to combine it with the `first_names` list. The `*` unpacks the pairs into the `magic` list. The `print()` statements then access specific names and surnames from the list.

#Task 1.8 SUM
def my_sum(*args):
    try:
        result = sum(args)
        print(result)
    except TypeError:
        raise ValueError("Arguments must be numbers")


print()

print("Task 1.8")

my_sum(1)
my_sum(1, 2, 3)
my_sum(-20, -10, 5, 5, 10, 10)

try:
    my_sum(1, "toto")
except ValueError as error:
    print(error)

#Task 1.9
def my_division(a, b):
    try:
        quotient = a // b
        remainder = a % b
        return quotient, remainder
    except ZeroDivisionError:
        print("Error: division by zero")


print()
print("Task 1.9")
print(my_division(42, 4))

#Task 1.10
def my_count(stop, start=0):
    for number in range(start, stop + 1):
        print(number)


my_count(5)

#task1.11
def my_count(stop, start=0, step=1):
    if not isinstance(stop, int) or not isinstance(start, int) or not isinstance(step, int):
        print("Error: arguments must be integers")
        return

    if step == 0:
        print("Error: step cannot be 0")
        return

    if step > 0 and stop < start:
        print("Error: stop must be greater than start")
        return

    if step < 0 and stop > start:
        print("Error: stop must be smaller than start")
        return

    for number in range(start, stop, step):
        print()
        print("Task 1.11")
        print(number)

#Task 1.12
def new_division(num, den, acc=1):
    result = num / den
    print()
    print("Task 1.12")
    print(f"{result:.{acc}f}")


new_division(8.4, 13)
new_division(8.4, 13, 6)

#Task 1.13
def ship(*args, **kwargs):
    print()
    print("Task 1.12")
    for name in args:
        print(name)

    for key, value in kwargs.items():
        print(key + ":", value)


ship("Batman", street="Mountain Drive", city="Gotham")

ship(
    "Superman",
    "The man of steel",
    apartment="3D",
    num=344,
    street="Clinton Street",
    city="Metropolis"
)

