#1.Find the relationship between top 5 Job designation and total Purchase amount
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('Ecommerce_Purchases.csv')
grouped_data = data.groupby('Job')['Purchase Price'].sum().reset_index()
top_5_jobs1 = grouped_data.sort_values('Purchase Price', ascending=False).head(5)
ax = sns.barplot(x = "Job", y = "Purchase Price", data = top_5_jobs1)
ax.set(xlabel="Profession", ylabel = "Total Purchase",title="Top 5 Jobs by Total Purchase Amount")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()
