a = int(input())
if a % 400 == 0 or (a % 100 != 0 and a % 4 == 0):
    print('leap')
else:
    print('not leap')