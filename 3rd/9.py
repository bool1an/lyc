a = int(input())
a1 = a // 1000
a2 = a // 100 % 10
a3 = a // 10 % 10
a4 = a % 10
min_a = 10000
d={'1':a1, '2':a2, '3':a3, '4':a4}
i1 = min(d, d=d.get)
i4 = max(d, d=d.get)
