'''Napisz program, ktory prosi o wpisanie pinu, az do skutku'''

#wprowadzenie
# zapytaj uzytkownika 'Wolisz szopy czy koty?' 
# i przypisz jego odpowiedz do zmiennej o nazwie zwierze
zwierze = input('Wolisz szopy czy koty? \n')

#+jesli szopy, to ja tez!
# jezeli uzytkownik odpowie 'szopy', napisz 'ja tez'
if zwierze == 'szopy':
    print('ja tez')
else: # w przeciwnym wypadku
    # %s oznaczania formatowanie łańcucha znaku
    # tzn. w miejsce s wstaw zwierze, ktore wybral uzytkownik
    print('Powiedziałeś, że wolisz %s' %zwierze)
  
#zadanie
# niech pin to 1234
pin = '1234'
# zapytaj uzytkownika 'Podaj swoj pin:'
# i przypisz jego odpowiedz do zmiennej o nazwie user_pin
user_pin = input('Podaj swoj pin: ')
# dopóki odpowiedz uzytkownika (czyli user_pin) jest inna 
# od podanego pinu (1234), to pisz 'Pin nieprawidłowy. Podaj poprawny: '
while pin != user_pin:
    user_pin = input('Pin nieprawidłowy. Podaj poprawny: ')
# w przeciwnym wypadku (tzn.kiedy uzytkownik poda w koncu 1234), napisz 'Jestes zalogowany'    
print('Jestes zalogowany')