n = int(input())
c = True
ans_ls = []
for k in range(n):
    min_c = 100
    cubs = [int(i) for i in input().split()]
    if len(cubs) % 2 == 0:
        l_cub = cubs[:len(cubs) // 2].copy()
        r_cub = cubs[:len(cubs) // 2 + 1:-1].copy()
        min_c = min(l_cub[0], r_cub[0])
        ans_ls.append(l_cub[0])
        ans_ls.append(r_cub[0])
        for i in range(1, len(l_cub)):
            if min_c < max(l_cub[i], r_cub[i]):
                c = False
                break
            else:
                min_c = min(l_cub[i], r_cub[i])
                ans_ls.append(l_cub[i])
                ans_ls.append(r_cub[i])
    else:
        l_cub = cubs[:len(cubs) // 2].copy()
        r_cub = cubs[:len(cubs) // 2:-1].copy()
        center = int(cubs[len(cubs) // 2])
        ans_ls.append(l_cub[0])
        ans_ls.append(r_cub[0])
        for i in range(1, len(l_cub)):
            if min_c < max(l_cub[i], r_cub[i]):
                c = False
                break
            else:
                min_c = min(l_cub[i], r_cub[i])
                ans_ls.append(l_cub[i])
                ans_ls.append(r_cub[i])
        if center > ans_ls[-1]:
            c = False
        else:
            ans_ls.append(center)
    if not c:
        print('НЕТ')
    else:
        for i in ans_ls:
            print(i, end=' ')
    print('\n', end='')
