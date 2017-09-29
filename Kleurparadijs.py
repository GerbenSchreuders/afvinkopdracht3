getal = int(input('geef een nummer: '))

if getal in range(0,37):
        print('geldig getal')
        if getal == 0:
            print('kleur is groen')
        elif getal%2 == 0:
            if getal in range(11,19) or getal in range(29,37):
                print('kleur is rood')
            else:
                print('kleur is zwart')
