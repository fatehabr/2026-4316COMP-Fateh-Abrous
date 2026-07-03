import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/vgsales.csv")

genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
genre_sales.plot(kind="bar")
plt.title("Global Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Global Sales (Millions)")
plt.tight_layout()
plt.savefig("screenshots/genre_sales.png")
plt.show()