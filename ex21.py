def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's o some math with functions!")

age = add(20, 7)
height = subtract(180, 7)
weight = multiply(20, 4)
iq = divide(450, 3)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")