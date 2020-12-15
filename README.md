# CS2316-FinalProject
Here is where I have the code hosted for my CS 2316 Final Project - Feel free to browse! Below will be a small summary of the project (more details may be added later). 

## Project Title
__Analyzing Relationships Between Educational Spending and Student Performance__
*Prepared for - CS 2316 (Data Input/Manipulation for Science and Industry) at Georgia Tech*

**Point of Interest / Purpose:** 
  * We were interested in discovering any correlations between how money is allocated within states' school departments and resulting educational outcomes.
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
      
  {To edit later -- include data cleaning process, include separate visualizations page, include separate insights page, include code pages}
