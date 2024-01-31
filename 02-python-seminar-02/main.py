# найти факториал числа N
N = 5
result = 1
while N > 0:
    result = result * N
    N -= 1
print(result)

# Каким по счёту числом Фибоначчи является число N, если не является, то вывести -1
f0 = 0
f1 = 1
fib = 1
N = 6
count = 1
while (fib < N):
    fib = f0 + f1
    f0 = f1
    f1 = fib
    count += 1
print(fib)
if fib == N:
    print(count)
else:
    print(-1)
