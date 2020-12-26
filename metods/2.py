stack = []
a = 0
n = input().split()
for i in range(len(n)):
    if len(n[i]) > 1:
        stack.append(int((n[i])[1]) * -1)
    elif n[i].isdigit():
        stack.append(int(n[i]))
    else:
        if n[i] == '/':
            a1 = stack.pop()
            a2 = stack.pop()
            a = a1 / a2
        elif n[i] == '-':
            a1 = stack.pop()
            a2 = stack.pop()
            a = a2 - a1
        elif n[i] == '+':
            a = stack.pop() + stack.pop()
        elif n[i] == '*':
            a = stack.pop() * stack.pop()
        stack.append(a)
print(stack[0])
