### df_concatenation ###

def df_concatenation():
  import pandas as pd
  import numpy as np

  ''' I'm going to read in all of the clean data we exported in Phase 1 to different dataframes,
  and then concatenate them horizontally, with state names remaining as the index.'''

  finance_df = pd.read_excel("2018 Public Elementary-Secondary Education Financial Data.xlsx", index_col = 0)
  graduation_rates_df = pd.read_csv("Graduation Rates by State.csv", delimiter = ",", index_col = 0)
  naep_scores_df = pd.read_csv("NAEP Reading and Math Scores by State.csv", delimiter = ",", index_col = 0)
  student_enrollment_df = pd.read_csv("Public School Enrollment by State.csv", delimiter = ",", index_col = 0)

  agg_df = pd.concat([finance_df, graduation_rates_df, naep_scores_df, student_enrollment_df], axis = 1)

  ''' Since our financial data is only dealing with the 2017-2018 years, I'm going to drop
  graduation rate columns for school years from beg of 2010 through end 2017. Also, I will
  standardize our revenue/expenditure/current spending variables by dividing them by the #
  of enrolled public school students for that calendar year.'''

  agg_df.drop(["2010-2011 ACGR", "2011-2012 ACGR", "2012-2013 ACGR", "2013-2014 ACGR", "2014-2015 ACGR",
      "2015-2016 ACGR", "2016-2017 ACGR", "Average ACGR 2010-2018"], axis = 1, inplace = True)

  agg_df["Total Revenue/Student"] = round((agg_df["Total Revenue"] / agg_df["Fall 2017 Enrollment"])*1000 , 2)
  agg_df["Total Expenditure/Student"] = round((agg_df["Total Expenditures"] / agg_df["Fall 2017 Enrollment"])*1000 , 2)
  agg_df["Total Current Spending/Student"] = round((agg_df["Total Current Spending"] / agg_df["Fall 2017 Enrollment"])*1000 , 2)
  agg_df["Current Spending on Instruction/Student"] = round(((agg_df[r"% of Current Spending on Instruction"]*agg_df["Total Current Spending"]) / agg_df["Fall 2017 Enrollment"])*1000 , 2)

  ''' Finally, I will write the dataframe containing our predictor and response variables
  to a csv file, as well as return the dataframe. This way, we can import the dataframe later for analysis.'''

  return agg_df
