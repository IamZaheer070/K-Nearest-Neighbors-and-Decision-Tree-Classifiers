**Machine Learning Project: K-Nearest Neighbors and Decision Tree Classifiers**
**K-Nearest Neighbors and Decision Tree Classifiers & Association Rule Mining**

This project demonstrates how to implement and evaluate two machine learning classifiers, K-Nearest Neighbors (KNN) and Decision Tree, using Python's `scikit-learn` library. The code includes data preparation, model training, testing, and performance evaluation.

@@ -This project demonstrates how to implement and evaluate two machine learning classification
   - **Model Training:** A Decision Tree classifier is trained on the new training set.
   - **Prediction:** The trained Decision Tree model predicts the target variable for the test set.
   - **Evaluation:** A classification report is generated to assess the model's performance.

**Association Rule Mining with Apriori Algorithm**

This code demonstrates the use of the Apriori algorithm and association rule mining to analyze transactional data from a bakery dataset. The process involves extracting frequent itemsets and generating strong association rules based on specified metrics.

**Data Loading and Preparation:**
Load the dataset from Bakery.csv.
Copy the dataset for processing.
Identify and exclude infrequent items (items appearing less than twice).

**Transaction Encoding:**

Convert the transactional data into a format suitable for the Apriori algorithm.
Filter out transactions containing infrequent items and ensure that transactions have more than one item.

**Data Transformation:**

Use TransactionEncoder to transform the data into a binary matrix.
Convert the binary matrix into a pandas DataFrame.

**Frequent Itemset Mining:**

Apply the Apriori algorithm to find frequent itemsets with a minimum support of 0.002.
Calculate and sort itemsets by support.

**Association Rule Generation:**

Generate association rules from the frequent itemsets with a minimum confidence threshold of 0.2.
Extract and display rules including antecedents, consequents, support, confidence, and lift.
