# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:08:18 2021

@author: doguilmak

dataset: Created by myself. Totally random values.

Introduction to Association Rules Analysis with Python (Turkish)
https://www.veribilimiokulu.com/python-ile-birliktelik-kurallari-analizi-association-rules-analysis-with-python/

"""
#%%

import pandas as pd

#%%

#  Data Preprocessing

# Reading file
df = pd.read_csv('pocket.csv')
print(df.head(10))
print("\n", df.describe().T)


# Seperating values in arrays
t = []
for i in range (0, 1999):
    t.append([str(df.values[i, j]) for j in range (0, 9)]) # Loop for every row

#%% 

# Association Rules Analysis

# Importing apriori function from 'apyori.py'
from apyori import apriori
rules_1 = apriori(t, min_support=0.01, min_confidence=0.2, min_lift = 3, min_length=2)

print(list(rules_1))


#  Importing apriori from mlxtend library
from mlxtend.frequent_patterns import apriori
df1 = apriori(df, min_support=0.02, use_colnames = True, verbose=1)

print(df1)

from mlxtend.frequent_patterns import association_rules

rules_2 = association_rules(df1, metric = "confidence", min_threshold = 0.2)
rules_2[(rules_2['confidence'] >= 0.2) & (rules_2['support'] >= 0.1)]

print(rules_2)
rules_2.to_excel("rules_2.xlsx")
