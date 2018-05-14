# importujemy biblioteki do generacji liczb
import random
import numpy
# jądro
random.seed('kot')
# losujemy 100 liczb z przedzialu (-5, 10)
vector = [random.randint(-5, 10) for x in range(100)]
# wypisz vector
print(vector)

'''skorzystaj z petli for'''
# recznie suma
# inicjalizacja licznika (zmienna o nazwie suma) - ustawiamy na zero
suma = 0
# dla kazdego elementu w vectorze sumuj elementy
for elem in vector:
    suma += elem
print(suma) # wypisz sume
    
sum(vector) # wbudowana funkcja sum

# recznie srednia
# podziel sume przez liczbe elementow vectora (len, czyli dlugosc)
print(suma/len(vector))

#recznie suma kwadratow
# inicjalizacja licznika (zmienna o nazwie suma_kw) - ustawiamy na zero
suma_kw = 0
# dla kazdego elementu w vectorze sumuj kwadraty elementow
for elem in vector:
    suma_kw += elem**2
print(suma_kw)
    
#recznie maksimum

#najpierw tworzymy funkcje z 2 argumentami
def czywieksze(x, y):
    if x >= y: # jezeli x jest wiekszy rowny od y, napisz x
        return x
    else: # w przeciwnym razie y
        return y

#sprawdzenie
liczba = czywieksze(23, 1202)
print(liczba)
max(2334, 234) #wbudowana funkcja max

#i wykorzystanie
poprzednia = vector[0]
for i in range(1, len(vector)-1):
    poprzednia = czywieksze(poprzednia, vector[i])
    
print(poprzednia)
max(vector) #wbudowana funkcja maximum

#recznie minimum
#tworzymy funkcje z 2 argumentami
def czymniejsze(x, y):
    if x >= y: # jezeli x jest wiekszy rowny od y, napisz y
        return y
    else: # w przeciwnym razie x
        return x


#i wykorzystanie
poprzednia = vector[0]
for i in range(1, len(vector)-1):
    poprzednia = czymniejsze(poprzednia, vector[i])
  
print(poprzednia)
min(vector) #wbudowana funkcja minimum

#policz ujemne

#wersja ot taka
# inicjalizacja licznika (zmienna o nazwie ujemne) - ustawiamy na zero
ujemne = 0
# dla kazdego elementu w vectorze - jezeli reszta z dzielenia elementu przez dwa jest rowna zero
for elem in vector:
    if elem % 2 == 0:
        #print(elem)
        ujemne += 1 # ujemne zwiekszaj o jeden

print(ujemne)

 
#wersja ladniejsza
# z uzyciem "list skladanych" tzw.list comprehension
ujemne2 = len([1 for elem in vector if elem < 0]) #PS niektorym nie dzialalo sum(), czy wczesniejszym kodzie zmienna nie byla przypadkiem sum zamiast suma? nie mozna nazw zmiennych nazywac od slow kluczowych jezyka
print(ujemne2)

#zachowaj parzyste

parzyste = [x for x in vector if x%2 == 0]
print(parzyste)

# bonus, jak to dziala
literki = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cyferki = list(range(1, 8 + 1))

szachownica = [(a, b) for a in literki for b in cyferki]
print(szachownica)



















    




