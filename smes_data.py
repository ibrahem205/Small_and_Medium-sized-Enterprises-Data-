import pandas as pd

data = pd.read_csv('/Downloads/Number of Smes Data.csv)

# Filter the DataFrame to include only the unknown 'النشاط الاقتصادي'
filtered_data = data[data['النشاط الاقتصادي'] == 'غير معرف']
# Create a pivot table with the filtered DataFrame and save it to a CSV file
filtered_data.pivot_table(columns='المنطقة', values='عدد المنشآت').to_csv('/Downloads/Number of unknown sem.csv', encoding='utf-8-sig')

# Create a pivot table with the region to all types of smes and save it to a CSV file
data.pivot_table(columns='المنطقة', values=['عدد المنشآت','عدد المنشآت متناهية الصغر','عدد المنشآت الصغيرة','عدد المنشآت المتوسطة','عدد المنشآت الكبيرة'], aggfunc='sum').to_csv('/Downloads/Number of sems per region.csv', encoding='utf-8-sig')

# Group the name of smes to the maximum number of smes, sort them in descending order, and save it to a CSV file
data.groupby('النشاط الاقتصادي')['عدد المنشآت'].max().sort_values(ascending=False).head(10).to_csv('/Downloads/Highest Smes.csv', encoding='utf-8-sig')
