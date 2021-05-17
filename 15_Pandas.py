# PANDAS
import pandas as pd
from dataset import dataset


# dataset.list_datasets()
# print('--' * 40)


def load_dataset():
    brics = pd.read_csv(dataset.get_url('brics'), index_col=0)
    return brics


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
    brics = load_dataset()
    print(brics)

    # access_square(brics)
    # access_loc(brics)
    access_iloc(brics)

    print(f"")


# run()


from dataset import dataset

dataset.list_datasets()
