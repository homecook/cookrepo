__author__ = 'kwickram'
'''
Script for importing csv files into the database (great for loading sample data).
Must clear all data first from database.
'''

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import ipdb
import os

ipdb.set_trace()

# DATA_FILE_PATH = '/Users/kri/Dropbox/homecook/db schema/'
# navigates to 'db schema' folder in homecook directory (note at different absolute paths on different machines)
DATA_FILE_PATH = os.path.abspath(os.path.join( os.path.dirname( __file__ ), '..' , '..', '..', '..', 'db schema'))
print()
MEALS_FILENAME = 'meals_sample_data.csv'
USERS_FILENAME = 'users_sample_data.csv'
ORDERS_FILENAME = 'orders_sample_data.csv'

USERS_TBLNAME = 'users_user'
MEALS_TBLNAME = 'meals_meal'
ORDERS_TBLNAME = 'orders_order'

IF_EXISTS = 'append'    # 'append': add the data, 'replace': drop and recreate table, 'fail': skip
WRITE_INDEX = False           #  write the dataframe index to 'index' column in datatable

DB_CONNECTION_STRING = 'postgresql+psycopg2://dkkqsvpjtlsttd:x4c-mLFohV_mKpmcohAwXwc4ze@ec2-54-83-202-64.compute-1.amazonaws.com:5432/d1jei2gq0hpjc7'
db = create_engine(DB_CONNECTION_STRING, connect_args={'sslmode':'require'})

def quick_load_csv(csv_filename, db_tablename):
    ipdb.set_trace()
    '''
    Loads csv file into database table, replacing existing content.
    '''
    try:
        filepath = os.path.join(DATA_FILE_PATH, csv_filename)
        df = pd.read_csv(filepath)
        df.to_sql(db_tablename, db, if_exists=IF_EXISTS, index=WRITE_INDEX)
    except Exception as err:
        print(err)
        err_message = 'import_csv.py - quick_load_csv() : Failed. ' + csv_filename, ' to ' + db_tablename
        print(err_message)
        pass

    return True

# load data
quick_load_csv(USERS_FILENAME, USERS_TBLNAME)
quick_load_csv(MEALS_FILENAME, MEALS_TBLNAME)
quick_load_csv(ORDERS_FILENAME, ORDERS_TBLNAME)

print('import_csv.py : Success.')


