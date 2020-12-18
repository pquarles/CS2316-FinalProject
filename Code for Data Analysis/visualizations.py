### visualizations.py ###

''' NOTE - all functions take in 'df' as an argument. df is a variable that we assigned to our function df_concatenation()
that you can find within the folder (it stores our final dataframe we use for analysis).'''

def visual1(df):
  import matplotlib.pyplot as plt
  ''' Create a figure with 3x3 axis & name accordingly'''
  figure, axs = plt.subplots(3, 3, figsize= (15,15))
  figure.suptitle("Avg NAEP Scores & ACGR vs. Different Predictor Variables")

  ''' Plot variables against NAEP Scores from dataframe. Y Labels will be Reading/Math Scores, while
  X Labels are various different predictor variables.'''
  dataframe.plot(x= "Total Current Spending/Student", y= "2019 Average NAEP Math Score", kind= "scatter", color = "red", ax = axs[0,0])
  dataframe.plot(x= "Total Current Spending/Student", y= "2019 Average NAEP Reading Score", kind= "scatter", color = "blue", ax = axs[1,0])
  dataframe.plot(x= "Total Current Spending/Student", y= "2017-2018 ACGR", kind= "scatter", color = "green", ax = axs[2,0])

  dataframe.plot(x= "Total Expenditure/Student", y= "2019 Average NAEP Math Score", kind= "scatter", color = "red", ax = axs[0,1])
  dataframe.plot(x= "Total Expenditure/Student", y= "2019 Average NAEP Reading Score", kind= "scatter", color = "blue", ax = axs[1,1])
  dataframe.plot(x= "Total Expenditure/Student", y= "2017-2018 ACGR", kind= "scatter", color = "green", ax = axs[2,1])

  dataframe.plot(x= "Current Spending on Instruction/Student", y= "2019 Average NAEP Math Score", kind= "scatter", color = "red", ax = axs[0,2])
  dataframe.plot(x= "Current Spending on Instruction/Student", y= "2019 Average NAEP Reading Score", kind= "scatter", color = "blue", ax = axs[1,2])
  dataframe.plot(x= "Current Spending on Instruction/Student", y= "2017-2018 ACGR", kind= "scatter", color = "green", ax = axs[2,2])

  '''The following removes the x_labels/tick labels for top plots and y-ticks for right plots'''
  for ax in axs.flat:
      ax.label_outer()

def visual2(df):

  ### REFER TO CITED SOURCES BELOW -- FILES NEED TO BE DOWNLOADED, as well as GeoPandas module & its dependencies
  import pandas as pd
  import geopandas as gpd
  import matplotlib.pyplot as plt

  ''' To utilize GeoPandas, I had to download a .shx Shape file from the US Census Bureau.
  I had to construct a filepath on my system and ensure the .shx file was in the working environment.'''

  ### Create your Unique filepath below --- Mine is included for Example
  filepath = r"C:\Users\parke\Documents\S7 - GT Fall 2020\CS2316\# Final Project" + r"\cb_2018_us_state_500k.shx"
  df_states = gpd.read_file(filepath)

  ''' Here I'm going to rename the NAME column in our gpd dataframe to "State"
  so I can merge it easily with our data later on. Furthermore, I am going to drop
  a number of US Provinces that are not to be analyzed (Guam, Puerto Rico, etc.) '''
  df_states.rename(columns= {"NAME": "State"}, inplace= True)
  df_states.drop([13, 37, 38, 44, 45], axis = 0, inplace = True)

  # Create a subplot, with figure & axis / Define size & title
  figure, ax = plt.subplots(1, figsize= (10, 10))
  plt.title("Map of United States Current Spending/Student", size = 16)

  #Merge our dataframe with the gpd dataframe (on 'State')
  merged_map = pd.merge(df_states, dataframe, on="State")

  #Map everything except Alaska & Hawaii, as those 2 spread out the plot drastically
  merged_map = merged_map[(merged_map.State != "Alaska") & (merged_map.State != "Hawaii")]
  merged_map.plot(column= "Total Current Spending/Student",
      cmap='Greens',          #colormap for states
      linewidth=0.4,          #line width for borders
      ax= ax,                 #plot the map on current ax
      edgecolor='black',      #state border colors
      legend= True,           #include a legend, label it, and put it under the plot
      legend_kwds= {"label": "Current Spending/Student",
                      'orientation': 'horizontal'})

  #Save the figure & show the figure
  plt.savefig("Map of US Current Spending/Student.png")
  plt.show()

def visual3(df):
  import matplotlib.pyplot as plt
  import numpy as np

  ''' Visualization of one predictor variable with two of our outcome variables.'''
  fig, axs = plt.subplots(1, 3, figsize= (30, 20))
  fig.suptitle("Avg NAEP Scores & % of Current Spending on Instruction", size= 24)

  # Plot NAEP Reading/Math on the same hist to see distribution
  dataframe["2019 Average NAEP Reading Score"].plot(kind= "hist", color= "orange", edgecolor= "black", alpha= 0.5, ax= axs[0])
  dataframe["2019 Average NAEP Math Score"].plot(kind= "hist", color= "pink", edgecolor= "black", alpha= 0.5, ax= axs[0])
  axs[0].legend(labels= ["Reading", "Math"])
  axs[0].set_xlabel("2019 Average NAEP Scores", size= 16)
  axs[0].set_ylabel("Frequency", size=16)

  #Plot % of Spending on Instruction on hist to see distribution
  dataframe["% of Current Spending on Instruction"].plot(kind= "hist", color= "red", edgecolor="black", alpha= 0.5, ax= axs[1])
  axs[1].set_xlabel("% of Current Spending on Instruction", size= 16)
  axs[1].set_ylabel("Frequency", size= 16)

  #Find Regression lines for NAEP Scores vs % of Spending on Instruction
  reading_fit = np.polyfit(dataframe["% of Current Spending on Instruction"], dataframe["2019 Average NAEP Reading Score"], 1)
  math_fit = np.polyfit(dataframe["% of Current Spending on Instruction"], dataframe["2019 Average NAEP Math Score"], 1)

  #Plot our data on the same subplot, with X= NAEP Scores & Y= % of Spending on Instruction
  dataframe.plot(kind="scatter", x= "% of Current Spending on Instruction", y= "2019 Average NAEP Reading Score", color= "orange", alpha= 0.75, ax= axs[2])
  dataframe.plot(kind="scatter", x= "% of Current Spending on Instruction", y= "2019 Average NAEP Math Score", color= "pink", alpha=0.75, ax= axs[2])
  axs[2].legend(labels= ["Reading", "Math"])
  axs[2].set_ylabel("2019 Average NAEP Scores", size= 16)
  axs[2].set_xlabel("% of Current Spending on Instruction", size= 16)

  #Put Regression Lines on their with equations
  axs[2].plot(dataframe["% of Current Spending on Instruction"], reading_fit[0]*dataframe["% of Current Spending on Instruction"] + reading_fit[1], color= "orange", linewidth= 3)
  axs[2].plot(dataframe["% of Current Spending on Instruction"], math_fit[0]*dataframe["% of Current Spending on Instruction"] + math_fit[1], color= "pink", linewidth= 3)

  axs[2].text(.6, .25, 'y={:.2f}+{:.2f}*x'.format(reading_fit[1], reading_fit[0]), transform=axs[2].transAxes, color="darkorange", size=16)
  axs[2].text(.4, .85, 'y={:.2f}+{:.2f}*x'.format(math_fit[1], math_fit[0]), transform=axs[2].transAxes, color="deeppink", size=16)

  plt.savefig("Regression - Avg NAEP Scores & Percent of Current Spending on Instruction.png")
  plt.show()
