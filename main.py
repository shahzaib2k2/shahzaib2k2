# Prime Number
x = int(input("Enter value for x\n"))
f = False
for i in range(2, x, 1):
    if x % i == 0:
        f = True
if f:
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")
