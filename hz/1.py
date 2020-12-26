n = input().split()
count = 0
for i in n:
    if i != ' ' and i != '' and i != '\t':
        count += 1
print(count)