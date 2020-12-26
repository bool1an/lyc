s = 0
n = -1
wh = int(input())
while s < wh:
    n += 1
    s = 2 ** n
if s == wh:
    print(n)
else:
    print('НЕТ')