a = input()
sum_l = int(a[2]) + int(a[1])
sum_h = int(a[0]) + int(a[1])
if sum_h > sum_l:
    ans = str(sum_h) + str(sum_l)
else:
    ans = str(sum_l) + str(sum_h)
print(ans)