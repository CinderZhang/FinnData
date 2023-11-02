# %% importing packages
import pandas as pd
import numpy as np
import sqlite3

from plotnine import *
from mizani.formatters import comma_format, percent_format
from pandas.tseries.offsets import DateOffset
# %% WRDS Connection
import wrds
conn = wrds.Connection()

conn.list_libraries().sort()
type(conn.list_libraries())



# %% CRSP library datasets
crsp_tables = conn.list_tables(library='crsp')

# %% aapl stock data with permno. use """ to break long string.
aapl_stk = conn.raw_sql("""SELECT *
                           FROM crsp.msf WHERE permno = 14593""", 
                           date_cols=['date'])
aapl_stk.head()

# %% stock data with permno: Note: you need to change the permno. 
# CRSP use CUSIP or permno as identifier, NOT ticker.
# tsla_stk = conn.raw_sql("""SELECT permno, date, prc, ret, shrout 
#                            FROM crsp.msf WHERE permno = <your_permno>""", 
#                            date_cols=['date'])
# tsla_stk.head()

# %%
