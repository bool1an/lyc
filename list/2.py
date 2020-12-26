n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
ans = []
for i in range(len(ls) - 1):
    ans.append(ls[i] + ls[i + 1])
for i in ans:
    print(i)