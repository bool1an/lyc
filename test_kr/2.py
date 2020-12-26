step = int(input())
start = int(input())
end = int(input())
d_ch = int(input())
if start > end:
    step *= -1
    end -= 2
for i in range(start, end + 1, step):
    if i % (d_ch * 3) != 0:
        print(i)