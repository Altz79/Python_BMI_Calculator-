#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
              { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
              { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
              { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
              {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
              {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

bmi_table = pd.DataFrame(input_data)

# add 3 needed columns
new_cols = ["BMI", "BMI_Category", "Health_risk"]
values = ['', '', '']
bmi_table = bmi_table.assign(**dict(zip(new_cols, values)))


# In[3]:


# calculate Body Mass Index

bmi_table["BMI"] = (bmi_table['WeightKg'] / ((bmi_table['HeightCm'] / 100) ** 2)).round(2)


# In[4]:


# BMI Category

def bmi_category (row):
    if row["BMI"] <= 18.4:
        return 'Underweight'
    elif row["BMI"] >= 18.5 and row["BMI"] <= 24.9:
        return 'Normal weight'
    elif row["BMI"] >= 25 and row["BMI"] <= 29.9:
        return 'Overweight'
    elif row["BMI"] >= 30 and row["BMI"] <= 34.9:
        return 'Moderately obese'
    elif row["BMI"] >= 35 and row["BMI"] <= 39.9:
        return 'Severely obese'
    elif row["BMI"] >= 40:
        return 'Very severely obese'
    else:
        return 'Not valid input'

bmi_table["BMI_Category"] = bmi_table.apply(lambda row: bmi_category(row), axis=1)


# In[5]:


# Health risk

def health_risk (row):
    if row["BMI"] <= 18.4:
        return 'Malnutrition risk'
    elif row["BMI"] >= 18.5 and row["BMI"] <= 24.9:
        return 'Low risk'
    elif row["BMI"] >= 25 and row["BMI"] <= 29.9:
        return 'Enhanced risk'
    elif row["BMI"] >= 30 and row["BMI"] <= 34.9:
        return 'Medium risk'
    elif row["BMI"] >= 35 and row["BMI"] <= 39.9:
        return 'High risk'
    elif row["BMI"] >= 40:
        return 'Very high risk'
    else:
        return 'Not valid input'

bmi_table["Health_risk"] = bmi_table.apply(lambda row: health_risk(row), axis=1)


# In[6]:


# BMI (Body Mass Index), BMI Category and Health risk as 3 new columns:

bmi_table


# In[7]:


# Count the total number of overweight people

x = bmi_table.BMI_Category.value_counts()['Overweight']
print('Total number of overweight people is: {}'.format(x))

