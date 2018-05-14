'''Popraw błędy i uruchom program.
                                    Powodzenia:) '''

# błędy, znajdź i popraw

len('abrakadabra')

print(1235 + 4)
# lub
print('1235' + '4')

slownik = {'a': 'pierwszy', 'b':'drugi'}

nazwa1 = 'mojanazwa'

krotka = [2, 4 ,9]
krotka[1] = 3 #to juz jest lista!

moja_lista = ['cos', 'kot', 1, 2]
moja_lista[3]

#inicjalizacja licznika
x = 1
while x < 10:    
    print('wiekszy')
    #zwiekszanie licznika o jeden
    x += 1

# == to znak rownosci ('czy rowne?')   
if 4 == 5-1:
    print('etwas')


#ZeroDivisionError     
        
# funkcja z 2 argumentami x i y o nazwie "moja_funkcja"
def moja_funkcja(x, y):
   try:
        print(0.8*x/(y-2)) # spróbuj wykonać kod
   except ZeroDivisionError: # przechwycenie wyjątku typu ZeroDivisionError  
        print('nie dziel przez 0')
    

moja_funkcja(16, 23)
moja_funkcja(16, 2)
moja_funkcja(16, '8')


#kiedy wydaje się, że wszystko jest ok
# funkcja na pierwiastkowanie z argumentem x
def pierwiastkowanie(x): #uwaga, mamy być w zbiorze liczb rzeczywistych
    if x >= 0: # jezeli x wieksze rowne od zera
        print(x**(1/2)) # to wyciagnij pierwiastek z liczby x
    else: # w przeciwnym wypadku
        print('nie rzeczywiste') # napisz nie rzeczywiste

pierwiastkowanie(64)
pierwiastkowanie(-10)
# czy to chcieliśmy osiagnąć?

# funkcja o nazwie "witanie" z argumentem "imie"
def witanie(imie):
    try:
        print('Hej' + imie) # spróbuj wykonać kod, czyli napisac "Hej" + imie
    except TypeError: # przechwycenie wyjątku typu TypeError, 
        #czyli jak nie poda sie argumentu typu String, to niech wypisze 'musisz podac imie'
        print('musisz podac imie')

witanie('Asia')
witanie(23)



