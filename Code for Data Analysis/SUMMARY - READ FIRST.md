# Data Analysis Section 
Here we were asked to use the data we cleaned previously to search for insights & create visualizations with it. Our project required that we find 5 insights & create 3 visualizations.

Within this README, we will break down a description of each function that is used to discover an insight or create a visualization. We will also use a SOURCES.md file to list out some 
documentation and files we used for this analysis stage. 

Within this folder, we will attach the 3 .py files-- 
* "df_concatenation" is a function that combined all of our clean data from before into one dataframe/CSV that we used for all of 
the analysis; 
* "insights" has all 5 insight functions within it; and 
* "visualizations" has all 3 visualization functions within it. 

Note: If you download and try to run these files, it's likely they will not work, as you'd need to install a number of modules used, as well as some extra files that are in SOURCES.md


# Insights 
## Insight 1 - 
* For our first insight, we wanted to determine whether there was any linear correlation whatsoever between educational spending and academic outcomes. The following function produces a dataframe with the correlation r between each individual predictor variable and each individual outcome variable. The results showed that certain variables did in fact have medium to strong correlations with our outcome variables, particularly % of Revenue from Federal Sources, % of Current Spending on Instruction, and Current Spending on Instruction per Student. The correlations for the NAEP reading and math scores were generally similar to one another, and generally higher than those for high school graduation rates.

## Insight 2 - 
* The following function returns a dataframe that contains the Top 10 states that spend the most on instruction per student (sorted descending). It has columns representing the boolean of whether or not the state's Average NAEP Math/Reading Score was above the 80% percentile for all average scores. As you can see, it's insightful that 4 out of the top 5 states did perform better than others, and this could be attributed to their spending on instruction. However, it's also important to note that Pennsylvania and New York both spend large amounts of money on instruction per student, yet they both did not perform above the 80th percentile. 

## Insight 3 - 
* Having determined in insight 1 that several predictor variables are relatively correlated with NAEP math and reading scores, we now will run two multiple regression models, one for math scores and the other for reading. The function below finds the linear regression coefficients for each predictor variable, the intercept of the line of best fit, and the r-squared value. The models yielded r-squared values of 0.4471 for math and 0.5468 for reading, indicating that a substantial amount of the variation in NAEP test scores could be explained by our predictor variables.

## Insight 4 - 
* We wanted to see if we could create a linear regression model to predict states' high school graduation rates as well. Initially, we didn't expect our model to fit the data well, since the correlation values obtained in insight 1 for graduation rates were noticeably lower than those for NAEP Reading and Math scores. However, running multiple regression with all predictors yielded an r-squared of 0.4487, which indicates that certain types of educational spending could in fact have a tangible effect on high school graduation rates.

## Insight 5 - 
* The following function returns a five-number summary (minimum, 1st quartile, median, 3rd quartile, and maximum) for all predictor variables. This allowed us to analyze the distributions of each of our variables and better understand how much each value varied. Certain variables, like % of Revenue from State Sources and % of Revenue from Local Sources, had very wide-ranging minimum and maximum values, in part due to the inclusion of the District of Columbia, which receives no state funding and relies upon local funding almost entirely. Total Current Spending per Student ranged all the way from \$6,760 to $24,120.

# Visualizations
## Visualization 1 - 
* Visualization 1 creates a figure composed of various sub-plots. The y-axis shows 3 different outcome variables: 2019 Average NAEP Math Score (Red Color), 2019 Average NAEP Reading Score (Blue Color), and 2017-2018 ACGR (Green Color). The x-axis shows 3 different predictor variables that are being plotted against the y-axis: Total Current Spending/Student, Total Expenditure/Student, and Current Spending on Instruction/Student. 
* This visualization exhibits the different trends between outcome and predictor variables. As you can see, ACGR (Average Cohort Graduation Rate) does not have much of a correlation with any of the predictor variables, but both the Average NAEP Math & Reading Scores have moderate positive correlations with the predictor variables.  

## Visualization 2 - 
* Visualization 2 utilizes the GeoPandas module to create a choropleth map showing which states spend the most per student. The map excludes Alaska & Hawaii, as those two states stretched the plot out too much and made for a less appealing/useful visual. There is a legend contained below the plot to explain the color scheme and ranges of spending. 
* This visualization is meaningful because of it's ability to show disparities in how much certain states currently spend per student. As you can see, the Northeast spends drastically more than the midwest & most parts of the nation do.  

## Visualization 3 - 
* Visualization 3 explores the distribution of 2019 Average NAEP Scores & the Percent of Current Spending on Instruction. Two histograms are used-- both showing that all 3 variables follow a relatively normal shaped distribution. Visualization 3 further explores the relationship between Spending on Instruction and the 2019 Average NAEP scores, with a regression line fitted to both Reading and Math scores to display meaning. We found that for every 1% increase in Percent of Current Spending on Instruction, there is a 64.65 point score increase for Reading and 83.83 point increase for Math. Essentially, if a state increased their Spending on Instruction from 50% to 60%, our regression line shows this could potentially increase their NAEP scores for Reading by an average of 8.4 points. 
