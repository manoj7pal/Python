# DataCamp: Cleaning Data into Python
import pandas as pd
from dataset import dataset
import matplotlib.pyplot as plt
import numpy as np


def datatype_issue():
    ride_sharing = pd.read_csv(dataset.get_url('ridesharing_csv'), index_col=0)
    # print(ride_sharing.info())

    """
    Issues:
        1. duration: should be int
        2. user_type: should be category
    """

    # 1.
    ride_sharing.duration = ride_sharing.duration.str.strip('minutes')
    ride_sharing.duration = ride_sharing.duration.astype('int')

    # 2.
    ride_sharing.user_type = ride_sharing.user_type.astype('category')

    print(ride_sharing.info())

    print(f"Average Ride Sharing Duration: {ride_sharing.duration.mean()} minutes")

    # ride_sharing.plot('user_type','duration', kind='bar')

    ride_sharing.groupby('user_type').mean()['duration'].plot(kind='bar')
    plt.show()

    print(ride_sharing.info())


# datatype_issue()


def treat_duplicates():
    ride_sharing = pd.read_csv(dataset.get_url('ridesharing_csv'), index_col=0)

    print(ride_sharing.info())

    # 1. Identify Complete duplicates
    print(ride_sharing[ride_sharing.duplicated(keep=False)].sort_values(by='bike_id'))

    # Complete Duplicates can be safely dropped - keep last instance
    ride_sharing.drop_duplicates(keep='last', inplace=True)
    print(ride_sharing[ride_sharing.duplicated(keep=False)].sort_values(by='bike_id'))

    # 2. Partial duplicate can also be found - For example ['station_A_id', 'station_B_id']
    dup_station_combinations = ride_sharing.duplicated(subset=['station_A_id', 'station_B_id'], keep=False)
    print(ride_sharing.loc[dup_station_combinations, ['station_A_id', 'station_B_id']].sort_values(
        by=['station_A_id', 'station_B_id']))

    # Similarly, Partial duplicates can be deleted in the same - by using the subset and keep argument

    # Aggregating measure values for duplicate records.
    # Reset Index - necessary as after grouping the first group column becomes the row index
    ride_sharing['duration_num'] = ride_sharing.duration.str.strip('minutes').astype('int')

    print(ride_sharing[dup_station_combinations].groupby(['station_A_id', 'station_B_id'])
          .agg({'duration_num': 'mean'})
          .reset_index()
          )


# treat_duplicates()


def duplicates_example1():
    ride_sharing = pd.read_csv(dataset.get_url('ridesharing_csv'), index_col=0)
    ride_sharing.duration = ride_sharing.duration.str.strip('minutes').astype('int')

    # Example
    # Drop complete duplicates from ride_sharing
    ride_dup = ride_sharing.drop_duplicates()

    # Create statistics dictionary for aggregation function
    statistics = {'duration': 'mean'}

    # Group by ride_id and compute new statistics
    ride_unique = ride_dup.groupby('user_gender').agg(statistics).reset_index()

    # Find duplicated values again
    duplicates = ride_unique.duplicated(subset='user_gender', keep=False)
    duplicated_rides = ride_unique[duplicates == True]

    # Assert duplicates are processed
    assert duplicated_rides.shape[0] == 0


# duplicates_example1()


"""
Text and Categorical Data Problems:
    1. .difference() --> MINUS operator in SQL
    2. .isin() --> IN operator in SQL

- To handle Categorical data efficiently, we should always have a MASTER/LOOKUP table of categorical data.
- This will help to identify and treat the inconsistent values efficiently. 

"""


def transform_restaurant_type(restaurant):
    master_restaurant_types = {
        'American': ['american', 'american ( new )', 'cajun/creole', 'hot dogs', 'steakhouses', 'hamburgers',
                     'californian', 'delis', 'chicken'],
        'Mexican': ['mexican/tex-mex', 'mexican'],
        'Asian': ['vietnamese', 'indonesian', 'chinese', 'japanese', 'russian', 'asian', 'noodle shops',
                  'southern/soul'],
        'Italian': ['italian', 'pizza'],
        'Coffee': ['coffee shops', 'coffeebar'],
        'Continental': ['continental', 'pacific new wave', 'eclectic', 'middle eastern', 'seafood', 'french ( new )'],
        'Others': ['diners', 'health food', 'fast food', 'desserts']
    }

    for key, values in master_restaurant_types.items():
        for value in values:
            restaurant.loc[restaurant.type == value, ['cuisine']] = key

    restaurant.cuisine = restaurant.cuisine.astype('category')
    print(restaurant.cuisine.dtypes == 'category')

    return restaurant


def sanitize_restaurant(restaurant):
    set_cusine = set(restaurant.cuisine)

    # Intentional Mistake: Others --> others
    master_cuisine_types = ['American', 'Mexican', 'Asian', 'Italian', 'Coffee', 'Continental', 'others']

    # Set .difference() --> MINUS operator in SQL
    inconsistent_type = set_cusine.difference(master_cuisine_types)
    # print(inconsistent_type)

    # isin() --> IN operator in SQL
    inconsistent_rows = restaurant[restaurant.cuisine.isin(inconsistent_type)]
    print(inconsistent_rows)

    # Return Consistent Rows
    consistent_rows = restaurant[~ inconsistent_rows]

    return consistent_rows


def cat_problems():
    restaurant = dataset.load_dataset('restaurant_dirty_csv')

    # print(restaurant.info()) # Type should be a categorical variable
    # print(set(restaurant.type))

    restaurant = transform_restaurant_type(restaurant)
    restaurant = sanitize_restaurant(restaurant)


# cat_problems()

def summarize_airlines(airlines):
    print(airlines.columns)
    print(airlines.info())
    print(airlines.head())

    # Unique values
    print('--' * 40)
    print('Airline Dataset: Unique Values')
    print('--' * 40)
    print(f"Day: {airlines.day.unique()}")
    print(f"Safety: {airlines.safety.unique()}")
    print(f"Satisfaction: {airlines.satisfaction.unique()}")
    print(f"Cleanliness: {airlines.cleanliness.unique()}")
    print('--' * 40)


def categorize_duration(airlines):
    wait_time_ranges = [0, 150, 200, 400, np.inf]  # OR airlines.wait_min.quantile([0, 0.25, 0.5, 1])
    wait_time_category = ['Less', 'Average', 'High', 'Very High']

    print(airlines.wait_min.describe())
    airlines['wait_time_category'] = pd.cut(airlines.wait_min, bins=wait_time_ranges, labels=wait_time_category,
                                            ordered=True)
    airlines.wait_time_category = airlines.wait_time_category.astype('category')
    print(airlines.wait_time_category.unique())

    return airlines


def transform_airlines(airlines):
    # Consitent Values - Strip, Remap
    airlines.dest_size = airlines.dest_size.str.lower().str.strip().astype('category')
    airlines.dest_region = airlines.dest_region.str.lower()
    airlines.loc[airlines.dest_region == 'eur', 'dest_region'] = 'europe'

    print(airlines.dest_size.unique())
    print(airlines.dest_region.unique())

    return airlines


def airlines_dataset_cleansing():
    airlines = dataset.load_dataset('airlines_csv')

    # summarize_airlines(airlines)
    airlines = transform_airlines(airlines)
    airlines = categorize_duration(airlines)


# airlines_dataset_cleansing()
# -------------------------------------------------------
def modify_dt(banking):
    print(banking.info())

    banking.birth_date = pd.to_datetime(banking.birth_date)
    banking['account_opened'] = pd.to_datetime(banking.account_opened, infer_datetime_format=True, errors='coerce')
    banking.last_transaction = pd.to_datetime(banking.last_transaction, infer_datetime_format=True, errors='coerce')
    banking.inv_amount = banking.inv_amount.astype('float')

    print(banking.info())
    return banking


def transform_banking_data(banking):
    # Handle DataType
    banking = modify_dt(banking)

    # Convert amount fields from Euro to Dollars
    banking['amt_currency'] = 'euro'
    # print(banking.loc[:, ['account_opened', 'amt_currency', 'acct_amount', 'inv_amount', 'fund_A', 'fund_B', 'fund_C','fund_D']].head())

    banking.loc[:, ['acct_amount', 'inv_amount', 'fund_A', 'fund_B', 'fund_C', 'fund_D']] = banking.loc[
                                                                                            :,
                                                                                            [
                                                                                                'acct_amount',
                                                                                                'inv_amount',
                                                                                                'fund_A',
                                                                                                'fund_B',
                                                                                                'fund_C',
                                                                                                'fund_D']] * 1.1
    banking['amt_currency'] = 'dollars'

    # Uniform Dates

    # 1. Convert account_opened to datetime, and standardize the format -   # Infer datetime format - # Return missing value for error
    # banking['account_opened'] = pd.to_datetime(banking.account_opened, infer_datetime_format=True, errors='coerce')
    # print(banking.info())
    # Extract the Year, Month and Date separately
    # print(banking.account_opened.dt.strftime('%Y').head(3))
    # print(banking.account_opened.dt.strftime('%m').head(3))
    # print(banking.account_opened.dt.strftime('%d').head(3))

    banking.account_opened = banking.account_opened.dt.strftime('%m-%d-%Y').astype('datetime64[ns]')
    # print(banking.info())
    # banking.account_opened = banking.account_opened.dt.strftime('%d-%m-%Y')
    # banking.account_opened = banking.account_opened.dt.strftime('%c')

    # print(banking.loc[:, ['account_opened', 'amt_currency', 'acct_amount', 'inv_amount', 'fund_A', 'fund_B', 'fund_C','fund_D']].head())

    return banking


def crossfield_validations(banking):
    # Inconsistent Amount
    eq_amount = (banking.inv_amount == banking[['fund_A', 'fund_B', 'fund_C', 'fund_D']].sum(axis=1))
    consistent_rows = banking[eq_amount]
    inconsistent_rows = banking[~eq_amount]

    print(f"Consistent Amounts: {consistent_rows.shape[0]}")
    print(f"Inconsistent Amounts: {inconsistent_rows.shape[0]}")

    # Inconsistent Age
    import datetime as dt

    banking.birth_date = pd.to_datetime(banking.birth_date)
    today = dt.date.today()

    # Adding 1 - as Data is pof previous year
    age_manual = today.year - (banking.birth_date.dt.year + 1)
    # print(age_manual, banking.Age)

    age_eq = (age_manual == banking.Age)

    print(f"Consistent Age: {banking[age_eq].shape[0]}")
    print(f"InConsistent Age: {banking[~age_eq].shape[0]}")


def run():
    banking = pd.read_csv(dataset.get_url('banking_dirty_csv'), index_col=0, parse_dates=True)

    banking = transform_banking_data(banking)
    crossfield_validations(banking)

    # print(banking.info())

    # Group by Month - Amount Fields
    # print(banking.groupby(by=banking.account_opened.dt.month)[
    #           'amt_currency', 'acct_amount', 'inv_amount', 'fund_A', 'fund_B', 'fund_C',
    #           'fund_D'].mean().reset_index())


# run()

# --------------------------------------------------------------------------------------------------------
# Completeness
# --------------------------------------------------------------------------------------------------------

def missingno(banking):
    import missingno as msno
    import matplotlib.pyplot as plt

    msno.matrix(banking)
    plt.show()


def run():
    banking = pd.read_csv(dataset.get_url('banking_dirty_csv'), index_col=0, parse_dates=True)
    print(banking.isna().sum())

    # missingno(banking)


# run()


# --------------------------------------------------------------------------------------------------------
""" Comparing Strings - 
        - fuzzywuzzy
        - WRatio: Score from 0 to 100 - 1oo indicates exact similar string, whereas 0 says disimilar strings
        - process.extract: takes a target string to be compared, and an iterable object of strings for comparison, and gives the [String Name, WRatio score, and index on the iterable obj] as output
        
    Record Linkage:
        - recordlinkage package
        - Unlike join, does not require a exact matcvhes between diff pairs of data, instead can find close matches using String Similarity.
"""
# --------------------------------------------------------------------------------------------------------
import fuzzywuzzy


def string_similarity():
    from fuzzywuzzy import fuzz

    str1 = 'Manoj Pal'
    str2 = 'Manoj'
    str3 = ['Mnoj', 'MAnOJ', 'Monoj', 'Monog']

    print(f"Similarity score of str1 and str2: {fuzz.WRatio(str1, str2)}")

    str3 = ['Mnoj', 'MAnOJ', 'Monoj', 'Monog']

    from fuzzywuzzy import process

    print(f"String Similarity Score b/w '{str1}' and all values of str3: {process.extract(str1, str3)}")
    print(f"String Similarity Score b/w '{str2}' and all values of str3: {process.extract(str2, str3)}")


# string_similarity()


def string_similarity():
    restaurants = dataset.load_dataset('restaurant_dirty_csv')
    print(restaurants.info())

    # Import process from fuzzywuzzy
    from fuzzywuzzy import process

    # Store the unique values of cuisine_type in unique_types
    unique_types = restaurants.type.unique()

    # Calculate similarity of 'asian' to all values of unique_types
    print(process.extract('asian', unique_types, limit=len(unique_types)))

    # Calculate similarity of 'american' to all values of unique_types
    print(process.extract('american', unique_types, limit=len(unique_types)))

    # Calculate similarity of 'italian' to all values of unique_types
    print(process.extract('italian', unique_types, limit=len(unique_types)))


# string_similarity()


def run():
    # Import process from fuzzywuzzy
    from fuzzywuzzy import process

    restaurants = dataset.load_dataset('restaurant_dirty_csv')

    categories = ('italian', 'asian', 'american')
    # Iterate through categories
    for cuisine in categories:
        # Create a list of matches, comparing cuisine with the cuisine_type column
        matches = process.extract(cuisine, restaurants['type'], limit=len(restaurants.type))

        # Iterate through the list of matches
        for match in matches:
            # Check whether the similarity score is greater than or equal to 80
            if match[1] >= 80:
                # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
                restaurants.loc[restaurants['type'] == match[0]] = cuisine

    # Inspect the final result
    print(restaurants['type'].unique())


# run()

# ---------------------------------------------------------------
# Record Linkage
# ---------------------------------------------------------------

def run():
    import recordlinkage as rl

    restaurants = dataset.load_dataset('restaurant_csv')
    restaurants_dirty = dataset.load_dataset('restaurant_dirty_csv')

    print(restaurants.info())
    print(restaurants_dirty.info())

    # print(restaurants.type.unique())
    # print(restaurants_dirty.type.unique())

    # print(np.sort(restaurants.phone.unique())[:5])
    # print(np.sort(restaurants_dirty.phone.unique())[:5])

    # Generate Pairs
    indexer = rl.Index()
    indexer.block('city')
    pairs = indexer.index(restaurants, restaurants_dirty)
    # print(pairs)

    # Configure Compare Object
    compare_cl = rl.Compare()
    compare_cl.exact('city', 'city', label='city')
    compare_cl.string('type', 'type', label='cuisine_type', threshold=0.8)
    compare_cl.string('addr', 'addr', label='address', threshold=0.8)
    compare_cl.string('name', 'name', label='restaurant_name', threshold=0.8)

    # Generate Potential matches
    pot_matches = compare_cl.compute(pairs, restaurants, restaurants_dirty)
    # print(pot_matches[pot_matches.sum(axis=1) >= 3])

    # Find duplicate rows
    dup_rows = pot_matches[pot_matches.sum(axis=1) >= 3]
    dup_rows_index = dup_rows.index.get_level_values(1)

    # Isolate dup rows from dirty df
    restaurants_new = restaurants_dirty[~ restaurants_dirty.index.isin(dup_rows_index)]

    # Link DF
    full_restaurants = restaurants.append(restaurants_new)
    print(restaurants.shape, restaurants_new.shape)
    print(full_restaurants.shape)

    # Verify the Duplicate rows/matches - Print Duplicate rows
    print(dup_rows)
    print(restaurants[restaurants.index.isin(dup_rows.index.get_level_values(0))][['name', 'phone']])
    print(restaurants_dirty[restaurants_dirty.index.isin(dup_rows.index.get_level_values(1))][['name', 'phone']])

    # 0 and 40 --> 3102461501 and 3102461501

run()
