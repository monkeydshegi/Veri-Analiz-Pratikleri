import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_vgchartz_2024.csv')

df_gruplama = df.groupby('decade')['total_sales'].sum().reset_index()

plt.figure(figsize=(10,6))

sns.barplot(data=df_gruplama,x="decade",y="total_sales",hue="total_sales", palette="pastel")

plt.title("Oyunların altın çağı!/Golden age of games!")
plt.xlabel("Yıllar/Years(70s,80s,etc.)")
plt.ylabel("Toplam Satış/Total Sales")
plt.show()

