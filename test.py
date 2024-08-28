# This is a test file

import pandas as pd
import sqlalchemy as sal

connection_string = ('mssql://<sql server _name>\SQLEXPRESS/<database_name>?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
engine = sal.create_engine(connection_string)
conn=engine.connect()


# reading from a table in sql server and storing in a df
df_sql = pd.read_sql_query('select * from orders', conn)
print(df_sql)

