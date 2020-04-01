# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:52:33 2020

@author: Falcon
"""

# matplotlib kutuphanesi
# gorsellestime kotuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df=pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique)

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

# %% 

import matplotlib.pyplot as plt

df1=df.drop(["Id"],axis=1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id ,setosa.PetalLengthCm, color="red",label="setosa-PetalLengthCm")
plt.plot(versicolor.Id ,versicolor.PetalLengthCm, color="green",label="setosa-PetalLengthCm")
plt.plot(virginica.Id ,virginica.PetalLengthCm, color="blue",label="setosa-PetalLengthCm")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid=True,linestyle=":",alpha=0.5) #alpha=saydamlık ayarı
plt.show()
