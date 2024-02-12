import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    aq1 = pd.read_csv('CompanyA_Quarter1.txt', sep = ':').T.reset_index()
    aq1.columns = aq1.iloc[0]
    aq1=aq1.drop(aq1.index[0])
    aq2 = pd.read_csv('CompanyA_Quarter2.txt', sep = ':').T.reset_index()
    aq2.columns = aq2.iloc[0]
    aq2=aq2.drop(aq2.index[0])
    bq1 = pd.read_csv('CompanyB_Quarter1.txt', sep = ':').T.reset_index()
    bq1.columns = bq1.iloc[0]
    bq1=bq1.drop(bq1.index[0])
    bq2 = pd.read_csv('CompanyB_Quarter2.txt', sep = ':').T.reset_index()
    bq2.columns = bq2.iloc[0]
    bq2=bq2.drop(bq2.index[0])


    df = pd.concat([aq1, aq2, bq1, bq2])
    df.columns.name = None

    df['Company'] = df['Company'].str.strip()
    df['Revenue'] = df['Revenue'].replace("[$,]", "", regex=True).astype(int)
    df['Expenses'] = df['Expenses'].replace("[$,]", "", regex=True).astype(int)
    df['Net Income'] = df['Net Income'].replace("[$,]", "", regex=True).astype(int)
    df['EPS'] = df['EPS'].replace("[$]", "", regex=True).astype(float)
    df['Assets'] = df['Assets'].replace("[$,]", "", regex=True).astype(int)
    df['Liabilities'] = df['Liabilities'].replace("[$,]", "", regex=True).astype(int)
    df['Equity'] = df['Equity'].replace("[$,]", "", regex=True).astype(int)

    company = input("Choose the company:\n(1) Company A\n(2) Company B\n ")

    if company == '1':
        df_a = df.loc[df['Company']=='Company A']
        print(df.iloc[1, 2:]-df.iloc[0, 2:])
    elif company == '2':
        df_b = df.loc[df['Company']=='Company B']
        print(df.iloc[1, 2:] - df.iloc[0, 2:])



main()