import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'C:/Tez/.venv/95_hata.xlsx'
sheet_names = pd.ExcelFile(file_path).sheet_names

distributions = ['Uniform', 'Ustel', 'Beta', 'Normal', 'Weibull', 'Lognormal', 'Geometric', 'Poisson']

contingency_tables = {}

for sheet in sheet_names:
    data = pd.read_excel(file_path, sheet_name=sheet, header=None)
    distribution_types = data.iloc[:, 10]
    predicted_distributions = data.iloc[:, 13]

    contingency_table = pd.DataFrame(0, index=distributions, columns=distributions)

    for i in range(len(distribution_types)):
        generated = distribution_types[i]
        predicted = predicted_distributions[i]

        if generated in distributions and predicted in distributions:
            contingency_table.loc[generated, predicted] += 1

    contingency_tables[sheet] = contingency_table

heatmap_data = pd.concat(contingency_tables, axis=1)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='g', cbar_kws={'label': 'Tahmin Edilen Dağılım Sayısı'})
plt.title('Isı Haritası')
plt.xlabel('Sayfalar')
plt.ylabel('Gerçek Dağılım Türleri')
plt.show()
