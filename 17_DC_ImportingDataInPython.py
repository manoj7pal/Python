"""
1. PLain files: .txt
2. Flat files: .csv
3.
"""

import numpy as np
import pandas as pd
from dataset import dataset
import matplotlib.pyplot as plt


def np_loadtxt():
    data = np.loadtxt(dataset.get_url('mnist'), delimiter=',')
    # data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])
    # data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

    one_image = data[10, 1:]
    im = one_image.reshape(28, 28)

    plt.imshow(im)
    plt.show()


# np_loadtxt()


# The function np.loadtxt() will freak at this.
# There is another function, np.genfromtxt(),which can handle such structures.
# If we pass dtype=None to it, it will figure out what types each column should be.

def np_genfromtxt():
    data = np.genfromtxt(dataset.get_url('titanic'), delimiter=',', dtype=None, names=True)
    print(data[:10])
    print(data['Fare'][:10])


# np_genfromtxt()

def pd_excel():
    # data = pd.read_excel(dataset.get_url('battledeath_xlsx'), sheet_name=[0,1])
    # print(type(data))

    # Excel specific function
    data = pd.ExcelFile(dataset.get_url('battledeath_xlsx'))
    print(data.sheet_names)

    # Load one sheet - by name or index
    data_2002 = data.parse('2002')
    data_2004 = data.parse(1)

    print(data_2002.head())
    print(data_2004.head())


# pd_excel()
# --------------------------------------------------------------------------------------------------------

""" 
Working with Relational Databases:
    a. sqlalchemy
    b. cx_Oracle
    c. pd.read_sql_query
    
"""
from sqlalchemy import create_engine
import os
import cx_Oracle as ora


# USING SQLALCHEMY

def get_connection(db):
    if db == 'sqlite':
        print('--' * 40)
        print('Sqllite DB  Connection')
        sqlite_engine = create_engine(f"sqlite:///dataset/Chinook.sqlite")
        return sqlite_engine
    elif db == 'oracle':
        print('--' * 40)
        print('Oracle DB Connection')

        # USF Berndt DB
        hostname = 'reade.forest.usf.edu'
        port = 1521
        sid = "cdb9"
        user = 'TEST1'
        pwd = 'testing123'
        dsn = ora.makedsn(hostname, port, sid=sid)
        print(dsn)

        # Install Oracle Driver - basic package : https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
        ora_engine = create_engine(f'oracle://{user}:{pwd}@{dsn}')
        return ora_engine
    else:
        return None


def sqlite_sqlalchemy():
    sqlite_engine = get_connection('sqlite')

    print(f"Engine: {sqlite_engine}, type of engine: {type(sqlite_engine)}")

    print(f"Table List: {sqlite_engine.table_names()}")

    con = sqlite_engine.connect()
    rs = con.execute('SELECT * FROM Album')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df.info())


# sqlite_sqlalchemy()
# --------------------------------------------------------------------------------------------------------
def ora_sqlalchemy():
    ora_engine = get_connection('oracle')

    print(f"Engine: {ora_engine}, type of engine: {type(ora_engine)}")
    print('--' * 40)
    print(ora_engine.table_names())

    # Binding Parameters
    con = ora_engine.connect()
    rs = con.execute('SELECT * FROM movie where movieid = :id and title=:title', id=10, title='GoldenEye (1995)')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)

    # OR

    rs = con.execute('SELECT * FROM movie where movieid = :id and title = :title',
                     {'id': 20, 'title': 'Money Train (1995)'})
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)


ora_sqlalchemy()

# --------------------------------------------------------------------------------------------------------
# USING PANDAS.READ_SQL_QUERY()

def pd_read_sql():
    sqlite_engine = get_connection('sqlite')
    ora_engine = get_connection('oracle')

    sqlite_df = pd.read_sql_query('SELECT * from Album where albumid = :id', sqlite_engine, params={'id': 1})
    print(sqlite_df)

    print('--' * 40)

    ora_df = pd.read_sql_query('SELECT * FROM movie where movieid = :id', ora_engine, params={'id': 10})
    print(ora_df)


# pd_read_sql()
