import pandas as pd

file_path = 'C:/Tez/.venv/95_hata.xlsx'
sheet_names = pd.ExcelFile(file_path).sheet_names

distributions = ['Uniform', 'Ustel', 'Beta', 'Normal', 'Weibull', 'Lognormal', 'Geometric', 'Poisson']

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

    print(f"{sheet} sayfası için kontenjan tablosu:")
    print(contingency_table)

    contingency_table.to_excel(f'kontenjan_tablo_{sheet}.xlsx', index=True)
