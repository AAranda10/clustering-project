#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import acquire
from scipy import stats


# In[2]:
'''
    This function will locate and count the number of rows that are missing from the dataframe so we can make decisions on how to handle this missing data 
    '''

def missing_rows(df):
    num_rows_missing = df.isnull().sum()
    pct_rows_missing = df.isnull().sum() / (df.isnull().sum() + df.notnull().sum())
    missing_rows = pd.DataFrame({'num_rows_missing':num_rows_missing,'pct_rows_missing':pct_rows_missing})
    return missing_rows

'''
    This function will locate and count the number of columns that are missing from the dataframe so we can make decisions on how to handle this missing data 
    '''

def missing_cols(df):
    num_cols_missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1) / (df.isnull().sum(axis=1) + df.notnull().sum(axis=1))
    num_rows = df.isnull().sum(axis=1).value_counts().sort_index().reset_index(drop=True)
    cols_missing = pd.DataFrame({'num_cols_missing':num_cols_missing, 'pct_cols_missing':pct_cols_missing, 'num_rows': num_rows})
    return cols_missing

'''
    This function will drop all the nulls that exceed a 70 percent threshold because I decided that I wanted the model to be as accurate as possible and null values will make for a weaker model 
    '''

def drop_nulls(df, prop_required_column = .70, prop_required_row = .70):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

'''
    This function will drop all clean, drop, and fill null values in this dataframe that make it easier to model and explore the data provided. This function will also address for the outliers in this dataset that could prove impactful on our models. 
    '''

def prep_zillow_data():
    df = acquire.get_zillow_data()
    df = drop_nulls(df, prop_required_column = .70, prop_required_row = .70)
    df['finishedsquarefeet12'] = df['finishedsquarefeet12'].fillna((df['finishedsquarefeet12'].mean()))
    df['lotsizesquarefeet'] = df['lotsizesquarefeet'].fillna((df['lotsizesquarefeet'].mean()))
    df['regionidcity'] = df['regionidcity'].fillna((df['regionidcity'].mean()))
    df['fullbathcnt'] = df['fullbathcnt'].fillna((df['fullbathcnt'].mean()))
    df['calculatedbathnbr'] = df['calculatedbathnbr'].fillna((df['calculatedbathnbr'].mean()))
    df['yearbuilt'] = df['yearbuilt'].fillna((df['yearbuilt'].mean()))
    df['censustractandblock'] = df['censustractandblock'].fillna((df['censustractandblock'].mean()))
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].fillna((df['calculatedfinishedsquarefeet'].mean()))
    df['structuretaxvaluedollarcnt'] = df['structuretaxvaluedollarcnt'].fillna((df['structuretaxvaluedollarcnt'].mean()))
    df['regionidzip'] = df['regionidzip'].fillna((df['regionidzip'].mean()))
    df = df.dropna()
    df = df.drop(columns = ['pid', 'id'])
    county_dummies = pd.get_dummies(df['fips'])
    df = pd.concat((df, county_dummies), axis = 1)
    df = df.rename(columns = {6059.0 : 'is_orange_county', 6037.0 : 'is_la_county', 6111.0 : 'is_ventura_county'})
    df = df[df.bedroomcnt < 8]
    df = df[df.bedroomcnt > 0]
    df = df[df.bathroomcnt > 0]
    df = df[df.bathroomcnt < 6]
    df.to_csv('prep_zillow.csv')
    return df

print('prep.py functions loaded successfully')
