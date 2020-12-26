login = input()
mail = input()
if not ('@' in login) and ('@' in mail):
    print('OK')
elif not ('@' in mail):
    print('Некорректный адрес')
elif '@' in login:
    print('Неккоректный логин')
