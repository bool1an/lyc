n = int(input())
c = True
for i in range(n):
    th_ls = []
    th_c = input().split()
    if len(th_c) % 2 == 0:
        for j in range(int(len(th_c) / 2)):
            if int(th_c[j]) + int(th_c[-1 - j]) >= int(th_c[j + 1]) + int(th_c[-2 - j]):
                th_ls.append(th_c[j])
                th_ls.append(th_c[-1 - j])
            else:
                c = False
    else:
        for j in range(int(len(th_c) // 2) + 1):
            if j == int(len(th_c) // 2):
                if int(th_c[j]) <= int(th_c[j + 1]) + int(th_c[j - 1]):
                    th_ls.append(th_c[j])
                else:
                    c = False
            else:
                if int(th_c[j]) + int(th_c[-1 - j]) >= int(th_c[j + 1]) + int(th_c[-2 - j]):
                    th_ls.append(th_c[j])
                    th_ls.append(th_c[-1 - j])
                else:
                    c = False
    if not c:
        print('НЕТ')
    else:
        for j in th_ls:
            print(j, end=' ')
