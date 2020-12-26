f_st = input().split()
s_st = input().upper().split('-L-')
t_st = input().split('>W<')
for i in f_st:
    pr_ls = []
    pr_lst = []
    for j in s_st:
        for s in list(j):
            if s in i.upper() and len(set(j)) >= 3:
                pr_ls.append(j)
                break
    for u in t_st:
        if u.islower() and len(u) <= len(i):
            pr_lst.append(u)
    print(f'''{i}:
    {'; '.join(pr_ls)}
    {' * '.join(pr_lst)}
    ''', end='')

