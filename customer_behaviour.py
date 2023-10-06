# -*- coding: utf-8 -*-
"""svce_neural_network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QmxdBKX3tSbuC5W7D8w29XpHPOakZwMJ
"""

import tensorflow as tf
from tensorflow import keras
from keras.models import Model
from keras import Input

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Final_customer.csv")
df.head(5)
df.columns

x = df[["Age","Salary", "Recency","Frequency", "Average views of the product"]]
y = df["Spending score"]
x

inputs = Input(shape = (5, ))
layer1 = keras.layers.Dense(10, activation = tf.nn.relu)(inputs)
layer2 = keras.layers.Dense(16, activation = tf.nn.relu)(layer1)
layer3 =  keras.layers.Dense(16, activation = tf.nn.relu)(layer2)
layer4 =  keras.layers.Dense(10, activation = tf.nn.relu)(layer3)
output =  keras.layers.Dense(1, activation = "linear")(layer4)
model = Model(inputs = inputs, outputs = output)

model.summary()

model.compile(loss = 'mse', optimizer = 'adam', metrics = ['mse', 'mae'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, test_size =0.2)

model.fit(x_train, y_train, epochs =250)

pred = model.predict(x_test)
pred
#predicted values

y_test#test values

import numpy as np
threshhold = np.median(np.array(df["Spending score"]))
def prediction():
  x1 = int(input("Enter the Age: "))
  x2 = int(input("Enter the Salary: "))
  x3 = int(input("Enter the Recency: "))
  x4 = int(input("Enter the Frequency: "))
  x5 = int(input("Enter the Average views of the product: "))
  predicted_value =  model.predict([[x1,x2,x3,x4,x5]])
  w = 'more' if predicted_value > threshhold else 'less'
  print(f"Customer is {w} likely to purchase the product")

#"Age","Salary", "Recency","Frequency", "Average views of the product"
demo = model.predict([[34, 65000, 21, 21, 9]])
if demo>threshhold:
  print("Customer is more likely to purchase the product")
else:
  print("Customer is less likely to purchase the product")

prediction()

