number = int(input())
f1 = number // 1000
f2 = number % 1000 // 100
f3 = number % 1000 % 100 // 10
f4 = number % 1000 % 100 % 10
if f4 > f3:
    f4, f3 = f3, f4
if f3 > f2:
    f3, f2 = f2, f3
if f2 > f1:
    f2, f1 = f1, f2
if f4 > f3:
    f4, f3 = f3, f4
if f3 > f2:
    f3, f2 = f2, f3
if f4 > f3:
    f4, f3 = f3, f4
if f4 == 0 and f3:
    f4, f3 = f3, f4
elif f4 == 0 and f2:
    f4, f2 = f2, f4
elif f4 == 0 and f1:
    f4, f1 = f1, f4
print(f1 + 10 * (f2 + 10 * (f3 + 10 * f4)))