# PANDAS
import numpy as np
import pandas as pd
from dataset import dataset


# dataset.list_datasets()
# print('--' * 40)


def access_square(brics):
    """
    Square brackets are helpful when accessing columns/attributes OR Rows independently of a dataframe,
    but not both rows and columns simultaneously.

    Rows: Slicing metyhod should be used or else, it raises a KEY Error

    [] --> return SERIES
    [[]] --> returns DATAFRAME
    """

    print('--' * 40)

    print(f"brics['country']:\n {brics['country']}, type of brics['country']: {type(brics['country'])}\n")
    print(f"brics[['country']]:\n {brics[['country']]}, type of brics[['country']]: {type(brics[['country']])}\n")
    print(
        f"brics[['country', 'capital']]:\n {brics[['country', 'capital']]}, type of brics[['country', 'capital']]: {type(brics[['country', 'capital']])}\n")
    print(f"brics[0:2]:\n {brics[0:2]}, type of brics[0:2]: {type(brics[0:2])}\n")

    print('--' * 40)


def access_loc(brics):
    """
     - Label Based Access
     - Slicing Not Possible
     - [] --> Series
     - [[]] --> DatFrame
     - SYNTAX: df.loc[ [<rows>] [<columns>] ]
    """
    print('--' * 40)

    print(f"brics.loc['BR']:\n{brics.loc['BR']}, type of brics.loc['BR']: {type(brics.loc['BR'])}\n")
    print(f"brics.loc[['BR']]:\n{brics.loc[['BR']]}, type of brics.loc[['BR']]: {type(brics.loc[['BR']])}\n")
    print(
        f"brics.loc[['BR', 'IN']]:\n{brics.loc[['BR', 'IN']]}, type of brics.loc[['BR', 'IN']]: {type(brics.loc[['BR', 'IN']])}\n")
    print(
        f"brics.loc[['BR', 'IN'],['country', 'capital']]:\n{brics.loc[['BR', 'IN'], ['country', 'capital']]}\n, type of brics.loc[['BR', 'IN'],['country', 'capital']]: {type(brics.loc[['BR', 'IN'], ['country', 'capital']])}\n")
    print(
        f"brics.loc[:,['country', 'capital']]:\n{brics.loc[:, ['country', 'capital']]}\n, type of brics.loc[:,['country', 'capital']]: {type(brics.loc[:, ['country', 'capital']])}\n")

    print('--' * 40)


def access_iloc(brics):
    """
     - Integre Based Access
     - Slicing Possible
     - [] --> Series
     - [[]] --> DatFrame
     - SYNTAX: df.iloc[ [<rows>] [<columns>] ]
    """
    print('--' * 40)

    print(f"brics.iloc[0]:\n{brics.iloc[0]}, type of brics.iloc[0]: {type(brics.iloc[0])}\n")
    print(f"brics.iloc[[0]]:\n{brics.iloc[[0]]}, type of brics.iloc[[0]]: {type(brics.iloc[[0]])}\n")
    print(f"brics.iloc[[0,1]]:\n{brics.iloc[[0, 1]]}, type of brics.iloc[[0,1]]: {type(brics.iloc[[0, 1]])}\n")
    print(
        f"brics.iloc[[0,1],[0,1,2]]:\n{brics.iloc[[0, 1], [0, 1, 2]]}\n, type of brics.iloc[[0,1],[0,1,2]]: {type(brics.iloc[[0, 1], [0, 1, 2]])}\n")
    print(
        f"brics.iloc[:,[0,1,2]]:\n{brics.iloc[:, [0, 1, 2]]}\n, type of brics.iloc[:,[0,1,2]]: {type(brics.iloc[:, [0, 1, 2]])}\n")

    print('--' * 40)


def run():
    brics = dataset.load_dataset('brics')
    print(brics)

    # access_square(brics)
    # access_loc(brics)
    access_iloc(brics)

    print(f"")


# run()

# Filtering Pandas DataFrame
def run():
    # cars = pd.read_csv(dataset.get_url('cars'), index_col=0)
    cars = dataset.load_dataset('cars')
    # print(cars.head())

    # 1. right hand drive countries
    dr = cars['drives_right'] == True

    print(f"Below are the countries, which follow Right-Hand drive:\n{('--' * 30)}")
    print(cars[dr])
    print('--' * 30)

    # 2. Left Hand Drive and Cars_per_cap below 100
    print('Left Hand Drive and Cars_per_cap below 100:')
    print('--' * 30)
    # dl = cars['drives_right'] == False
    # cpc_lt_100 = cars['cars_per_cap'] < 100
    # result = cars[ np.logical_and(dl, cpc_lt_100) ]
    result = cars[np.logical_and(np.logical_not(cars.drives_right),
                                 cars.cars_per_cap < 100)]  # np.logical_not(cars.drives_right) OR cars.drives_right == False
    print(result)

    print('--' * 30)

    # 3. Car Maniacs : cpc > 500
    print('Car Maniacs: cpc > 500')
    print('--' * 30)
    print(cars[cars.cars_per_cap > 500])
    print('--' * 30)

    # 4. Cars with medium cars_per_cap i.e between 100 and 500
    print('Cars with medium: cpc between 100 and 500')
    print('--' * 30)
    medium = cars[np.logical_and(cars.cars_per_cap >= 100, cars.cars_per_cap <= 500)]
    print(medium)

    print('--' * 30)

    # 4. Only US
    print(cars.loc[['US'], :])  # Best Way
    print('OR')
    print(cars.iloc[[0], :])
    print('OR')
    print(cars[0:1])
    print('--' * 30)

    print(cars.loc[['US', 'IN'], :])


# run()

# Iterating over the Dataframes -


def run():
    # cars = pd.read_csv(dataset.get_url('cars'), index_col=0)
    cars = dataset.load_dataset('cars')

    # for lab, row in cars.iterrows():
    #     print(lab)
    #     print(row)

    # Country: Cars_per_Cap
    for lab, row in cars.iterrows():
        print(f"{lab}: {row['cars_per_cap']}")

    print('--' * 30)

    # Add a new column to see the length of the country characters
    print('Add a new column to see the length of the country characters')
    print('--' * 30)
    for lab, row in cars.iterrows():
        cars.loc[[lab], ['country_chars']] = len(row['country'])
    print(cars)
    print('--' * 30)

    # Code for loop that adds COUNTRY column
    print('More examples of Bad code writing:')
    print('--' * 30)
    for lab, row in cars.iterrows():
        cars.loc[lab, 'COUNTRY'] = cars.loc[lab, 'country'].upper()

    # Print cars
    print(cars)
    print('--' * 30)

    # BETTER WAY TO DO ABOVE OPERATION
    print('BETTER WAY TO DO ABOVE OPERATIONS - without loops')
    print('--' * 30)
    cars['country_CHARS'] = cars['country'].apply(len)
    cars['COUNTRY'] = cars['country'].apply(str.upper)
    print(cars)

    del (cars['country_chars'])
    del (cars['country_CHARS'])
    del (cars['COUNTRY'])
    print(cars)


run()
