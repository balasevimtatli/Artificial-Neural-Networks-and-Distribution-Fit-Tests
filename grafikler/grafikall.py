import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Tez/.venv/95_hata.xlsx'
sheet_names = pd.ExcelFile(file_path).sheet_names

distributions = ['Uniform', 'Ustel', 'Beta', 'Normal', 'Weibull', 'Lognormal', 'Geometric', 'Poisson']

contingency_tables = {}

for sheet in sheet_names:
    data = pd.read_excel(file_path, sheet_name=sheet, header=None)

    distribution_types = data.iloc[:, 10]   # 11. sütun dağılım türleri
    predicted_distributions = data.iloc[:, 13]  # 14. sütun tahmin edilen dağılım türleri

    contingency_table = pd.DataFrame(0, index=distributions, columns=distributions)

    for i in range(len(distribution_types)):
        generated = distribution_types[i]
        predicted = predicted_distributions[i]

        if generated in distributions and predicted in distributions:
            contingency_table.loc[generated, predicted] += 1

    contingency_tables[sheet] = contingency_table

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
axes = axes.flatten()

for ax, (sheet, table) in zip(axes, contingency_tables.items()):
    table.plot(kind='bar', ax=ax, title=f"{sheet} Sayfası Kontenjan Tablosu")
    ax.set_xlabel("Gerçek Dağılım Türleri")
    ax.set_ylabel("Tahmin Edilen Dağılım Sayısı")
    ax.legend(title="Tahmin Edilen Dağılımlar")
    ax.grid(axis='y')

plt.tight_layout()
plt.show()
