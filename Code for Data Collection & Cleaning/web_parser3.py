"""This function uses BeautifulSoup to retrieve a table from the National Center for Education Statistics with the number of
students enrolled in public schools for every state. Since the website (and much of the table format) is the same as the one
used for the web_parser1 dataset, much of the code is very similar."""

def web_parser3():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    response_obj_3 = requests.get("https://nces.ed.gov/programs/digest/d19/tables/dt19_203.20.asp")
    soup_obj_3 = BeautifulSoup(response_obj_3.text, "html.parser")

    student_enrollment_df = pd.DataFrame(columns = ["Fall 2017 Enrollment"])

    table_row_tags = soup_obj_3.find_all("tr")
    state_row_tags = table_row_tags[14:65]

    for state_row in state_row_tags:
        row_data = state_row.find_all("td")
        state_name = state_row.find("th").text
        student_enrollment_df.loc[str(state_name)] = int(row_data[12].text.replace(",", ""))

    student_enrollment_df.to_csv("Public School Enrollment by State.csv", index = True)
