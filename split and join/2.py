n = int(input())
ls = []
for i in range(n):
    k = input()
    if 'лук' not in k:
        ls.append(k)
print(', '.join(ls))