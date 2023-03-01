import pandas as pd
df = pd.read_csv('C:/Users/rlaeo/OneDrive/바탕 화면/iris.csv', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

f = sns.pairplot(df, hue="species");
plt.show()
