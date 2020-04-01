# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:55:31 2020

@author: Falcon
"""

# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarını acip inceleyip sonuclaramızı bu dosya tiplerine rahat bir şekilde kayıtedebilir
# 3) pandas for missing data için işimizi kolaylaştırıyor
# 4) reshape yapıp datayı daha etkili bir şekilde kulanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde yardımcı
# 7) her şeyden önemlisi pandas hız açısından optimize edilmiş bir kütüphane

import pandas as pd

dictionary = {"ISIM":["Ali","Veli","Ayse","Kenan","Evran"],
             "YAS":[15,40,25,32,27],
             "MAAS":[2800,6400,2575,1200,4000]}

dataframe1=pd.DataFrame(dictionary)

head=dataframe1.head(3) #ilk 3 veriyi gösterir
tail=dataframe1.tail(3) #son 3 veriyi gösterir

# %% Pandas basic method

print(dataframe1.columns)

print(dataframe1.info())

print(dataframe1.dtypes)

print(dataframe1.describe())

#%% indexing and slicing

dataframe1["yeni_sutun"]=[1,2,3,4,5]
print(dataframe1.YAS)

print(dataframe1["YAS"])

print(dataframe1.loc[:,"YAS"])

print(dataframe1.loc[:3,"YAS"])

print(dataframe1.loc[:3,"YAS":"ISIM"])

print(dataframe1.loc[:,["YAS","ISIM"]])

print(dataframe1.loc[::-1,:])

print(dataframe1.loc[:,:"ISIM"])

print(dataframe1.loc[:,"ISIM"])

print(dataframe1.iloc[:,2])

# %% filtering

filtre1=dataframe1.MAAS>4000
print(filtre1)

filtrelenmis_data=dataframe1[filtre1]

filtre2=dataframe1.YAS<30

dataframe1[filtre1 & filtre2]

print(dataframe1[dataframe1.YAS>20])

# %% List Comprehension
#import numpy as np

ortalama_maas=dataframe1.MAAS.mean() #pandas

#ortalama_maas_np=np.mean(dataframe1.MAAS) #numpy

dataframe1["maas_seiyesi"]=["düşük" if ortalama_maas>each else "yüksek" for each in dataframe1.MAAS]

#for each in dataframe1.MAAS:
#    if(ortalama_maas>each):
#        print("düşük")
#    else:
#       print("yüksek")

dataframe1.columns

dataframe1.columns=[each.lower() for each in dataframe1.columns]

dataframe1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataframe1.columns]

# %% drop and Concatenating

dataframe1.drop(["yeni_sutun"],axis=1,inplace=True) #axis=1(sütun) asix=0(satır), inplace=yap ve uygula

data1=dataframe1.head()
data2=dataframe1.tail()

#vertical
data_concat=pd.concat([data1,data2],axis=0)

#horizontal
maas=dataframe1.maas
yas=dataframe1.yas

data_h_concat=pd.concat([maas,yas],axis=1)

# %% Transforming Data

dataframe1["list_comp"]=[each*2 for each in dataframe1.yas]

# Apply ()

def multiply(yas):
    return yas*2
dataframe1["apply_metodu"]=dataframe1.yas.apply(multiply)
