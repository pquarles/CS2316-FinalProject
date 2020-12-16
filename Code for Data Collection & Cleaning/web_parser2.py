  """This function retrieves reading and math scores from the National Assessment of Educational Progress via their web API.
  However, each state's score for one exam is stored at a different URL, so I actually have to make 102 separate requests to retrieve the data.
  I accomplish this by using a for loop to build a URL string for each state in the format specified in the API documentation, and then extracting
  the relevant JSON data. In order to conduct these requests ethically and avoid any trouble, I use time.sleep(1) to instruct Python to
  pause for one second in between each request. Finally, it adds is retrieved to a dataframe and exports to a CSV."""

def web_parser2():
  import time
  import requests
  import pandas as pd

  naep_scores_df = pd.DataFrame(index = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"], columns = ["2019 Average NAEP Math Score", "2019 Average NAEP Reading Score"])
  math_column = []
  reading_column = []

  for state in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]:
      for subject in [("mathematics", "MRPCM"), ("reading", "RRPCM")]:
          response_obj_2 = requests.get("https://www.nationsreportcard.gov/NRCDataService/GetAdhocData.aspx?type=data&subject=" + subject[0] + "&grade=8&subscale=" + subject[1] + "&jurisdiction=" + state + "&variable=SCHTYPE&Year=2019&stattype=MN:MN")
          data_dict = response_obj_2.json()

          """Once I have retrieved the dictionary for the given state and subject, I retrieve the average score from the dictionary as a float and append it to the correct column."""

          avg_score = float(data_dict["result"][0]["value"])

          if subject[0] == "mathematics":
              math_column.append(float(avg_score))
          else:
              reading_column.append(float(avg_score))

          time.sleep(1)

  """Once I have obtained the columns, I add them each to the empty dataframe I created earlier."""

  naep_scores_df.loc[:, "2019 Average NAEP Math Score"] = math_column
  naep_scores_df.loc[:, "2019 Average NAEP Reading Score"] = reading_column

  """Lastly, I export the completed dataframe as a csv file."""

  naep_scores_df.to_csv("NAEP Reading and Math Scores by State.csv", index = True)
