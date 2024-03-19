import sqlite3
import pandas as pd

df_2018 = pd.read_csv('/Users/williamchung/Desktop/sql_project/2018.csv')
df_2019 = pd.read_csv('/Users/williamchung/Desktop/sql_project/2019.csv')
df_2020 = pd.read_csv('/Users/williamchung/Desktop/sql_project/2020.csv')
df_ms = pd.read_csv('/Users/williamchung/Desktop/sql_project/market_segment.csv')
df_mc = pd.read_csv('/Users/williamchung/Desktop/sql_project/meal_cost.csv')

# clean up column names
df_2018.columns = df_2018.columns.str.strip()
df_2019.columns = df_2019.columns.str.strip()
df_2020.columns = df_2020.columns.str.strip()
df_ms.columns = df_ms.columns.str.strip()
df_mc.columns = df_mc.columns.str.strip()

# connect to sqlite database
conn = sqlite3.connect('/Users/williamchung/Desktop/sql_project/hotel.db')

# write dataframe as SQLite tables 
df_2018.to_sql('2018', conn, if_exists='replace')
df_2019.to_sql('2019', conn, if_exists='replace')
df_2020.to_sql('2020', conn, if_exists='replace')
df_ms.to_sql('ms', conn, if_exists='replace')
df_mc.to_sql('mc', conn, if_exists='replace')
