import pandas as pd
from sqlalchemy import create_engine, types
import cx_Oracle as ora


def load_file():
    data = pd.ExcelFile('dataset/visualbi_dataset.xlsx')
    print(data.sheet_names)

    revenue_df = data.parse('Revenue')
    revenue_df.columns = ['region_code', 'product_code', 'year', 'month', 'revenue', 'quantity']

    region_df = data.parse('Region Master')
    region_df.columns = ['region_code', 'region_name']

    product_df = data.parse('Product Master')
    product_df.columns = ['product_code', 'product_name', 'unit_price', 'valid_from', 'valid_to']

    return revenue_df, region_df, product_df


def get_connection(db):
    if db == 'oracle':
        # Private DB - encrypting due to confidentiality
        hostname = 'reade.forest.usf.edu'
        port = 1521
        sid = "cdb9"
        user = 'DW788'
        pwd = 'Arati@18'
        dsn = ora.makedsn(hostname, port, sid=sid)
        print(dsn)

        # Install Oracle Driver - basic package : https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
        ora_engine = create_engine(f'oracle://{user}:{pwd}@{dsn}')
        return ora_engine


def create_tables(revenue_df, region_df, product_df, con):
    revenue_df.to_sql('revenue', con=con, if_exists='replace', schema='DW788', index=False)
    region_df.to_sql('region', con=con, if_exists='replace', schema='DW788', index=False,
                     dtype={'region_name': types.NVARCHAR(32)})
    product_df.to_sql('product', con=con, if_exists='replace', index=False,
                      dtype={'product_name': types.NVARCHAR(32)})


def run():
    # 1. load file
    revenue_df, region_df, product_df = load_file()

    # 2. Get Oracle Connection
    ora_engine = get_connection('oracle')
    print(ora_engine)

    # 3. Create each table in Oracle
    create_tables(revenue_df, region_df, product_df, ora_engine.connect())

    # 4. Load each table values in the table


run()
