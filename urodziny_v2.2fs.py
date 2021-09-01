from datetime import datetime
from datetime import timedelta
import json
t=3
actuell=datetime.now()
czas='2022-01-31'
#czasSix='2021-10-27'
nowyCzas = datetime.strptime(czas,"%Y-%m-%d")
nowyCzass = nowyCzas-actuell
try:
    with open('c:/Python/birth.json','r+') as f:
        birth=json.load(f)
except:
    birth={}
print(birth)

print('DZISIEJSZA DATA TO : ', actuell,'\n \n')

'''birth={'Marcin':'1982-04-20',
   'Karola':'1985-06-28',
   'Nadusia':'2012-12-12',
   'Nataszka':'2016-06-29',
   'Magdalena_KADRY&PŁACE':'1977-12-08'}'''
 
print('''

              OBLICZACZ DNI DO NASTEPNYCH URODZIN

MENU:

1 : WYPISZ DATY URODZIN

2 : ILE DNI ZOSTALO DO KOLEJNYCH URODZIN

3 : ILE DNI MA DANA OSOBA

4 : DODAJ OSOBE DO BAZY DANYCH

5 : ILE DNI ZOSTAŁO DO PEWNEJ DATY \n     *funkcja dodatkowa na życzenie zaprzyjaźninego Usera:-)

6 : ILE DNI DO 27 pazdziernika
  
0 : KONIEC PROGRAMU __ WYJSCIE

''')
  
while t!=0:
    wejscie=input('\n WYBIERZ NUMER MENU : ')
    if int(wejscie)==1:
        print('DATY URODZIN : ')
        for x,y in birth.items():
            print(f"{x} ma urodziny dnia : {y}")
    if int(wejscie)==2:
        print('ILE DNI ZOSTALO DO KOLEJNYCH URODZIN')
        for imie,liczba in birth.items():
            newData = datetime.strptime(liczba,"%Y-%m-%d")
            #print(type(newData))
            newData = newData.replace(year=datetime.now().year)
            x=newData-actuell
            if x.days<0:
                print(f'{imie} MA URODZINY ZA {x.days+360}')
            else:
                print(f'{imie} MA URODZINY ZA {x.days}')
    if wejscie=='3':
        print('ILE DNI ZYCIA MAJĄ WPISANE OSOBY :-) \n    *funkcja dodatkowa na życzenie')
        for imie,liczba in birth.items():
            newDatas = datetime.strptime(liczba,"%Y-%m-%d")
            #print(type(newData))
            #newDatas = newDatas.replace(year=datetime.now().year)
            v=actuell-newDatas
            if v.days<0:
                print(f'{imie} MA {v.days+360} DNI ŻYCIA ZA SOBĄ')
            else:
                print(f'{imie} MA {v.days} DNI ŻYCIA ZA SOBĄ')
    if wejscie=='4':
        newPerson=input('PODAJ IMIE NOWEJ OSOBY : ')
        newDatung=input('PODAJ DATE URODZIN NOEWJ OSOBY \nFORMAT PODAWANIA : YYYY-MM-DD : ')
        birth[newPerson]=newDatung
        print('Dodano osobę : ',newPerson,'ktora urodziła się : ',newDatung)
    if wejscie=='5':
        print('DO TEJ PIĘKNEJ DATY ZOSTAŁO JESZCZE ',nowyCzass.days, 'DNI')
    if wejscie=='6':
        print('FUNKCJA W BUDOWIE\nW BUDOWIEDO TEJ DATY ZOSTAŁO CI JESZCZE DNI')

        
    if int(wejscie)==0:
        print('WYBRANO ZAMKNIECIE PROGRAMU')
        with open('c:/Python/birth.json','w+') as f:
            json.dump(birth,f)
        t=0

  

