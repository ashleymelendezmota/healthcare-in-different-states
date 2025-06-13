import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

# print the first five rows
print(healthcare.head())

# print all unique diagnosis definitions in the 'DRG Definition' column
print(healthcare["DRG Definition"].unique())

# rows about chest pain
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# separate by state
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

# average cost
costs = alabama_chest_pain[' Average Covered Charges '].values

# boxplot
states = chest_pain['Provider State'].unique()
print(states)

# charges covered by state
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

# state boxplots space
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 6))

# boxplot states
plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels = states)
plt.show()

