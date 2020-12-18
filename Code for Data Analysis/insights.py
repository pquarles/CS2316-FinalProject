### insights.py ###
''' NOTE - all functions take in 'df' as an argument. df is a variable that we assigned to our function df_concatenation()
that you can find within the folder (it stores our final dataframe we use for analysis).'''

def insight1(df):
    import numpy as np
    import pandas as pd
    from scipy.stats import pearsonr

    '''This function will obtain correlation values between all predictor and outcome variables,
    and thereby demonstrate if a noticeable linear relationship is present in any of these pairs.'''

    predictor_names = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"]
    outcome_variable_names = ["2017-2018 ACGR", "2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"]

    correlation_df = pd.DataFrame(index = predictor_names, columns = outcome_variable_names)

    for predictor in predictor_names:
        for outcome_var in outcome_variable_names:
            correlation_df.loc[predictor, outcome_var] = pearsonr(x = df[predictor], y = df[outcome_var])[0]

    return correlation_df

def insight2(df):
    import numpy as np
    import pandas as pd

    '''IDEA: All averages fall where we would assume: For Math, between NAEP Basic (262) and NAEP Proficient (299) &
    For Reading, between Basic (243) and Proficient (281) as well. So, I'll create categories for Math/Reading to see what states
    are above the 80th percentile of scores (assign True/False to it) & see if spending has a trend with it.'''

    spending_df = dataframe[["Current Spending on Instruction/Student", "Total Revenue/Student", "2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"]]
    sorted_df = spending_df.sort_values(by= "Current Spending on Instruction/Student", ascending = False)

    percentile_80_math = np.percentile(sorted_df["2019 Average NAEP Math Score"], 80)
    percentile_80_reading = np.percentile(sorted_df["2019 Average NAEP Reading Score"], 80)

    sorted_df["NAEP Math Avg Better than 80% of States"] = sorted_df["2019 Average NAEP Math Score"] >= percentile_80_math
    sorted_df["NAEP Reading Avg Better than 80% of States"] = sorted_df["2019 Average NAEP Reading Score"] >= percentile_80_reading

    sorted_df.drop(["2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"], axis = 1, inplace=True)

    return sorted_df.head(10) #return Top 10 States by Spending on Instruction/Student

def insight3(df):
    import numpy as np
    import pandas as pd
    from sklearn import linear_model

    '''This function performs creates two multiple linear regressions using all predictor variables to predict NAEP Math and Reading scores. It returs a dataframe with the coefficients for each variable, as well as the r-squared values
    and intercept for each model.'''

    predictors = df[[f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"]]

    regression_df = pd.DataFrame(index = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"], \
    columns = ["Math Coefficient", "Reading Coefficient"])

    math_regression_obj = linear_model.LinearRegression()
    math_regression_obj.fit(predictors, df["2019 Average NAEP Math Score"])
    math_r_squared = math_regression_obj.score(predictors, df["2019 Average NAEP Math Score"])
    math_intercept = math_regression_obj.intercept_
    regression_df.loc[:, "Math Coefficient"] = math_regression_obj.coef_

    reading_regression_obj = linear_model.LinearRegression()
    reading_regression_obj.fit(predictors, df["2019 Average NAEP Reading Score"])
    reading_r_squared = reading_regression_obj.score(predictors, df["2019 Average NAEP Reading Score"])
    reading_intercept = reading_regression_obj.intercept_
    regression_df.loc[:, "Reading Coefficient"] = reading_regression_obj.coef_

    return (regression_df, math_r_squared, math_intercept, reading_r_squared, reading_intercept)

def insight4(df):
    import numpy as np
    import pandas as pd
    from sklearn import linear_model

    '''This function performs creates a multiple linear regression using all predictor variables to predict a state's adjusted cohort graduation rate, or AGCR. It returs a dataframe with the coefficients for each variable, as well as the r-squared values
    and intercept for each model.'''

    predictors = df[[f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"]]

    regression_df = pd.DataFrame(index = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"], \
    columns = ["Graduation Rate Coefficient"])

    regression_obj = linear_model.LinearRegression()
    regression_obj.fit(predictors, df["2017-2018 ACGR"])
    r_squared = regression_obj.score(predictors, df["2017-2018 ACGR"])
    intercept = regression_obj.intercept_
    regression_df.loc[:, "Graduation Rate Coefficient"] = regression_obj.coef_

    return (regression_df, r_squared, intercept)

def insight5(df):
    import numpy as np
    import pandas as pd

    predictor_cols = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"]

    outcome_cols = ["2017-2018 ACGR", "2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"]

    predictor_summaries = pd.DataFrame(index = [f"% of Revenue from Federal Sources", f"% of Revenue from State Sources", f"% of Revenue from Local Sources", f"% of Current Spending on Instruction", \
    f"% of Current Spending on Support Services", f"Instruction as a % of Total Salaries/Wages", "Total Revenue/Student", "Total Expenditure/Student", "Total Current Spending/Student", "Current Spending on Instruction/Student"], \
    columns = ["Minimum", "1st Quartile", "Median", "3rd Quartile", "Maximum"])

    outcome_summaries = pd.DataFrame(index = ["2017-2018 ACGR", "2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"], columns = ["Minimum", "1st Quartile", "Median", "3rd Quartile", "Maximum"])

    for var in predictor_cols:
        predictor_summaries.loc[var, "Minimum"] = df[var].min()
        predictor_summaries.loc[var, "1st Quartile"] = np.percentile(df[var], 25)
        predictor_summaries.loc[var, "Median"] = np.percentile(df[var], 50)
        predictor_summaries.loc[var, "3rd Quartile"] = np.percentile(df[var], 75)
        predictor_summaries.loc[var, "Maximum"] = df[var].max()

    for var in outcome_cols:
        outcome_summaries.loc[var, "Minimum"] = df[var].min()
        outcome_summaries.loc[var, "1st Quartile"] = np.percentile(df[var], 25)
        outcome_summaries.loc[var, "Median"] = np.percentile(df[var], 50)
        outcome_summaries.loc[var, "3rd Quartile"] = np.percentile(df[var], 75)
        outcome_summaries.loc[var, "Maximum"] = df[var].max()

    return (predictor_summaries, outcome_summaries)
