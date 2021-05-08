#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("Name:")
print("We will be cleaning heart disease data, and conclude which age group has high risk of heart stroke as per diabetes and hight blood pressure level")
print("We will also find which gender has the most not normal platelets count in blood, and plot a pie chart around it")


# # Task 1 - Find the diabetic and hight blood pressure patients across all age groups, and conclude the risk heart stroke is higher in which age group

# In[5]:


#Import libraries
import pandas as pd
import matplotlib.pyplot as plt 


#read the csv
df = pd.read_csv('heart_disease.csv')
df


diabetic_patient = df.loc[df['diabetes'] == 1] 
diabetic_patient

groupby_age_diabetes= diabetic_patient.groupby('age')['diabetes'].count().reset_index() 
groupby_age_diabetes

patient_high_bp= df.loc[df['high_blood_pressure'] == 1]
patient_high_bp

groupby_age_bp= patient_high_bp.groupby('age')['high_blood_pressure'].count().reset_index() 
groupby_age_bp

plt.figure(figsize=(12, 8))
diabetes = groupby_age_diabetes['diabetes']
age =groupby_age_diabetes['age'] 
plt.scatter(age, diabetes, label = "diabetic patients") 
age2=groupby_age_bp['age'] 
bp = groupby_age_bp['high_blood_pressure'] 
plt.scatter(age2, bp, label = "patients with high bp")
plt.xlabel("Age Group", size=14)
plt.ylabel("Diabetic and high blood pressure level", size=14) 
plt.legend()
plt.show()


# In[ ]:





# In[3]:





# In[4]:





# In[5]:





# In[6]:





# Conclusion - 

# # Task 2 - Find as per gender who has not normal platelets level in blood

# In[7]:


#Filter by platelets(condition lesser then 150000 OR greater then 450000) and create new dataframe


# In[8]:


#On this new dataframe perform group operation as per gender and create new dataframe 




# In[9]:


#Plot a pie chart as per the gender to show the percentage of male and female who has not normal platelets


# Conclusion - 

# In[ ]:




