import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mengunduh dataset Superstore dari URL
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
superstore_data = pd.read_csv(url)

# a. Menemukan kategori di setiap region yang memiliki sales paling tinggi
highest_sales_by_category = superstore_data.groupby(['Region', 'Category'])['Sales'].max().reset_index()
idx = highest_sales_by_category.groupby(['Region'])['Sales'].transform(max) == highest_sales_by_category['Sales']
result_a = highest_sales_by_category[idx]

# Visualisasi a menggunakan Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Sales', hue='Category', data=result_a)
plt.title('Sales Paling Tinggi berdasarkan Kategori di Setiap Region')
plt.show()

# b. Menemukan bulan di setiap tahun yang memiliki sales di atas rata-rata sales per tahunnya
superstore_data['OrderDate'] = pd.to_datetime(superstore_data['OrderDate'])
superstore_data['Year'] = superstore_data['OrderDate'].dt.year
monthly_sales = superstore_data.groupby(['Year', superstore_data['OrderDate'].dt.month])['Sales'].sum().reset_index()
average_sales_per_year = superstore_data.groupby('Year')['Sales'].mean().reset_index()
average_sales_per_year.columns = ['Year', 'AverageSales']

result_b = monthly_sales[monthly_sales['Sales'] > monthly_sales['Year'].map(average_sales_per_year.set_index('Year')['AverageSales'])]

# Visualisasi b menggunakan Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x='Year', y='Sales', hue='OrderDate', data=result_b)
plt.title('Sales di Atas Rata-rata per Bulan di Setiap Tahun')
plt.show()
