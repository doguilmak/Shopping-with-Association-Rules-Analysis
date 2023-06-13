# -*- coding: utf-8 -*-
"""AssociationRulesAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/134u2gUr_E7gKQOp-DwodRhvngX87_iST

<h1 align=center><font size = 5>Offer Food with Association Rules Analysis</font></h1>

<br>

<img src="https://images.unsplash.com/photo-1542838132-92c53300491e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80" height=480 width=950 alt="market">

<small>Picture Source: <a href="https://unsplash.com/photos/D6Tu_L3chLE">Unsplash</a></small>

<br>

<h2>Data Set Information:</h2>

<p>The dataset has no real-world equivalent. It is completely randomly generated. Therefore, it will be of great benefit to going through the real data set in order to make a real recommendation. If you have the appropriate data set, you can go over it (hope you show it to me).</p>

<br>

<h2>Association Rules Analysis</h2>

<p>Association Rules Analysis is a data mining technique used to discover interesting relationships or associations among a set of items in large datasets. It is commonly applied in market basket analysis, where the goal is to identify patterns in customer purchasing behavior.</p>

<br>

<p>The analysis involves finding associations between items that frequently co-occur in transactions. The associations are represented as rules of the form "if {itemset A} then {itemset B}". For example, a rule could be "if a customer buys bread and milk, then they are likely to buy eggs."</p>

<br>

<h2>Keywords</h2>

<ul>
	<li>Market</li>
	<li>Machine Learning</li>
	<li>Association Rules Analysis</li>
	<li>Apriori</li>
	<li>Association Rule Mining</li>
</ul>

<br>

<h1>Objective for this Notebook</h1>

<p>In this project, a recommendation model was developed with <i>Association rule analysis</i> based on the products preferred by the customers.</p>

<div class="alert alert-block alert-info" style="margin-top: 20px">
<li><a href="https://#importing_libraries">Importing Libraries</a></li>
<li><a href="https://#data_preprocessing">Data Preprocessing</a></li>
<li><a href="https://#build_ara_model">Building Association Rules Analysis Model</a></li>
<br>

<p></p>
Estimated Time Needed: <strong>20 min</strong>
</div>

<a id="importing_libraries"></a>

<h2 align=center>Importing Libraries</h2>
"""

import pandas as pd
import numpy as np

"""<br>

<a id="data_preprocessing"></a>

<h2 align=center>Data Preprocessing</h2>
"""

items = ['Coffee', 'Bread', 'Milk', 'Eggs', 'Butter', 'Juice', 'Cereal', 'Yogurt', 'Cheese', 'Pasta',
         'Rice', 'Chicken', 'Beef', 'Fish', 'Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries',
         'Tomatoes', 'Potatoes', 'Carrots', 'Onions', 'Lettuce', 'Broccoli', 'Cucumber', 'Soap',
         'Shampoo', 'Toothpaste']

"""<p>This code will generate a DataFrame with 30 item columns and 1000 customer rows. You can change it as you wish. Each value in the DataFrame represents whether the <b>customer took the item (1)</b> or <b>not (0)</b>. The 'CustomerID' column is added to uniquely identify each customer.</p>"""

np.random.seed(42)

data = []

df_range = 1000 #@param {type:"number"}
for _ in range(df_range):
    customer = [int(pd.Series([0, 1]).sample(n=1, weights=[0.7, 0.3]).iloc[0]) for _ in range(len(items))]
    data.append(customer)

df = pd.DataFrame(data, columns=items)
df.insert(0, 'CustomerID', range(1, df_range+1))

df.head()

"""<p>Let's return the last 5 rows of the DataFrame. However, you can pass an integer value inside the parentheses to specify a different number of rows to retrieve.</p>"""

df.tail()

"""<p>Show descriptive statistics of a DataFrame and transpose the result.</p>"""

df.describe().T

df.info()

print("Number of NaN values: {}.".format(df.isnull().sum().sum()))

df.shape

df.to_excel('data.xlsx', index=False)

df.drop(columns=['CustomerID'], axis=1, inplace=True)

"""<br>

<a id="build_ara_model"></a>

<h2 align=center>Building Association Rules Analysis Model</h2>
"""

from mlxtend.frequent_patterns import apriori
df1 = apriori(df, min_support=0.02, use_colnames = True)

print(df1)

from mlxtend.frequent_patterns import association_rules

rule = association_rules(df1, metric = "confidence", min_threshold = 0.2)

"""The strength of an association rule is measured by two metrics: support and confidence.

<p><code>Support</code>: Support indicates the frequency of occurrence of the items in the dataset. It is calculated as the proportion of transactions containing both itemset A and itemset B. Support is an indication of how frequently the itemset appears in the dataset.</p>

$$support = P(A \cap B) $$

<br>

<p><code>Confidence</code>: Confidence measures the reliability of the association rule. It is calculated as the proportion of transactions containing itemset A that also contain itemset B. Confidence is the percentage of all transactions satisfying X that also satisfy Y.</p>

$$conf(X 	\Rightarrow Y) = P(Y | X) = \frac{supp(X \cap Y)}{supp(X)}$$

<br>

Additionally, two other metrics are often used in association rules analysis:

<br>

<p><code>Lift</code>: Lift measures the strength of the association rule by comparing the observed support with the expected support if itemset A and itemset B were independent of each other. A lift greater than 1 indicates a positive association, while a lift less than 1 indicates a negative association. The ratio of the observed support to that expected if X and Y were independent.</p>

$$lift(X 	\Rightarrow Y) = \frac{supp(X \cap Y)}{supp(X) \cdot supp(Y)}$$

<br>




<p><code>Conviction</code>: Conviction measures the degree of implication of the rule. It is calculated as the ratio of the expected confidence to the observed confidence if itemset A and itemset B were independent of each other. Higher conviction values indicate stronger implications.It compares the probability that X appears without Y if they were dependent with the actual frequency of the appearance of X without Y.</p>

$$conv(X 	\Rightarrow Y) = \frac{1-supp(Y)}{1-conf(X \Rightarrow Y)}$$

<br>

Association rules analysis helps uncover hidden patterns and relationships in the data, which can be used for various purposes. For example, in retail, it can be used to make product recommendations, optimize store layouts, plan promotional strategies, and improve inventory management.

By identifying the frequent itemsets and generating meaningful association rules, businesses can gain insights into customer behavior, improve decision-making, and enhance the overall customer experience.

<br>

<small>Source: <a href='https://en.wikipedia.org/wiki/Association_rule_learning'>Wikipedia</a></small>
"""

rule[(rule['confidence'] >= 0.30) & (rule['support'] >= 0.1)]

rule["antecedents"] = rule["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
rule["consequents"] = rule["consequents"].apply(lambda x: ', '.join(list(x))).astype("unicode")

rule

['Coffee', 'Bread', 'Milk', 'Eggs', 'Butter', 'Juice', 'Cereal', 'Yogurt', 'Cheese', 'Pasta',
         'Rice', 'Chicken', 'Beef', 'Fish', 'Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries',
         'Tomatoes', 'Potatoes', 'Carrots', 'Onions', 'Lettuce', 'Broccoli', 'Cucumber', 'Soap',
         'Shampoo', 'Toothpaste']

rule[(rule['antecedents'] == 'Coffee') & (rule['confidence'] >= 0.10) & (rule['support'] >= 0.001)]

rule[(rule['antecedents'] == 'Bread, Milk') & (rule['confidence'] >= 0.10) & (rule['support'] >= 0.001)]

rule[(rule['antecedents'] == 'Bread, Milk') & (rule['confidence'] >= 0.10) & (rule['support'] >= 0.001)]['consequents'][0:3].values

rule[(rule['antecedents'] == 'Bread, Milk') & (rule['confidence'] >= 0.10) & (rule['support'] >= 0.001)]['support'][0:3].values

def suggest_item(rule, items, min_threshold=0.2, min_support=0.02, parameter='support', confidence_thold = 0.10, support_thold=0.001):
  from mlxtend.frequent_patterns import apriori
  import numpy as np
  import pandas as pd

  df1 = apriori(df, min_support=min_support, use_colnames = True)
  rule = association_rules(df1, metric = "confidence", min_threshold = min_threshold)

  rule["antecedents"] = rule["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
  rule["consequents"] = rule["consequents"].apply(lambda x: ', '.join(list(x))).astype("unicode")

  suggestions = rule[(rule['antecedents'] == items) & \
                     (rule['confidence'] >= confidence_thold) & \
                     (rule['support'] >= support_thold)]['consequents'].values

  parameters = rule[(rule['antecedents'] == items) & \
                     (rule['confidence'] >= confidence_thold) & \
                     (rule['support'] >= support_thold)][parameter].values

  return suggestions, parameters

item = 'Bread'
suggested_items, parameter = suggest_item(rule, item, parameter='confidence')
for i in range(len(suggested_items)):
  print(f'I recommend to buy you {suggested_items[i]} with {parameter[i]} value with {item}.')

"""<p>The best recommendation is on the below for the <code>Bread</code> item."""

list_zip = zip(suggested_items, parameter)
zipped_list = list(list_zip)
df2 = pd.DataFrame(zipped_list, columns = ['item','parameter'])
best_parameter = df2['parameter'].max()
best_suggestion = df2['item'][df2['parameter'].argmax()]
print(f'Best parameter: {best_parameter}')
print(f'Best suggestion: {best_suggestion}')

"""<br>

<h1>Contact Me<h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")