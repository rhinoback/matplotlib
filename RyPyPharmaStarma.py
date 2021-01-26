#!/usr/bin/env python
# coding: utf-8

# # Pymaceuticals Inc.
# ---
# 
# ### Observations and Insights
# - *Your observations and insights here* ...
# 

# In[30]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
mudy_data_complete = pd.merge(study_results, mouse_metadata, how="left")

# Display the data table for preview
mudy_data_complete.head()


# In[ ]:





# In[31]:


#Part 1
#Checking the number of mice.
number_mice= mudy_data_complete["Mouse ID"].nunique()
number_mice=249
# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
dup_mouse = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]=="g989", :]
# Optional: Get all the data for the duplicate mouse ID. 
print(dup_mouse)
dupli_mous_ID = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]=="g989", :]
dupli_mous_ID
# Create a clean DataFrame by dropping the duplicate mouse by its ID.

mudy_comp_clean_df = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]!="g989", :]
mudy_comp_clean_df
# Checking the number of mice in the clean DataFrame.
mudy_comp_clean_df["Mouse ID"].nunique()

#part 2

# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.


#mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).median()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).var()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).std()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).sem()["Tumor Volume (mm3)"]

#summary_df= #assinging these values to new columns

summary_stats_df=pd.DataFrame({
    "MeanTumVol":mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"],
    "MedianTumVol":mudy_data_complete.groupby(["Drug Regimen"]).median()["Tumor Volume (mm3)"],
    "TumVolVar":mudy_data_complete.groupby(["Drug Regimen"]).var()["Tumor Volume (mm3)"],
    "TumVolStdDev":mudy_data_complete.groupby(["Drug Regimen"]).std()["Tumor Volume (mm3)"],
    "TumVolSEM":mudy_data_complete.groupby(["Drug Regimen"]).sem()["Tumor Volume (mm3)"],
})

summary_stats_df


# In[ ]:





# In[32]:


mice_unique=mudy_data_complete["Mouse ID"].unique()
print(mice_unique)


# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:



dupli_mous_ID = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]=="g989", :]
dupli_mous_ID
# Create a clean DataFrame by dropping the duplicate mouse by its ID.

mudy_comp_clean_df = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]!="g989", :]
mudy_comp_clean_df
# Checking the number of mice in the clean DataFrame.
mudy_comp_clean_df["Mouse ID"].nunique()


# In[34]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.

mudy_comp_clean_df = mudy_data_complete.loc[mudy_data_complete["Mouse ID" ]!="g989", :]
mudy_comp_clean_df
# Checking the number of mice in the clean DataFrame.
mudy_comp_clean_df["Mouse ID"].nunique()


# In[74]:


mcc_df= mudy_comp_clean_df
mcc_df


# In[84]:


print(mcc_df[["Mouse ID", "Sex"]])


# In[ ]:





# In[ ]:





# ## Summary Statistics

# In[36]:


Capomulin 	40.675741 	41.557809 	24.947764 	4.994774 	0.329346
Ceftamin 	52.591172 	51.776157 	39.290177 	6.268188 	0.469821
Infubinol 	52.884795 	51.820584 	43.128684 	6.567243 	0.492236
Ketapril 	55.235638 	53.698743 	68.553577 	8.279709 	0.603860
Naftisol 	54.331565 	52.509285 	66.173479 	8.134708 	0.596466
Placebo 	54.033581 	52.288934 	61.168083 	7.821003 	0.581331
Propriva 	52.320930 	50.446266 	43.852013 	6.622085 	0.544332
Ramicane 	40.216745 	40.673236 	23.486704 	4.846308 	0.320955
Stelasyn 	54.233149 	52.431737 	59.450562 	7.710419 	0.573111
Zoniferol


# In[37]:





# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.


#mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).median()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).var()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).std()["Tumor Volume (mm3)"]
#mudy_data_complete.groupby(["Drug Regimen"]).sem()["Tumor Volume (mm3)"]

#summary_df= #assinging these values to new columns

summary_stats_df=pd.DataFrame({
    "MeanTumVol":mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"],
    "MedianTumVol":mudy_data_complete.groupby(["Drug Regimen"]).median()["Tumor Volume (mm3)"],
    "TumVolVar":mudy_data_complete.groupby(["Drug Regimen"]).var()["Tumor Volume (mm3)"],
    "TumVolStdDev":mudy_data_complete.groupby(["Drug Regimen"]).std()["Tumor Volume (mm3)"],
    "TumVolSEM":mudy_data_complete.groupby(["Drug Regimen"]).sem()["Tumor Volume (mm3)"],
})

summary_stats_df


# In[38]:


mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"]


# In[39]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Using the aggregation method, produce the same summary statistics in a single line
mudy_data_complete.groupby(["Drug Regimen"]).mean()["Tumor Volume (mm3)"]


# ## Bar and Pie Charts

# In[49]:


#data for graphs
summary_stats_df=pd.DataFrame({
    "MeanTumVolCnt":mudy_data_complete.groupby(["Drug Regimen"]).count()["Tumor Volume (mm3)"],
    "MedianTumVolCnt":mudy_data_complete.groupby(["Drug Regimen"]).count()["Tumor Volume (mm3)"],
    "TumVolVarCnt":mudy_data_complete.groupby(["Drug Regimen"]).count()["Tumor Volume (mm3)"],
    "TumVolStdDevCnt":mudy_data_complete.groupby(["Drug Regimen"]).count()["Tumor Volume (mm3)"],
    "TumVolSEMCnt":mudy_data_complete.groupby(["Drug Regimen"]).count()["Tumor Volume (mm3)"],
})

summary_stats_df


# In[ ]:


230, 178, 178, 188, 186, 181, 161, 228, 181, 182


# In[50]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[54]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas.
#loc?  



# In[67]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using using pyplot.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Capomulin', 'Ramicane', 'Ketapril', 'Naftisol', 'Zoniferol','Placebo','Stelasyn', 'Infubinol','Ceftamin','Propriva']
men_means = [230, 178, 178, 188, 186, 181, 161, 228, 181, 182]
#women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
#rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Unique Mice Tested')
ax.set_xlabel("Drug Regimen")
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()

plt.show()


# In[20]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using using pyplot.


# In[11]:


# Generate a pie plot showing the distribution of female versus male mice using pandas


# In[64]:


# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
# Load in csv
male_female= pd.read_csv("Resources/avg_rain_state.csv")
rain_df.head()

# Labels for the sections of our pie chart
labels = ["Male","Female"]

# The values of each section of the pie chart
sizes = [51, 49]

# The colors of each section of the pie chart
colors = ["orange", "lightskyblue"]

# Tells matplotlib to seperate the "Humans" section from the others
explode = (0.1, 0)


# In[65]:


# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)

# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")


# In[66]:


import matplotlib.pyplot as plt

# Some data
labels = 'Men','Women'
fracs = [51,49]

# Make figure and axes
fig, axs = plt.subplots(2, 2)

# A standard pie plot
axs[0, 0].pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

# Shift the second slice using explode
axs[0, 1].pie(fracs, labels=labels, autopct='%.0f%%', shadow=True,
              explode=(0, 0.1, 0, 0))


# In[83]:


# Adapt radius and text size for a smaller pie
patches, texts, autotexts = axs[1, 0].pie(fracs, labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=True, radius=0.5)
# Make percent texts even smaller
plt.setp(autotexts, size='x-small')
autotexts[0].set_color('white')

# Use a smaller explode and turn of the shadow for better visibility
patches, texts, autotexts = axs[1, 1].pie(fracs, labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=False, radius=0.5,
                                          explode=(0, 0.05, 0, 0))
plt.setp(autotexts, size='x-small')
autotexts[0].set_color('white')

plt.show()


# In[12]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot


# ## Quartiles, Outliers and Boxplots

# In[13]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

# Start by getting the last (greatest) timepoint for each mouse

# Merge this group df with the original dataframe to get the tumor volume at the last timepoint


# In[14]:


# Put treatments into a list for for loop (and later for plot labels)
treatment_list = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_list = []

# Calculate the IQR and quantitatively determine if there are any potential outliers. 
for drug in treatment_list:
    
    # Locate the rows which contain mice on each drug and get the tumor volumes
    
    # add subset 
    
    # Determine outliers using upper and lower bounds


# In[15]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


# ## Line and Scatter Plots

# In[102]:




tum = [40, 50, 1]
days = [0, 50, 10]

fig, ax = plt.subplots()
ax.plot(days, tum, label="tum")
#ax.legend()

plt.show()


# In[103]:





# In[17]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen


# In[ ]:




