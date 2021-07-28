from dataset import dataset
# dataset.sort_dataset_file()

# -------------------------------------------------------------------
# Data Joining using MERGE method:
# Remember that .merge() only returns rows where the values match in both tables.
# -------------------------------------------------------------------
import pickle, requests, matplotlib.pyplot as plt


def load_file_from_web(dataset_name):
    r = requests.get(dataset.get_url(dataset_name))
    open('output/taxi_owners.pkl', 'wb').write(r.content)
    file = open('output/taxi_owners.pkl', mode='rb')
    return file


def load_dataset(dataset_name):
    file = load_file_from_web(dataset_name)
    df = pickle.load(file)
    return df


def merge_dataset(taxi_owners, taxi_vehicles):
    taxi_owner_vehicles = taxi_owners.merge(taxi_vehicles, on='vid', suffixes=['_o', '_v'])

    print(taxi_owner_vehicles.head())
    print(taxi_owner_vehicles.fuel_type.value_counts())

    # print(taxi_owner_vehicles.fuel_type.hist())
    # plt.show()

    return taxi_owner_vehicles


def taxi_problem():
    taxi_owners = load_dataset('chicago_taxi_owners_p')
    taxi_vehicles = load_dataset('chicago_taxi_vehicles_p')
    taxi_owner_vehicles = merge_dataset(taxi_owners, taxi_vehicles)


def business_problem():
    bus_licenses = load_dataset('chicago_business_licenses_p')
    bus_owners = load_dataset('chicago_business_owners_p')
    bus_owners_licenses = bus_licenses.merge(bus_owners, on='account')
    print(bus_owners_licenses.sort_values(by='account').head())
    print(
        bus_owners_licenses.groupby('title').agg({'account': 'count'}).sort_values(by='account', ascending=False).head(
            10))


def run():
    # taxi_problem()
    business_problem()


# run()


# -------------------------------------------------------------------
# Merging Multiple Dataframes
# -------------------------------------------------------------------
# Business and the grants

def load_file_from_web(dataset_name):
    response = requests.get(dataset.get_url(dataset_name))
    loc = f'output/{dataset_name}.pkl'
    open(loc, 'wb').write(response.content)
    file = open(loc, mode='rb')
    return file


def load_dataset(dataset_name):
    file = load_file_from_web(dataset_name)
    df = pickle.load(file)
    df.name = dataset_name
    return df


def describe_data(df):
    print('--' * 40)
    print(df.name)
    print('--' * 40)
    print(df.head())
    print('--' * 40)
    return df.info(), df.describe, df.columns


def merge_datasets(bus_owners, bus_licenses, census):
    bus_summary = bus_owners.merge(bus_licenses, on=['account'], suffixes=['_own', '_lic']) \
        .merge(census, on=['ward', 'zip'], suffixes=['_bus', '_cen'])

    return bus_summary


import numpy as np


def run():
    bus_owners = load_dataset('chicago_business_owners_p')
    bus_licenses = load_dataset('chicago_business_licenses_p')
    census = load_dataset('chicago_census_p')

    # describe_data(bus_owners)
    # describe_data(bus_licenses)
    # describe_data(census)

    bus_summary = merge_datasets(bus_owners, bus_licenses, census)
    # print(bus_summary.shape)
    # print(bus_summary.columns)
    # print(bus_summary.head())

    print(bus_summary.loc[
              bus_summary.account == '10002', ['account', 'title', 'address_bus', 'zip', 'pop_2000', 'pop_2010',
                                               'change']])
    print(bus_summary.business.value_counts())


# run()


# -------------------------------------------------------------------------------------------
# Outer Joins
# -------------------------------------------------------------------------------------------
import pandas as pd


def load_dataset(dataset_name):
    ext = dataset_name.split('_')[-1]
    print(f'ext:{ext}')

    df = pd.DataFrame()

    if ext == 'p':
        response = requests.get(dataset.get_url(dataset_name))
        loc = f'output/{dataset_name}.pkl'
        open(loc, 'wb').write(response.content)
        file = open(loc, 'rb')
        df = pickle.load(file)
    elif ext == 'csv':
        df = pd.read_csv(dataset.get_url(dataset_name))

    return df


def summarize_data(df):
    print(df.head())


def merge_df(df1, df2, on, how):
    return df1.merge(df2, on=on, how=how)


def run():
    movies = load_dataset('movies_p')
    summarize_data(movies)

    actors = load_dataset('movie_actors_csv')

    # If column names are not same in both df's
    print(movies.merge(actors, left_on='title', right_on='Title', how='inner').head(10))

    actors.columns = [i.lower() for i in actors.columns]
    summarize_data(actors)

    movie_actors = merge_df(movies, actors, on='title', how='left')
    movie_actors = merge_df(movies, actors, on='title', how='left')
    movie_actors = movie_actors.sort_values(by='actor', ascending=True)
    summarize_data(movie_actors)

    movie_actors_r = merge_df(movies, actors, on='title', how='right')
    summarize_data(movie_actors_r)


run()

# -------------------------------------------------------------------------------------------
