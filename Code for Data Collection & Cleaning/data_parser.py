''' This function reads a downloaded dataset (located in your local directory) into a dataframe using Pandas,
cleans the data (drops unnecessary columns, renames columns to make more sense, aggregates on certain columns,
and finally writes the resulting dataframe to an excel file). If you'd like to run this in your command line,
you must call the function below the definition.'''

def data_parser():
  import pandas as pd
  import numpy as np

  df = pd.read_excel('elsec18.xls') #Although this is 1997 Excel file, read_excel still works.

  ''' First, I am going to go through the dataframe and remove any columns that I don't believe are valuable
  for our analysis later on. Some cells of the .xls could be of value, while others are very small subcategories
  of a larger variable. We can always revisit which ones we think are of value if we need more insights.'''

  df_main = df.drop(["IDCENSUS", "NAME", "YRDATA", "CONUM", "CSA", "CBSA", "SCHLEV", "NCESID", "V33", "F12", "G15", "K09", "K10", "K11", "J99",
          "L12", "M12", "Q11", "I86", "V11", "V13", "V15", "V17", "V21", "V23", "V37", "V29", "V10", "V12", "V14", "V16", "V18",
          "V22", "V24", "V38", "V30", "V32", "_19H", "_21F", "_31F", "_41F", "_61V", "_66V", "W01", "W31", "W61", "C14", "C15", "B11", "C20",
          "C25", "C36", "B10", "B12", "B13", "C01", "C05", "C07", "C10", "C11", "C12", "C24", "C35", "C38", "C39", "T06", "E13", "J13", "J12",
          "J14", "V91", "V92", "E17", "E07", "E08", "E09", "V40", "V45", "V90", "V85", "J17", "J07", "J08", "J09", "J40", "J45", "J90",
          "J11", "J96", "TCUROTH", "E11", "V60", "V65", "J10", "J97", "NONELSEC", "V70", "V75", "V80", "J98", "T02", "T06", "T09", "T15", "T40",
          "T99", "D11", "A09", "A11", "A13", "A15", "A20", "A40", "U11", "U22", "U30", "U97", "C13"], axis = 1)

  '''Next, I am taking the condensed df (clean of all columns we do not want), and I am renaming the columns we are using
  to more user-friendly titles. Notice not all are changed, this is because I am unsure if we want to go forward using that
  variable for analysis.'''

  df_main.rename(columns= {"STATE": "State", "TOTALREV": "Total Revenue", "TFEDREV": "Total Revenue from Federal Sources",
      "C16": "Revenue - Math, Science, & Teacher Quality", "C17": "Revenue - Safe & Drug-Free Schools", "C19": "Revenue - Vocational Education",
      "TSTREV": "Total Revenue from State Sources", "TLOCREV": "Total Revenue from Local Sources", "TOTALEXP": "Total Expenditures", "TCURELSC": "Total Current Spending",
      "TCURINST": "Total Current Spending (Instruction)", "TCURSSVC": "Total Current Spending (Support Services)", "TCAPOUT": "Total Capital Outlay Expenditure",
      "Z32": "Total Salaries and Wages", "Z33": "Total Salaries and Wages (Instruction)", "Z34": "Total Employee Benefit Payments"}, inplace = True)

  ''' In this section, I am creating new dfs by summing the total of a certain factor (in the original df)
  and grouping by State Code. The result is a bunch of dfs representing the total (of a factor) for each State.
  The goal is to merge all of these together to produce a final df we want to clean/export.'''

  t_r = df_main.groupby("State")["Total Revenue"].sum()                                           # Find Total Revenue
  t_r_fed = df_main.groupby("State")["Total Revenue from Federal Sources"].sum()                  # Find Total Revenue from Federal Sources
  t_r_state = df_main.groupby("State")["Total Revenue from State Sources"].sum()                  # Find Total Revenue from State Sources
  t_r_local = df_main.groupby("State")["Total Revenue from Local Sources"].sum()                  # Find Total Revenue from Local Sources
  t_exp = df_main.groupby("State")["Total Expenditures"].sum()                                    # Find Total Expenditures
  t_spending = df_main.groupby("State")["Total Current Spending"].sum()                           # Find Total Current Spending
  t_spending_inst = df_main.groupby("State")["Total Current Spending (Instruction)"].sum()        # Find Total Current Spending on Instruction
  t_spending_support = df_main.groupby("State")["Total Current Spending (Support Services)"].sum() # Find Total Current Spending on Support Services
  t_sal = df_main.groupby("State")["Total Salaries and Wages"].sum()                              # Find Total Salaries and Wages
  t_sal_inst = df_main.groupby("State")["Total Salaries and Wages (Instruction)"].sum()           # Find Total Salries and Wages on Instruction

  # MERGE WHAT WE WANT TOGETHER & CHANGE STATE CODES TO STATE NAMES
  merge_df = pd.concat([t_r, t_r_fed, t_r_state, t_r_local, t_exp, t_spending, t_spending_inst, t_spending_support, t_sal, t_sal_inst], axis = 1)
  merge_df.rename(index = {1: "Alabama", 2: "Alaska", 3: "Arizona", 4: "Arkansas", 5: "California", 6: "Colorado", 7: "Connecticut",
      8: "Delaware", 9: "District of Columbia", 10: "Florida", 11: "Georgia", 12: "Hawaii", 13: "Idaho", 14: "Illinois", 15: "Indiana",
      16: "Iowa", 17: "Kansas", 18: "Kentucky", 19: "Louisiana", 20: "Maine", 21: "Maryland", 22: "Massachusetts", 23: "Michigan",
      24: "Minnesota", 25: "Mississippi", 26: "Missouri", 27: "Montana", 28: "Nebraska", 29: "Nevada", 30: "New Hampshire",
      31: "New Jersey", 32: "New Mexico", 33: "New York", 34: "North Carolina", 35: "North Dakota", 36: "Ohio", 37: "Oklahoma",
      38: "Oregon", 39: "Pennsylvania", 40: "Rhode Island", 41: "South Carolina", 42: "South Dakota", 43: "Tennessee", 44: "Texas",
      45: "Utah", 46: "Vermont", 47: "Virginia", 48: "Washington", 49: "West Virginia", 50: "Wisconsin", 51: "Wyoming"}, inplace = True)

  ''' In this section, I am adding columns to our merge_df that standardize the data. I will be creating columns that represent
  percentages of an total variable (i.e., % of Total Rev from Federal Sources). Once the standardized column is created, I am
  deleting the columns that are now of no use (i.e., the Total Revenue from Federal Sources column).'''

  merge_df[r"% of Revenue from Federal Sources"] = round(merge_df["Total Revenue from Federal Sources"] / merge_df["Total Revenue"], 4)
  merge_df[r"% of Revenue from State Sources"] = round(merge_df["Total Revenue from State Sources"] / merge_df["Total Revenue"], 4)
  merge_df[r"% of Revenue from Local Sources"] = round(merge_df["Total Revenue from Local Sources"] / merge_df["Total Revenue"], 4)
  merge_df[r"% of Current Spending on Instruction"] = round(merge_df["Total Current Spending (Instruction)"] / merge_df["Total Current Spending"], 4)
  merge_df[r"% of Current Spending on Support Services"] = round(merge_df["Total Current Spending (Support Services)"] / merge_df["Total Current Spending"], 4)
  merge_df[r"Instruction as a % of Total Salaries/Wages"] = round(merge_df["Total Salaries and Wages (Instruction)"] / merge_df["Total Salaries and Wages"], 4)
  merge_df.drop(["Total Revenue from Federal Sources", "Total Revenue from State Sources", "Total Revenue from Local Sources",
      "Total Current Spending (Instruction)", "Total Current Spending (Support Services)", "Total Salaries and Wages (Instruction)"], axis = 1, inplace = True)

  ''' Finally, I am going to write the cleaned dataframe to a .xlsx file. In the analysis stage, we will combine all of our dataframes.'''

  writer = pd.ExcelWriter("2018 Public Elementary-Secondary Education Financial Data.xlsx")
  merge_df.to_excel(writer)
  writer.save()
