# CS2316-FinalProject
Below will be a small summary of the final project my partner Robert & I had to completed for a CS class at Georgia Tech. Feel free to navigate the repository and look at what we found. Of course, DO NOT reuse any of this code for personal use (such as for a project at your school). 

There are separate folders containing code we used to gather/clean/export our data (including reasoning behind selecting sources and links to those sources) & code we used for analysis of the data (including images of our insights and visualizations). 

## Analyzing Relationships Between Educational Spending and Student Performance

**About this Project:**
* _Prepared by - P. Quarles & R. Weimar (insert GitHub username if he has one)_
* _Prepared for - CS 2316 (Data Input/Manipulation for Science and Industry) at Georgia Tech_

**Point of Interest / Purpose:** 
  * We were interested in discovering any correlations between how money is allocated within states' school departments for public primary-secondary schools and resulting educational outcomes.
  * Purpose - We hoped to be able to determine whether or not policymakers can expect an increase in student educational outcomes by increasing state school funding, and which   income/expense metrics for school systems are most closely related to student performance.
  * To measure educational outcomes, we will analyze each state’s high school graduation rates and average 8th grade Reading and Mathematics scores from the National Assessment of Educational Progress, a standardized test taken by a representative sample of students in the United States.
    
**Programming Languages / Modules:** 
  * All coding was completed using Python
  * Within Python, a number a modules were utilized:
    * Pandas to import data, use dataframes, aggregate data, perform calculations, etc.
    * NumPy for various calculations
    * Requests / BeautifulSoup to gather web data
    * Scipy.stats.pearsonr for correlation 
    * Sklearn for multiple regression
    * Matplotlib for visualizations & plotting
    * GeoPandas (utilizing a bunch of other dependencies) for visualization - required downloading a .shx file from US Census Bureau to overlay with GeoPandas 
      
 **Data Collection Process:** 
   * Utilized a downloaded dataset:
     * __Revenues and expenditures by category for all US school districts__, which we grouped together by state; obtained from the US Census Bureau, and downloaded as an Excel file along with a Word document to understand cell key references.
   * Also used data from 3 web sources:
     * __High school graduation rates by state__; scraped from National Center for Education Statistics using BeautifulSoup module of Python
     * __Average NAEP 8th grade Mathematics and Reading Scores by state__; obtained via the NAEP API using the requests module of Python
     * __K-12 public school enrollment by state__; obtained from the National Center for Education Statistics using BeautifulSoup; we used this in order to convert raw educational spending values into spending per student
      
**Data Cleaning Process:**

_Downloaded Dataset_ 
* This dataset contains all the revenue and expenditure variables for public elementary-secondary school systems in America. We plan to use data gathered from this as our predictor variables in our final analysis, as we will want to see how these variables correlate or possibly affect educational outcomes from each state. 
* We intend to collect this data by downloading the Excel file with all of the data contained in it and reading it from an .xls format into a Pandas dataframe with the Pandas module. The next step to cleaning this data is to fully understand what each of the column headers refer to (some are cell names, some are text, etc.) by reading through the 'school18doc.doc' that contains all the keys to state codes and column variables.
* After understanding what columns are of value and which ones are not, we intend to use the df.drop() function to condense the dataframe to a more workable size. Furthermore, we'll use the df.rename() function to change column headers to what they are meant to represent (i.e., changing "Z32" to "Total Salaries and Wages") so we can better understand what we are looking at when working with the data later on. 
* Then, since every row is still referring to a different county, we intend to consolidate the data by grouping each valuable variable by State Code and finding the sum of all the rows correlating to that state. Basically, we will create a number of dataframes that group the sum of each variable by state. 
* After grouping, we plan to concatenate all of the different variable dataframes into what we call the "merged dataframe." This will leave us with each state code as an index in the dataframe, and each column header as variable that has been aggregated by state. We will then use df.rename() to change all the state codes to their respective states (found in the 'school18doc.doc'). 
* Finally, we plan to create various new columns in the merged dataframe that standardize some of the data we already have. For example, we may create a column called "% Rev from Federal Sources" that will divide the "Total Rev from Federal" column by the "Total Revenue" column. After this, we'll .drop() any unnecessary columns used for calculation purposes only & write the final merged dataframe to an Excel file for later analysis. 

_Web Collection #1_
* This website has a table with each state's adjusted high school graduation rates by school year, from 2010-2011 to 2017-2018. We will use this data as one of our dependent variables in our analysis.
* We will first scrape and parse this data using requests.get() and BeautifulSoup. We will then use the .find_all() method to locate the table row tags, and then select only those tags representing the desired rows in the table.
* We will then place each row in a Pandas dataframe, using the state name as an index and placing each school year's graduation rate in a different column. We will clean the data by converting data to floats, manually replacing missing values with np.nan, and removing any superscripted numbers representing footnote references in the original table. 
* Finally, we will add a column for the average graduation rate across all years, avoiding missing values in our calculation.

_Web Collection #2_
* This API provides states' scores on the National Assessment of Educational Progress, a standardized exam taken by a representative sample of 4th, 8th, and 12th graders nationwide. We will use the API to obtain grade 8 scores from public schools in every state for both the reading and math exams. However, each state average for a specific subject is stored at a different endpoint, so we will have to make 102 requests for all 50 states and the District of Columbia.
* We will make each request using requests.get(), and then parse the data, which is stored in json format, using the .json() method. In order to make these requests efficiently, we will use two for loops to build the URL for each request as a string. One for loop will iterate through the state element of the URL, and the other will iterate through the two exam subjects for each state.
* We will then convert the data to floats and add it to a dataframe with two columns, one for reading scores and one for math scores, and state names as indices.

_Additional Web Collection_
* This additional dataset is essential because it describes the total public school enrollment in every state, which we will use later to calculate the per student spending/revenue for each state, which allows us to compare each state's budgets on a fair basis.
* This data is from the same source as our web requirement #1, so the steps for scraping it are largely the same; we will use requests.get() and BeautifulSoup to parse the HTML, and then use .find_all() to find the table row tags. 
* The data will need to be cleaned slightly by first removing the commas in the numbers, and then converting into integers. We will then place the data in a dataframe with a single column and state names as indices.

__Data Analysis:__
* PLEASE SEE "SUMMARY - READ FIRST.md" within the "Code for Data Analysis" folder. 

__Conclusions:__
* Overall, several metrics of per student educational spending were positively correlated with standardized test scores, and to a lesser extent, higher high school graduation rates.
* Performing multiple regression with all predictors of NAEP Math scores, NAEP Reading scores, and high school graduation rates yielded r-squared values of 0.4471, 0.5468, and 0.4487, respectively, which suggests that a significant amount of the variation in test scores and graduation rates could be explained by our predictor variables.
* In conclusion, our results suggest that states with higher spending per student, a higher percentage of current spending on instruction, and a lower percentage of revenue from federal sources tend to have better educational outcomes, and that state and local policymakers could expect higher test scores and graduation rates by increasing their instructional spending.

