import numpy as np
import pandas as pd
from scipy.stats import pearsonr

#This function will obtain correlation values between all predictor and outcome variables,
#and thereby demonstrate if a noticeable linear relationship is present in any of these pairs.
def insight1(df):
    predictor_names = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"]
    outcome_variable_names = ["2017-2018 ACGR", "2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"]

    correlation_df = pd.DataFrame(index = predictor_names, columns = outcome_variable_names)

    for predictor in predictor_names:
        for outcome_var in outcome_variable_names:
            correlation_df.loc[predictor, outcome_var] = pearsonr(x = df[predictor], y = df[outcome_var])[0]

    return correlation_df

df = pd.read_csv("Predictor & Response Variables.csv", index_col = 0)
print(insight1(df))
