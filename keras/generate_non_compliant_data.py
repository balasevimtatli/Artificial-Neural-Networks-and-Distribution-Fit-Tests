import pandas as pd

xls = pd.ExcelFile("995k95_prediction_last_update_control_95.xls")
output_dfs = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)


    filtered_df = df[df["check"] > 0]

    rows = []
    columns = df.columns.tolist()

    for index, row in filtered_df.iterrows():
        first_13_columns = row.iloc[:13].copy()

        prediction_value = 0
        for i in range(47, 62):
            col = columns[i]
            if row[col] == 1:
                if col == "New_Prediction_0":
                    prediction_value = "Lognormal"
                elif col == "New_Prediction_1":
                    prediction_value = "Poisson"
                elif col == "New_Prediction_2":
                    prediction_value = "Ustel"
                elif col == "New_Prediction_3":
                    prediction_value = "Geometric"
                elif col == "New_Prediction_4":
                    prediction_value = "Normal"
                elif col == "New_Prediction_5":
                    prediction_value = "Weibull"
                elif col == "New_Prediction_8":
                    prediction_value = "Uniform"
                elif col == "New_Prediction_12":
                    prediction_value = "Beta"
                else:
                    prediction_value = 0
                break

        first_13_columns["prediction_value"] = prediction_value

        rows.append(first_13_columns)

    # Sonuçları dataframe olarak kaydet
    output_df = pd.DataFrame(rows, columns=columns[:13] + ["prediction_value"])
    output_dfs[sheet_name] = output_df

# Sonuçları yeni bir Excel dosyasına yaz
with pd.ExcelWriter("95_hata.xlsx") as writer:
    for sheet_name, output_df in output_dfs.items():
        output_df.to_excel(writer, sheet_name=sheet_name, index=False)
