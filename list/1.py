n = int(input())
wh_lst = []
for i in range(n):
    wh_lst.append(input())
k = int(input())
srh = []
for i in range(k):
    srh.append(input())
for i in srh:
    if i in wh_lst:
        print(i)