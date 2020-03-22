# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:09:24 2020

@author: Falcon
"""
#%%
#variable

var1=10 #integer
var2=40

gun="cuma" #string

var3=10.27 #double(float)
# 5var=19 hata verir
#%%

#string

s="bugun gunlerden pazartesi"

variable_type= type(s) 

print(s)

var1="ankara"
var2="ist"
var3=var1+var2

var4="100"
var5="200"
var6=var4+var5

uzunluk= len(6)
#%%
#numbers
#int
integer_deneme=-50

#double=float=ondalikli sayi
float_deneme=-30.95
#%%
#Built-in fuction
#int(str2)
#float(str2)
#round(str2)
str2="10"
int(str2)
type(str2)
#%%
#User defined functions

var1=20
var2=15

out=((var1+var2)*50)/40

def ilk_fonkison(var1,var2):
    """
    parametre=
    return=
    """
    output=((var1+var2)*50)/40
    return output
    
#%%
#default flexible function

#default    
def cember_cevre_hesap(r):
    """
    cember cevresi hesaplama
    input(parametre)=r
    output=cemberin cevresi
    """
    output=2*3.14*r
    return output

#flexible

def hesapla(yas,boy,*args):
    print(args)
    output=yas+boy
    return output

#%%Lambda Function
    
def hesapla(x):
    output=x*x
    return output

sonuc=hesapla(3)

sonuc2=lambda x: x*x
print(sonuc2(4))
    
