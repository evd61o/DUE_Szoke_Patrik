import string

szoveg = input('Kérek egy szöveget: ')

def kiertekeles(szoveg):
    szamok = 0
    betuk = 0
    specialis_karakterek = 0
    for item in range(len(szoveg)):
        if szoveg[item].isnumeric():
            szamok+= 1
        elif szoveg[item].isalpha():
            betuk+= 1
        else:
            specialis_karakterek+= 1
    print('Szövegben lévő számok darabszáma: ', szamok)
    print('Szövegben lévő betűk darabszáma: ', betuk)
    print('Szövegben lévő speciális karakterek darabszáma: ', specialis_karakterek)

kiertekeles(szoveg)