""" Lab 10: Save people
You can save people from heart disease by training a model to predict whether a person has heart disease or not.
The dataset is available at src/lab10/heart.csv
Train a model to predict whether a person has heart disease or not and test its performance.
You can usually improve the model by normalizing the input data. Try that and see if it improves the performance. 

EQ for normalizing: x' = (x - xmin)/(xmax - xmin) ((Every resut will be between 0 and 1))
"""
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np

data = pd.read_csv("src/lab10/heart.csv")


# Transform the categorical variables into dummy variables.
print(data.head())
string_col = data.select_dtypes(include="object").columns
df = pd.get_dummies(data, columns=string_col, drop_first=False)
print(df.head())

y = df.HeartDisease.values
x = df.drop(["HeartDisease"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=3
)

""" Train a sklearn model here. """
#The n_neighbors parameter can decide how biased your model is if it's too high!
#Through testing, I discovered that non-normalized data created a more-accurate model when n_neighbors was lower,
#but the opposite was true for normalized data. The model improved with a higher n_neighbors, plateuing around 80. Only a smidge higher than the
#model trained on non-normalized data.
sklearn_model = KNeighborsClassifier(n_neighbors=10)
sklearn_model.fit(x_train,y_train)


# Accuracy
print("Accuracy of model: {}\n".format(sklearn_model.score(x_test,y_test)))

""" Improve the model by normalizing the input data. 
If the performace does not improve explain why as a comment in the code. """

y = df.HeartDisease.values
x = df.drop(["HeartDisease"], axis=1)

# Normalize the input data before creating a test train split (Use the same random state)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_test, y_test)))
