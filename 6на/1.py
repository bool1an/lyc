d = int(input())
m = int(input())
y = int(input())
m -= 2
if m < 1:
    m = m + 12
    y = y - 1
c = y // 100
y = y % 100
n = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(n)