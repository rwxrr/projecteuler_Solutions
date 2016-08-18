"""
EN
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

TR
3'ün veya 5'in katı olan 10'dan küçük tüm doğal sayıları listelersek, 3, 5, 6, ve 9'u elde ederiz. Bu katların toplamı 23'tür.

3'ün veya 5'in 1000'den küçük tüm katlarının toplamını bulunuz.

"""



#!/usr/bin/python 

liste=[]
top=0
for i in range(0,1000):
    if i%3==0 or i%5==0:
        liste.append(i)

for i in liste:
    top+=int(i)

print top


