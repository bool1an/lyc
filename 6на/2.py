count = int(input())
n = 0
while count != 1:
    if count % 2 == 0:
        count //= 2
        n += 1
    else:
        count -= 1
        n += 1
print(n)