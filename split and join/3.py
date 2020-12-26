lis = []
a = input()
while a != '':
    lis.append(a.split(':'))
    a = input()
paswrds = input().split(';')
for i in lis:
    if i[1] in paswrds:
        print('To: ', i[0], '\n', (i[4].split(','))[0] + ', ', 'ваш пароль слишком простой, смените его.', sep='')
