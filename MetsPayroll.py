#!/usr/bin/env python
# coding: utf-8

# ## An Granular Analysis and Visualization of the Mets' 2022 Payroll
# - This analysis will be shown at website goes here 
# -    Goals: 
#         - To show a team-wide view of MLB Payrolls in 2022 and compares them to a team's win total
#         - To show a player-wide view of MLB Payrolls in 2022 and compares it to their team's win total
#         - To analyze a player's value with his salary group 
#         - To experiment with the package "Plotly" 

# In[74]:


#Importing the Necessary Packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[75]:


'''
Inspiration to use this package came from:
https://towardsdatascience.com/using-plotly-express-to-create-interactive-scatter-plots-3699d8279b9e
'''
import plotly.express as px


# In[76]:


#Importing the CSV and dropping the unneeded first column
done2 = pd.read_csv('yep2.csv')
done2= done2.drop(done2.columns[0], axis=1) #dropping the Count column


# ### EDA: Exploratory Data Analysis

# In[77]:


done2.info()


# In[78]:


done2.describe()


# In[79]:


done2.head()


# ### Data Cleanup

# In[80]:


#Changing the Payroll data to numeric and rounding it to the ones place 
done2['Payroll'] = pd.to_numeric(done2['Payroll'])
done2['Payroll'] = done2['Payroll'].apply(lambda x: round(x, 0))
done2.head()


# In[81]:


done2.rename(columns={"FA/Arb/Pre-Arb":'Contract_Status'}, inplace =True)


# In[82]:


done2.head()


# ### Player Visualizations 

# In[83]:


#The First Visualization presents a players' WAR by their salary 
viz =px.scatter(done2, x='Payroll', y='WAR',color='Name')
viz


# In[84]:


#The First Visualization presents a players' WAR by their salary group
viz4 =px.scatter(done2, x='Payroll', y='WAR',color='Contract_Status')
viz4


# #### Team/Salary Analysis 

# In[85]:


#Importing the CSV
TeamPayroll = pd.read_csv('TeamPayroll.csv')


# In[86]:


#Data Cleanup: sorting by the most important Metric, the y-axis will be in Millions, dividing by 100,000, and rounding the MilPerWin by 1 decimal point
Team =  TeamPayroll.sort_values(by=['MilPerWin'], ascending = False)
Team['MilPerWin'] = Team['MilPerWin'] /1000000
Team['MilPerWin'] = round(Team['MilPerWin'],1)


# In[87]:


#Looks a lot better if it's only 15 Teams and not 30 
Team = Team.head(15)
Team


# #### Team Visualizations 

# In[88]:


viz3 =px.bar(Team, x = 'Team', y='MilPerWin', text_auto =True) #Creates visualization
viz3.update_layout(title = 'The Top 15 Teams that Spent the Most For Each Win', title_x=0.5) #adds title
viz3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False) #puts the data on the outside of the bar

#The below adds the orange rectangle
import plotly.graph_objects as go
viz3.add_shape(type="rect",
    x0=1.5, y0=0, x1=2.4, y1=2.8,
    line=dict(
        color="orangered",
        width=1,
    ),
    fillcolor="#ff9933",
)

viz3


# In[89]:


#Imports the necessary packages for export 
import chart_studio.plotly as py
import chart_studio.tools


# In[90]:


#The below sends each chart to the website, which then is manually embedded into MMO's website
py.plot(viz, filename = 'Player_Salary', auto_open=False)
py.plot(viz3, filename = 'Team_Bar', auto_open=False)
py.plot(viz4, filename = 'Salary_Group', auto_open=False)

