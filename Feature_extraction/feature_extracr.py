import numpy as np
import pandas as pd
df=pd.read_csv('anime.csv')
print("DataFrame loaded from 'anime.csv':\n", df.head())
def extract_episodes(txt):
    check = False
    epi=""
    for i in txt:
        if i==')':
            check = False
            return epi[0:2]
        if check==True:
            epi+=i
        if i=='(':
            check = True
    # If no closing parenthesis is found, return empty string or handle accordingly
    return epi[0:2] if epi else ""

def extraction_time(txt):
    data = ""
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1,i+20):
                data += txt[j]

            return data

df['episodes']=df['Title'].apply(extract_episodes)
df['episodes']=df['episodes'].astype(int)
df['Total Time'] = df['Title'].apply(extraction_time)
from dateutil.relativedelta import relativedelta
from datetime import datetime

def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        r = relativedelta(end_date, start_date)
        return r.years * 12 + r.months + 1  # +1 to include the starting month
    except:
        return None

df['Months'] = df['Total Time'].apply(calculate_total_months)

print("Episodes extracted and added to DataFrame:\n", df[['Title', 'episodes','Total Time','Months']].head())