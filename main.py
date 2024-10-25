n=int(input('введите число n: '))
fib1 = 1
fib2 = 1
if n >= 1:
    print(fib1)
if n >= 2:
    print(fib2)
for _ in range(3,n+1):
    fib_next=fib1+fib2
    print(fib_next)
    fib1, fib2 = fib2, fib_next
