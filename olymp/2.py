n = [str(int(i) + 1) if i != '9' else 0 for i in list(input())]
m = int(input())
ans = []
for i in n:
    if i != 0:
        ans.append(i)
print(''.join(ans.reverse()))


