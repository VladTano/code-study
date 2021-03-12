def IntToBinaryRepresentation(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x >>= 1
    return n

x = int(input("Enter the base-10 positive integer number\n"))
print("Custom function: " + IntToBinaryRepresentation(x))
print("Built-in function: " + bin(x)[2:])
