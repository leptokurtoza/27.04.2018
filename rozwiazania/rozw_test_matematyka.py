'''Przygotuj test z tabliczki mnozenia dla dzieci, niech automatycznie na koniec podlicza punkty, 
przykladow ma byc 10, liczby od 1 do 10.
'''
# importujemy biblioteke random do losowania 
import random
# inicjalizujemy licznik do sumowania punktow. Zaczynamy liczyc od zera
punkty = 0
for i in range(10):
    # losujemy liczbe z przedzialu od 1 do 10 dwukrotnie i przypisujemy je do zmiennych a i b
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    # uzytkownik musi podac wynik mnozenia dwoch liczb. %s oznaczania formatowanie łańcucha znaku
    # tzn. w miejsce %s najpierw wstaw a, a potem b
    # odpowiedz przypisz do zmniennej o nazwie odp
    odp = input('%s x %s = ' %(a, b))
    # rzutujemy odpowiedz (ktora jest stringiem) na integer. 
    # Jezeli odpowiedz rowna sie wynikowi mnozenia a i b, to napisz 'dobrze'
    if int(odp) == a*b:
        print('dobrze')
        punkty += 1 # sumuj liczbe punktow za prawidlowo odzielone odpowiedzi
    else:
        print('zle') # w przeciwnym wypadku napisz 'zle'
        
print('punkty:')
print(punkty) # wypisz liczbe uzyskanych punktow
