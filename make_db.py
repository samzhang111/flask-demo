import pandas as pd
import sqlite3 as db

df = pd.read_csv('busstops.csv')

# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_sql.html
with db.connect('busstops.db') as conn:
    df.to_sql('bus_stops', conn, if_exists='replace')
