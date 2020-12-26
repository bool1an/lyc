n = int(input())
ch = int(input())
while ch <= 999:
    print(f'Похоже на великана {ch % (n * 10)}?')
    ch = int(input())