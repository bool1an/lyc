print('Вы находитесь в пещере на развилке. Вы можете выбрать тоннель 1, 2 или 3.'
      '\nВведите номер тоннеля для выбора. ')
choice = input()
print(f'Вы выбрали тоннель №{choice}.', end='')
if choice == '1':
    print('Вы смогли выбраться из пещеры.')
elif choice == '2':
    print('Вы попали в комнату с двумя другими тоннелями, какой вы выберете? У вас есть выбор между 1 и 2.')
    choice = input()
    if choice == '1':
        print('Вы выбрались из пещеры.')
    else:
        print('Там была пропасть и темнота, вы споткнулись и упали. '
              '\nGAME OVER')
elif choice == '3':
    print('Это единственное место, где смог выжить тиронозавр. Он был голодным и поэтому съел вас. '
          '\nGAME OVER')