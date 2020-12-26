h_int = int(input())
s_int = int(input())
h_set = set()
s = set()
for i in range(h_int):
    h_set.add(input())
for i in range(s_int):
    if input() in h_set:
        print('YES')
    else:
        print('NO')


