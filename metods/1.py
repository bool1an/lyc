alp_eng = 'abcdefghijklmnopqrstuvwxyz'
alp_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
lst = list(input().lower())
s = ''
max_s = 0
for i in lst:
    if i == ' ':
        continue
    if lst.count(i) > max_s:
        max_s = lst.count(i)
        s = i
    elif lst.count(i) == max_s:
        if i in alp_ru:
            if alp_ru.find(i) >= alp_ru.find(s):
                s = s
            else:
                s = i
        elif i in alp_eng:
            if alp_eng.find(i) >= alp_eng.find(s):
                s = s
            else:
                s = i
print(s)