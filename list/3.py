ls = []
ls_d = []
count = 0
f_s = input().split()
for i in range(int(f_s[0])):
    ls.append(input())
for i in range(len(ls)):
    th_ls = ls[i].split()
    th_c = int(th_ls[0])
    th_n = int(th_ls[1].replace('*', ''))
    th_s = th_c * th_n
    count += th_s
    if th_s != int(th_ls[2].replace('=', '')):
        ls_d.append(i)
if abs(count - int(f_s[1])) != 0:
    print(int(f_s[1]) - count)
    for i in ls_d:
        print(i + 1, end=' ')
else:
    print(0)
