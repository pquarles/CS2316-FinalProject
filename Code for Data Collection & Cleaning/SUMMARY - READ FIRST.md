# Code for Data Collection & Cleaning

## What's going on here? 

In this folder, there will be a number of .py files that contain certain functions that were written to access data, clean it, and export it back to an excel file.
Each function writes the data to a Pandas dataframe; this is so all the data can be later aggregated into one dataframe for analysis. As per this project's requirements, 
we gather data from one government resource (the US Census Bureau) and 3 web sources. More information will be provided below:

## Description of Each File:

### data_parser.py
__What does this function do?__
* This function reads a downloaded dataset titled 'elsec18.xls' (from your local directory) into a dataframe using Pandas,
cleans the data (drops unnecessary columns, renames columns to make more sense, aggregates on certain columns, etc.)
and finally writes the resulting dataframe to an excel file. 

__About the Source__: 
* https://www.census.gov/data/tables/2018/econ/school-finances/secondary-education-finance.html
  * Download the "All Data Items" Excel file - Once downloaded, the filename is "elsec18.xls"
  * To understand column headings and state codes, supporting documentation will be needed. I may include it as a separate file & link to it later on. 
* We chose to use public school financial data from the Census Bureau website because it includes detailed information about financial revenue/expenses for each school district, which we will group together by state, and it breaks down larger revenue/expense variables into smaller sub-categories that we can use to standardize the information and draw insights from.

__Modules Used__:
* Pandas

### web_parser1.py
__What does this function do?__
* This function uses Requests and BeautifulSoup to scrape a table of high school graduation rates for each state. It converts values to integers and addresses various inconsistencies (i.e., changing "---" to NaN). Finally, it creates an average (while avoiding NaNs) across the years (2010-1028) and adds a column for it. The final product is a Pandas dataframe showing Average Cohort Graduation Rate for each the years 2010-2018, which is exported to a CSV file. 

__About the Source__: 
* https://nces.ed.gov/programs/digest/d19/tables/dt19_219.46.asp
* Our first web dataset is from the National Center for Education Statistics, and includes high school graduation rates by state. We will use this data as one of our outcome variables to measure whether states' enducational income/spending are correlated to their HS graduation rates.

__Modules Used__:
* Requests
* BeautifulSoup
* Numpy
* Pandas

### web_parser2.py
__What does this function do?__
* This function retrieves reading and math scores from the National Assessment of Educational Progress via their web API.
  However, each state's score for one exam is stored at a different URL, so I actually have to make 102 separate requests to retrieve the data.
  I accomplish this by using a for loop to build a URL string for each state in the format specified in the API documentation, and then extracting
  the relevant JSON data. In order to conduct these requests ethically and avoid any trouble, I use time.sleep(1) to instruct Python to
  pause for one second in between each request. 
* Once we have all the columns as lists, we add them an empty dataframe and export the dataframe to export as a CSV file. 

__About the Source__: 
* https://www.nationsreportcard.gov/api_documentation.aspx
  * Each data point in this API is stored at a different URL, so we had to make a total of 102 requests to retrieve all the data. A sample endpoint can be found here:
  * https://www.nationsreportcard.gov/NRCDataService/GetAdhocData.aspx?type=data&subject=mathematics&grade=8&subscale=MRPCM&jurisdiction=AL&variable=SCHTYPE&Year=2019&stattype=MN:MN
* Our second web dataset is an API with data on each state's performance on the National Assessment of Educational Progress, a standardized test with multiple subjects given to a representative sample of US 4th, 8th, and 12th grade students. (We chose this exam over the ACT and SAT because certain states mandate that all students take those exams while some do not, which drastically affects ACT and SAT averages in many states.)  We will use data from the math and reading exams to determine whether states' enducational income/spending is correlated with higher scores on each subject.

__Modules Used__:
* Time
* Requests
* Pandas

### web_parser3.py
__What does this function do?__
* This function uses BeautifulSoup to retrieve a table from the National Center for Education Statistics with the number of
students enrolled in public schools for every state. Since the website (and much of the table format) is the same as the one
used for the web collection requirement #1 dataset, much of the code is very similar.
* The purpose of this function is that so we can use this to create standardization amongst the data, converting revenue/spending variables to revenue/spending PER STUDENT variables. 

__About the Source__: 
* https://nces.ed.gov/programs/digest/d19/tables/dt19_203.20.asp
* Our additional web dataset is also from the National Center for Education Statistics, and contains information on total public school enrollment by state. We will use this information to divide each state's educational revenue and expenses by the number of students to get per student measures of each value. This is an essential step because it allows us to compare states with very large budgets, like California, and small ones, like Wyoming, on an equitable basis.

__Modules Used__:
* Requests
* BeautifulSoup
* Pandas
