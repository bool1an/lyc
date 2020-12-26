n = float(input())
i = 0
t = 0
while n >= -300:
    t += n
    i += 1
    n = float(input())
print(t / i)