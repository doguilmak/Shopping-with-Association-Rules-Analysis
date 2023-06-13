
<h1 align=center><font size = 5>Offer Food with Association Rules Analysis</font></h1>

<br>

<img src="https://images.unsplash.com/photo-1542838132-92c53300491e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80" height=480 width=950 alt="market">

<small>Picture Source: <a href="https://unsplash.com/photos/D6Tu_L3chLE">Unsplash</a></small>

<br>

<h2>Objective</h2>

<p>In this project, a recommendation model was developed with <i>Association rule analysis</i> based on the products preferred by the customers (random). Some inferences were obtained from the people who shopped among 9 different products representing the shopping cart of different people. The aim is to obtain and interpret the links between people's preferred products. Association rule extraction, which can provide a very efficient effect for markets.</p>

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

<h2>Association Rules Analysis</h2>

<p>The strength of an association rule is measured by two metrics: support and confidence.  </p>

<p><code>Support</code>: Support indicates the frequency of occurrence of the items in the dataset. It is calculated as the proportion of transactions containing both itemset A and itemset B. Support is an indication of how frequently the itemset appears in the dataset.</p>  

$$support = P(A \cap B) $$  

<br>  

<p><code>Confidence</code>: Confidence measures the reliability of the association rule. It is calculated as the proportion of transactions containing itemset A that also contain itemset B. Confidence is the percentage of all transactions satisfying X that also satisfy Y.</p>  

$$conf(X \Rightarrow Y) = P(Y | X) = \frac{supp(X \cap Y)}{supp(X)}$$

<br>  

<p>Additionally, two other metrics are often used in association rules analysis:  </p>

<br>  

<p><code>Lift</code>: Lift measures the strength of the association rule by comparing the observed support with the expected support if itemset A and itemset B were independent of each other. A lift greater than 1 indicates a positive association, while a lift less than 1 indicates a negative association. The ratio of the observed support to that expected if X and Y were independent.</p>

$$lift(X \Rightarrow Y) = \frac{supp(X \cap Y)}{supp(X) \cdot supp(Y)}$$

<br>

<p><code>Conviction</code>: Conviction measures the degree of implication of the rule. It is calculated as the ratio of the expected confidence to the observed confidence if itemset A and itemset B were independent of each other. Higher conviction values indicate stronger implications.It compares the probability that X appears without Y if they were dependent with the actual frequency of the appearance of X without Y.</p>

$$conv(X \Rightarrow Y) = \frac{1-supp(Y)}{1-conf(X \Rightarrow Y)}$$

<br>  

</p>Association rules analysis helps uncover hidden patterns and relationships in the data, which can be used for various purposes. For example, in retail, it can be used to make product recommendations, optimize store layouts, plan promotional strategies, and improve inventory management.</p>  

<p>By identifying the frequent itemsets and generating meaningful association rules, businesses can gain insights into customer behavior, improve decision-making, and enhance the overall customer experience.</p>

<br>

  

<small>Source: <a  href='https://en.wikipedia.org/wiki/Association_rule_learning'>Wikipedia</a></small>


<h2>Data Set Information:</h2>

<p>The Data Set was obtained on completely random values. It was created for demonstration (prototype) purposes only, as no real data is available. The values ​​of the dataset can be played with as desired.</p>

<p>The variety of the product can be arranged as desired.</p>

    items = ['Coffee', 'Bread', 'Milk', 'Eggs', 'Butter', 'Juice', 'Cereal', 'Yogurt', 'Cheese', 'Pasta', 'Rice', 'Chicken', 'Beef', 'Fish', 'Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries', 'Tomatoes', 'Potatoes', 'Carrots', 'Onions', 'Lettuce', 'Broccoli', 'Cucumber', 'Soap', 'Shampoo', 'Toothpaste']

<p>The number of customers shopping and the number of products purchased can be adjusted as desired.</p>

    np.random.seed(42) 
    data = [] 
    df_range = 1000  #@param {type:"number"}  
    for _ in  range(df_range): 
	    customer = [int(pd.Series([0, 1]).sample(n=1, weights=[0.7, 0.3]).iloc[0]) for _ in  range(len(items))] 
	    data.append(customer) 
	    
	df = pd.DataFrame(data, columns=items) 
	df.insert(0, 'CustomerID', range(1, df_range+1))

<br>

<h1>Contact Me</h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
