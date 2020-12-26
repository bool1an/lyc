n = int(input())
un_set = set()
for i in range(n):
    th_set = set()
    k = int(input())
    for j in range(k):
        th_set.add(input())
    if i == 0:
        un_set = th_set.copy()
    un_set = un_set.intersection(th_set)
for i in un_set:
    print(i)