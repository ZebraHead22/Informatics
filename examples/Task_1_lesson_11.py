import pandas as pd

df = pd.read_csv('./NISPUF17.csv', sep=',') # Укажите свой путь к файлу NISPUF17.csv
# print(df['EDUC1'].unique())
# print(df['EDUC1'].where(df['EDUC1'] == 1).count())

def proportion_of_education(dataframe):

    len_of_df = len(df)
    less_than_12 = round(float(df['EDUC1'].where(df['EDUC1'] == 1).count() / len_of_df), 2)
    e12 = round(float(df['EDUC1'].where(df['EDUC1'] == 2).count() / len_of_df), 2)
    more_than_12 = round(float(df['EDUC1'].where(df['EDUC1'] == 3).count() / len_of_df), 2)
    college = round(float(df['EDUC1'].where(df['EDUC1'] == 4).count() / len_of_df), 2)

    pror =  {"less than high school":less_than_12,
    "high school":e12,
    "more than high school but not college":more_than_12,
    "college":college}

    print(pror)

proportion_of_education(df)