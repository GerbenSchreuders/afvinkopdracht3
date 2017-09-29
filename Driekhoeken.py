a = int(input('geef grote driehoek 1: '))
b = int(input('geef grote driehoek 2: '))

if a > b:
    print('driehoek 1 is groter dan driehoek 2')
elif b > a:
    print('driehoek 2 is groter dan driehoek 1')
elif a == b:
    print('de driehoeken zijn allebei even groot')
