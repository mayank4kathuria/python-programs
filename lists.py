print("Hello world from file!!")

print("4 + 3 equals ", 4+3)


# program for getting fibonacci sequence

fib_len = int(input("Enter the Number of Fib seq need: "))
a, b = 0, 1

for i in range(fib_len):
    print(a)
    a, b = b, a+b
