count1 = float(input())
count2 = float(input())
string = input()
if string == '+':
    print(count1 + count2)
elif string == '-':
    print(count1 - count2)
elif string == '*':
    print(count1 * count2)
elif string == '/':
    if count2 == 0:
        print(888888)
    else:
        print(count1 / count2)
else:
    print(888888)
