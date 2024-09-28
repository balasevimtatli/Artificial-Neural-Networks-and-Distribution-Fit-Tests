import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C://Tez//.venv/9595distribution_test_results_all_sheets.xlsx'
excel_file = pd.ExcelFile(file_path)

for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    distributions = df.iloc[:, 13]  # 10. sütun (Dağılım bilgisi)
    suitability = df.iloc[:, 15].replace("Uygun Degil", "Uygun Değil")  # 14. sütun ("Uygun"/"Uygun Degil" bilgisi)

    distribution_groups = df.groupby([distributions, suitability]).size().unstack(fill_value=0)

    distribution_groups.plot(kind='bar', stacked=True, color=['green', 'red'])
    plt.title(f"{sheet_name} - Dağılımların Uygunluk Durumu")
    plt.xlabel("Dağılım Türü")
    plt.ylabel("Frekans")
    plt.legend(["Uygun", "Uygun Degil"])
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
