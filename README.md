# CS2316-FinalProject
Below will be a small summary of the final project my partner Robert & I had to completed for a CS class at Georgia Tech. Feel free to navigate the repository and look at what we found. Of course, DO NOT reuse any of this code for personal use (such as for a project at your school). 

There are separate folders containing code we used to gather/clean/export our data (including reasoning behind selecting sources and links to those sources) & code we used for analysis of the data (including images of our insights and visualizations). 

## Analyzing Relationships Between Educational Spending and Student Performance

**About this Project:**
* _Prepared by - P. Quarles & R. Weimar (insert GitHub username if he has one)_
* _Prepared for - CS 2316 (Data Input/Manipulation for Science and Industry) at Georgia Tech_

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
