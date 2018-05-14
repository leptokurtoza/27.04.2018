# importujemy biblioteki json i random i os
import json
import random
import os 
os.chdir('C:\\Users\\Ola\\Desktop\\PULPIT\\Oli\\Python')
# Aby otworzyć plik należy skorzystać z metody open(plik, tryb), w której podajemy jako argument pierwszy ścieżkę do pliku, a jako drugi sposób, w jaki plik ma być otworzony -> r (read) - tryb tylko do odczytu
# obiekt ten (otwarty plik) typu json przypisujemy do zmiennej o nazwie file
file = open('rody.json', 'r', encoding='cp1250')
# obiekt file z JSON konwertujemy do obiektu Python (bedzie w postaci slownika)
# i przypisujemy do zmiennej o nazwie rody
rody = json.load(file)

print(rody)

# wyciaganie kluczy i wartosci ze slownika (tutaj ze zmiennej o nazwie rody) 
# liste kluczy przypisujemy do zmiennej o nazwie klucze
klucze = list(rody.keys())
# liste wartosci przypisujemy do zmiennej o nazwie motto
motto = list(rody.values())

#kto ma najdluzsze zawolanie?
print(motto)
# liczymy dlugosci (len) zawolan
dlugosci = [len(zaw) for zaw in motto]
# sprawdzamy, ktore zawolanie jest najdluzsze
najdl = motto[dlugosci.index(max(dlugosci))]
print(najdl)


# quiz z dopasowywaniem odpowiedzi 'tak' 'nie'
# podliczanie puktow
# inicjalizacja liczby punktow. Zaczynamy od trzech
punkty = 3
for i in range(3):
    # wybierz losowo klucz z listy i wartosc i przypisz je do zmiennych o nazwach odpowiednio: wklucz i wmotto
    wklucz = random.choice(klucze)
    wmotto = random.choice(motto)
    # zapytaj uzytkownika. %s oznaczania formatowanie łańcucha znaku
    # tzn. w miejsce %s wstaw najpierw wmotto (wybraną losowo wartosc), potem wklucz (wybrany losowo klucz)
    # odpowiedz przypisz do zmniennej o nazwie odp
    odp = input('czy %s jest zawolaniem %s ?\n' % (wmotto, wklucz))
    # jezeli wartosc ze slownika rody rowna sie (wartosci) wmotto i odpowiedz uzytkownika jest 'tak', napisz 'dobrze'
    if rody[wklucz] == wmotto and odp == 'tak':
        print('dobrze')
    # jezeli wartosc ze slownika rody jest rozna od wmotto odpowiedz uzytkownika jest 'nie', napisz 'dobrze'
    elif rody[wklucz] != wmotto and odp == 'nie':
        print('dobrze')
    else:
        print('zle') # w przeciwnim razie napisz 'zle'
        punkty -= 1 # i zmniejszaj liczbe punktow o jeden
print(punkty) # wypisz liczbe uzyskanych punktow
    
    



    