f_w = list(input())
l_w = []
s_in_w = True
ans = 0
n = int(input())
for i in range(n):
    l_w.append(input())
for i in range(n):
    s_in_w = True
    f_w_c = f_w.copy()
    l_e = list(l_w[i])
    for j in l_e:
        if j not in f_w_c:
            s_in_w = False
        else:
            f_w_c.remove(j)
    if s_in_w:
        ans += len(l_e)
print(ans)
