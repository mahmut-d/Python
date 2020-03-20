# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:39:57 2020

@author: Falcon
"""
#%%liste
liste=[1,2,3,4,5]
type(liste)

liste_str=["elma","kiraz","cilek"]
type(liste_str)

value=liste[1]
print(value)

last_value=liste[-1]

liste_divide=liste[0:3]

liste.append(7)#append=listenin sonuna parantez içindeki elamaı ekler
liste.remove(7)#remove=listeden  parantez içindeki elamaı çıkarır
liste.reverse()#reverse=listeyi revize eder

liste2=[1,5,9,4,6,1,2]
liste2.sort()#sort=listeyi sıralar

str_int_liste=[1,3,5,"elma","kiraz"]

#%%Tuple

t=(1,2,3,4,5)
dir(tuple)#dir=kulanım araçlarını gösterir
help(tuple.count)#help=yardım
t.count(3)#tuple'da kaç tane 3 var?
t.index(5)#tuple'da '5' kaçıncı sırada? 

#%%Dictionary

dictionary={"ali":34,"veli":24,"aysel":19}
#ali,veli,aysel = keys
#34,24,19 = values
def deneme():
    dictionary={"ali":34,"veli":24,"aysel":19}
    return dictionary

dic=deneme()