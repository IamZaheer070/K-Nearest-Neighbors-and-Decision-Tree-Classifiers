import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
#load data fram and using specified attributes
data = pd.read_csv("/content/drive/MyDrive/DATA.csv")
selected_attributes = data.iloc[:, 12:17]
target = data['GRADE'].values

X_train, X_test, y_train, y_test = train_test_split(selected_attributes, target, test_size=0.2, random_state=39)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
result = classification_report(y_test, y_pred, zero_division=1)
print("KNN Results:")
print(result)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(selected_attributes, data['GRADE'], test_size=0.2, random_state=41)
clf_dt = DecisionTreeClassifier()
#training data
clf_dt.fit(X_train, y_train)
#use testing data for predictions
y_pred_dt = clf_dt.predict(X_test)
result1 = classification_report(y_test, y_pred_dt, zero_division=1)
print("Decision Tree Classifier Results:")
print(result1)