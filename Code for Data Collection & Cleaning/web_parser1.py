'''This function uses Requests and BeautifulSoup to scrape a table of high school graduation rates for each state.
It converts values to integers and addresses various inconsistencies (i.e., changing "---" to NaN).
Finally, it creates an average (while avoiding NaNs) across the years (2010-1028) and adds a column for it.
The final product is a Pandas dataframe showing Average Cohort Graduation Rate for each the years 2010-2018, which is exported to a CSV file.'''

def web_parser1():
  import requests
  from bs4 import BeautifulSoup
  import numpy as np
  import pandas as pd

  """This function uses BeautifulSoup to scrape a table of high school graduation rates for each state.
  I start by retrieving the html from the URL and finding the <tr> tags."""

  response_obj_1 = requests.get("https://nces.ed.gov/programs/digest/d19/tables/dt19_219.46.asp")
  soup_obj_1 = BeautifulSoup(response_obj_1.text, "html.parser")

  table_row_tags = soup_obj_1.find_all("tr")
  state_row_tags = table_row_tags[10:61]

  """Next, I create an empty dataframe with the correct column labels, and iterate through the <tr> tags,
  each of which corresponds to one state. I then add a row to the dataframe for each state with the state's
  name as the index and each year's average cohort graduation rate (ACGR) in their respective columns."""

  graduation_rates_df = pd.DataFrame(columns = ["2010-2011 ACGR", "2011-2012 ACGR", "2012-2013 ACGR", "2013-2014 ACGR", "2014-2015 ACGR", "2015-2016 ACGR", "2016-2017 ACGR", "2017-2018 ACGR"])

  for state_row in state_row_tags:
    row_data = state_row.find_all("td")
    state_name = state_row.find("th").text
    graduation_rates_df.loc[str(state_name)] = [str(row_data[n].text) for n in [0, 2, 4, 6, 7, 8, 9, 10]]

  """After that, I convert the values into integers and address various inconsistencies in the data. I remove a superscripted
  number from one of the row indices, and convert the empty cells from the table, which were marked as '---', to NaN."""

  for index in graduation_rates_df.index:
      for column in graduation_rates_df.columns:
          if graduation_rates_df.loc[index, column] != "---":
              graduation_rates_df.loc[index, column] = float(graduation_rates_df.loc[index, column])

  graduation_rates_df.rename(index = {"Alabama9" : "Alabama"}, inplace = True)

  graduation_rates_df = graduation_rates_df.replace(to_replace = "---", value = np.NaN)

  """Lastly, I create a column for the average graduate rate across all years for each state. I computed the average
  without using a dedicated function or method in order to avoid any issues stemming from NaN values. I then export the dataframe
  as a csv file."""

  avg_grad_rate_col = []
  for index in graduation_rates_df.index:
      rate_sum = 0
      count = 0
      for column in graduation_rates_df.columns:
          if not pd.isna(graduation_rates_df.loc[index, column]):
              rate_sum += graduation_rates_df.loc[index, column]
              count += 1
      avg_grad_rate_col.append(rate_sum / count)

  graduation_rates_df.loc[:, "Average ACGR 2010-2018"] = avg_grad_rate_col

  graduation_rates_df.to_csv("Graduation Rates by State.csv", index = True)
