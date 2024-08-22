from mlxtend.frequent_patterns.association_rules import association_rules
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
# Load data
data = pd.read_csv('Bakery.csv')
data2 = data.copy()
# data.info()
val_counts = dict(data["Items"].value_counts()[:10])
val_counts = data["Items"].value_counts()
val_counts.tail(10)
excluded = list(val_counts[val_counts.values < 2].index)
transactions=[]
for action in data2["TransactionNo"].unique():
    transaction=list(set(data2[data2["TransactionNo"]==action]['Items']))
    if not any(x in transaction for x in excluded):
        if len(transaction) != 1:
            transactions.append(transaction)
transEnc = TransactionEncoder()
#covert data into binary matrix true false
te_ary = transEnc.fit(transactions).transform(transactions)
#convert binary matrix into pandas dataframs
df = pd.DataFrame(te_ary, columns=transEnc.columns_)
min_support = 0.002
min_lift = 0.1
freq_itemsets = apriori(df, min_support,use_colnames=True)
freq_itemsets['support'] = freq_itemsets['support']*100
freq_itemsets = freq_itemsets.sort_values(by='support',ascending=False)
min_confthreshold = 0.2
rules = association_rules(freq_itemsets, metric='confidence', min_threshold=min_confthreshold)
result = rules[['antecedents','consequents','support','confidence','lift']]
print("\nStrong Association Rules are:")
print(result[:2])