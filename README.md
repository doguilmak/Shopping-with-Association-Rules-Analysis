
# Shopping Evaluation with Association Rules Analysis

## Problem Statement

Some inferences were obtained from the people who shopped among 9 different products representing the shopping cart of different people. The aim is to obtain and interpret the links between people's preferred products. Association rule extraction, which can provide a very efficient effect for markets, is built step by step in the **poc.py** file.

## Dataset

Dataset is created by myself. It has ***9 columns*** and ***2000 rows with the header***. Each column represents different products. A value of 0 indicates that the product was not received by the customer, and a value of 1 indicates that the product was received by the customer.

## Methodology

In this project, evaluations were made with the **apriori** algorithm. **apyori.py** was made by **Yu Mochizuki**. If you are looking for the meaning of support, confience, lift and etc. please take a look at [Wikipedia](https://en.wikipedia.org/wiki/Association_rule_learning).

## Analysis

Analysis is included in **rules_2.xlsx** file. Also you can check on **rules_2** dataframe in **poc.py**.

**Process took 0.26288461685180664 seconds.**

## How to Run Code

Before running the code make sure that you have these libraries:

 - pandas 
 - apyori (in apyori.py file)
 - mlxtend
    
## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak).  
 - Mail address: doguilmak@gmail.com
 