import pandas as pd
from scipy.stats import kstest, norm, uniform, beta, expon, lognorm, weibull_min, geom, poisson

distribution_functions = {
    "Normal": norm,
    "Uniform": uniform,
    "Beta": beta,
    "Ustel": expon,
    "Lognormal": lognorm,
    "Weibull": weibull_min,
    "Geometric": geom,
    "Poisson": poisson
}


single_param_distributions = ["Ustel", "Geometric", "Poisson"]


double_param_distributions = ["Normal", "Uniform", "Beta", "Lognormal", "Weibull"]


xls = pd.ExcelFile("895_all_output.xlsx")
output_dfs = {}


for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)

    df["distribution1_result"] = ""
    df["distribution2_result"] = ""


    for index, row in df.iterrows():
        data = row.iloc[:10].values.astype(float)


        dist1_name = row.iloc[10]
        param1_1 = float(row.iloc[11])
        param1_2 = float(row.iloc[12])

        if param1_2 == 0:
            df.at[index, "distribution1_result"] = 0
        elif dist1_name in distribution_functions:
            dist_func1 = distribution_functions[dist1_name]
            if dist1_name in double_param_distributions:
                args1 = (param1_1, param1_2)
            else:
                args1 = (param1_1,)

            ks_stat1, p_value1 = kstest(data, dist_func1.cdf, args=args1)
            df.at[index, "distribution1_result"] = "Uygun" if p_value1 > 0.05 else "Uygun Degil"


        dist2_name = row.iloc[13]
        param2_1 = float(row.iloc[11])
        param2_2 = float(row.iloc[12])

        if param2_2 == 0:
            df.at[index, "distribution2_result"] = 0
        elif dist2_name in distribution_functions:
            dist_func2 = distribution_functions[dist2_name]
            if dist2_name in double_param_distributions:
                args2 = (param2_1, param2_2)
            else:
                args2 = (param2_1,)

            ks_stat2, p_value2 = kstest(data, dist_func2.cdf, args=args2)
            df.at[index, "distribution2_result"] = "Uygun" if p_value2 > 0.05 else "Uygun Degil"


    output_dfs[sheet_name] = df


with pd.ExcelWriter("distribution_test_results_all_sheets.xlsx") as writer:
    for sheet_name, output_df in output_dfs.items():
        output_df.to_excel(writer, sheet_name=sheet_name, index=False)
