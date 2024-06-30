import pandas as pd
from scikit-learn.preprocessing import StandardScaler
from scikit-learn.ensemble import RandomForestClassifier
from scikit-learn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("iris.csv")

print(df.head())
print(df[['sepal_length']])

# Select independent and dependent variable
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]
print(X)

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))
