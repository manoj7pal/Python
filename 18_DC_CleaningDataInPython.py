# DataCamp: Cleaning Data into Python
import pandas as pd
from dataset import dataset
import matplotlib.pyplot as plt


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
