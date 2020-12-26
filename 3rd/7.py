a = input()
max_a = 0
min_a = 10
i_min = -1
a_l = 0
i_max = -1
for i in range(3):
    if int(a[i]) > max_a:
        max_a = int(a[i])
        i_max = i
    if int(a[i]) < min_a:
        min_a = int(a[i])
        i_min = i
sym = (max_a + min_a) / 2
for i in range(3):
    if i != i_min and i != i_max:
        a_l = int(a[i])
if a_l == sym:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
