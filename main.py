import math
#zad1
# potęga = ((5/9) ** 2)
# logarytm = (math.log(23 + math.sin(45))) ** (1/4)
# wynik = potęga + logarytm
# print(round(wynik, 2))

#zad2
# lista = [2,34,22,2,4,2,2,42]
# print(min(lista))
# print(lista.count(min(lista)))

#zad3
# def lista (lista=[2,'a',34,22,'dzialaj',2,4,2,2,'prosze',42]):
#     lista1 = []
#     for i in lista:
#         if type(i) == str:
#             lista1.append(i)
#     return lista1
# print(lista())


#zad4
# try:
#     a = int(input("Podaj a:"))
#     lista = [1, 2, 3, 4]
#     lista1 = []
#     for i in lista:
#         if a > i:
#             lista1.append(i)
# except ValueError:
#     print("To nie jest liczba!")
#
#     print(lista1)
# print("liczb mniejszych jest:", len(lista1))



# zad3.
#Napisz skrypt, w którym utworzysz listę z liczbami całkowitymi, a następnie sprawdzisz czy co drugi element jest parzysty. Wyświetl ilość takich elementów.

# b = 1
# lista = [1, 4, 4, 6, 6, 9, 8, 8]
# for a in lista:
#     if (b % 2 == 0):
#         if (a % 2 == 0):
#             print(a)
#     b += 1




#zad4.
#Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby całkowite a i b. Zadaniem jest utworzenie ciągu liczb od a do b z krokiem równym 2 i podniesieniem każdego elementu do kwadratu. W skrypcie dokonaj sprawdzenia błędów związanych z wczytywaną wartością, do tego celu użyj składni try-except

# a = input('Wpisz')
# b = input('Wpisz')
# try:
#     a = int(a)
#     b = int(b)
#     if(a>b):
#         print("B ma być większe, debilu")
#     for x in range(a, b, 2):
#         x = x ** 2
#         print(x)
# except ValueError:
#     print("Złe dane")






