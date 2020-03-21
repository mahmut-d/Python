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

#%%Conditionals
#if else statement

var1=10
var2=20

if(var1>var2):
    print("var1 buyuktur")
elif(var1==var2):
    print("essitirler")
else:
    print("var2 buyuktur")
    
liste=[1,2,3,4,5]

value=3
if value in liste:
    print("evet {} degeri liste içiresinde".format(value))
else:
    print("hayir")

keys = dictionary.keys()
if "ali" in keys:
    print("evet")
else:
    print("hayir")
    
#%% 
#metot yazın
#input=int yıllar
#output=int yuzyıl

def year2century(year):
    str_year=str(year)  
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100,200,300,800
            return int(str_year[0])
        else:                   #120,650,820
            return int(str_year[0])+1 
    else:
        if(str_year[2:4]=="00"):#1700,1400,1300
            return int(str_year[:2])
        else:                    #1520,1780,1488
            return int(str_year[:2])+1

year2century(2005)

#%%loop

for each in range(1,11):
    print(each)
    
for mem in "ankara istanbul":
    print(mem)

for mem in "ankara istanbul".split():
    print(mem)
    
liste=[1,2,3,8,14,16,54]
    

print(sum(liste))

count=0
for top in liste:
    count = count + top
print(count)
