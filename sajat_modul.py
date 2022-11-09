def negyzet(szam):
    return szam*szam

szam=int(input('Kérek egy számot amit négyzetre fogunk emelni: '))
print('A szám négyzete: ', negyzet(szam))

def has(szam):
    if szam < 100:
        print('A számod kisebb mint 10')
    else:
        print('A számod nagyobb vagy egyenlő 10 el')
has(negyzet(szam))