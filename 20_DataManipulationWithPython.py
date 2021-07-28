from dataset import dataset
import pandas as pd


def load_dataset():
    homelessness = dataset.load_dataset('homelessness_csv')
    print(homelessness.info())
    # print(homelessness.describe())
    return homelessness


def subset_homelessness(homelessness):
    print(homelessness.region.unique())
    print(homelessness.state.unique())

    # Only Mountain Region dataset , and specific columns
    df_mountain = homelessness[homelessness.region == 'Mountain']
    print(df_mountain.region.unique())
    print(homelessness.loc[homelessness.region == 'Mountain', ['region', 'state', 'individuals']])

    # Region : 'Alabama' 'Alaska' 'Arizona'
    print(homelessness[homelessness.state.isin(['Alabama', 'Alaska', 'Arizona'])])


def sort_homelessnes(homelessness):
    # Sort by region
    print(homelessness.sort_values(by='region').head(10))
    print(homelessness.sort_values(by='region', ascending=False).head(10))

    # Sort by Region, Family Members
    print(homelessness.sort_values(by=['region', 'family_members']).head(10))
    print(homelessness.sort_values(by=['region', 'family_members'], ascending=[True, False]).head(10))
    pass


def add_columns(homelessness):
    """ Adding New Columns: MNany names like - transforming, mutating, and feature engineering."""
    homelessness['total_members'] = homelessness.individuals + homelessness.family_members
    homelessness['proportion_individuals'] = homelessness.individuals / homelessness.total_members

    homelessness['ind_per_10k'] = (homelessness.individuals * 10000) / homelessness.state_pop
    homelessness = homelessness.sort_values(by='ind_per_10k', ascending=False)
    print(homelessness[homelessness.ind_per_10k > 20])

    print(homelessness[['state', 'individuals', 'family_members', 'total_members', 'proportion_individuals']].head())

    pass


def run():
    # 0. Load Dataset
    homelessness = load_dataset()

    # 1. Subset Homelessness
    # subset_homelessness(homelessness)

    # 2. Sort Homelessness by Region, Family members and no. of individuals
    # sort_homelessnes(homelessness)

    # 3. Adding New Columns
    add_columns(homelessness)


# run()

# ----------------------------------------------------------------------------------------
# Summary Statistics: Single and Group Statistics
# ----------------------------------------------------------------------------------------
import numpy as np


def load_dataset():
    walmart = dataset.load_dataset('walmart_sales_csv')
    print(walmart.info())
    # print(walmart.describe())
    # print(walmart.head())

    return walmart


def summarize(walmart):
    print(f"Basic Statistics")
    print('--' * 40)

    print(f"Mean Weekly Sale: {round(walmart.weekly_sales.mean(), 2)}")
    print(f"Median Weekly Sale: {round(walmart.weekly_sales.median(), 2)}")
    print(f"Max Weekly Sale: {walmart.weekly_sales.max()}")
    print(f"Min Weekly Sale: {walmart.weekly_sales.min()}")
    print(f"Walmart Sales data ranges from {walmart.date.max()} to {walmart.date.min()}.")
    print(
        f"Average and Median of sales, temperature and fuel rate at once: \n{walmart[['weekly_sales', 'temperature_c', 'fuel_price_usd_per_l']].agg([np.mean, np.median, np.std, np.min, np.max])}")

    print('--' * 40)
    walmart = walmart.sort_values(by='date', ascending=True)
    walmart['cum_weekly_sales'] = walmart.weekly_sales.cumsum()
    walmart['cum_max_sales'] = walmart.weekly_sales.cummax()

    print(walmart.head(10))

    print('--' * 40)


def group_summary(walmart):
    print('--------------------- Group Statistics ---------------------')
    # % of sales occurred at each store type
    print(
        f"Store Type Sales %: \n{round(walmart.groupby(by='type').weekly_sales.sum() / walmart.weekly_sales.sum() * 100, 2)}")

    # % of sales occurred at each store type, holiday impact
    print(f"Holiday impact on weekly sales - Store Type wise:")
    print(round((walmart.groupby(by=['type', 'is_holiday']).weekly_sales.sum() / walmart.weekly_sales.sum() * 100), 2))

    # For each store type, aggregate weekly_sales: get min, max, mean, and median
    print('For each store type, aggregate weekly_sales: get min, max, mean, and median:')
    print(walmart.groupby(by='type').weekly_sales.agg([np.min, np.max, np.mean, np.median]).reset_index())

    # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
    print('For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median:')
    print(walmart.groupby(by='type')['unemployment', 'fuel_price_usd_per_l'].agg([np.min, np.max, np.mean, np.median]))

    print('--' * 40)
    pass


# ----------------------------------------------------------------------------------------
# Pivot Tables
# ----------------------------------------------------------------------------------------

def pivot_table(walmart):
    # Pivot for mean weekly_sales for each store type: Mean by default
    print('Pivot for mean(Mean by default) weekly_sales for each store type: ')
    print(walmart.pivot_table(index='type', values='weekly_sales'))
    print()

    # Pivot for mean and median weekly_sales for each store typ
    print('Pivot for mean and median weekly_sales for each store type:')
    print(walmart.pivot_table(index='type', values='weekly_sales', aggfunc=[np.mean, np.median]))
    print()

    # Pivot for mean weekly_sales by store type and holiday
    print('Pivot for mean weekly_sales by store type and holiday:')
    print(walmart.pivot_table(index='type', columns='is_holiday', values='weekly_sales'))

    # Print mean weekly_sales by department and type; fill missing values with 0
    print('Print mean weekly_sales by department and type; fill missing values with 0:')
    print(walmart.pivot_table(index='type', columns='department', values='weekly_sales', fill_value=0))

    # Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
    print('Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols')
    print(walmart.pivot_table(index='type', columns='department', values='weekly_sales', fill_value=0, margins=True))

    # We can play around around the index and columns argument - to show result in any manner(ie. row or column-wise)
    # fill_value=0 --> for handling NULL values, margins = True --> Row and Column-wise sum
    print(walmart.pivot_table(index='store',
                              columns=['type', 'is_holiday'],
                              values=['weekly_sales', 'temperature_c', 'fuel_price_usd_per_l'],
                              aggfunc=[np.mean, np.median, np.min, np.max], fill_value=0, margins=True))

    print(walmart.pivot_table(index=['type', 'is_holiday'],
                              columns='store',
                              values=['weekly_sales', 'temperature_c', 'fuel_price_usd_per_l'],
                              aggfunc=[np.mean, np.median, np.min, np.max], fill_value=0, margins=True))


def run():
    # 0. Load Dataset
    walmart = load_dataset()

    # Summarize
    # summarize(walmart)

    # Group Statistics
    group_summary(walmart)

    # Pivot Tables - Mean by default
    pivot_table(walmart)


# run()


# ----------------------------------------------------------------------------------------
# Indexes
# ----------------------------------------------------------------------------------------\

def load_dataset():
    temperatures = dataset.load_dataset('temperatures_csv')
    return temperatures


def transform_data(temperatures):
    temperatures = temperatures.replace({'country': {"Côte D'Ivoire": 'Ivory Coast'}})
    temperatures.loc[temperatures.avg_temp_c.isna() == True, ['avg_temp_c']] = temperatures.avg_temp_c.mean()
    temperatures['date'] = pd.to_datetime(temperatures.date)
    return temperatures


def verifying_data(temperatures):
    # Verifying Null Temperatures
    print(temperatures.avg_temp_c.mean())
    null_temp = temperatures.avg_temp_c.isna() == True
    print(temperatures[null_temp])
    print(temperatures.loc[[164], :])

    pass


def summarize_data(temperatures):
    print(temperatures.info())
    # print(temperatures.describe())
    # print(temperatures.head())
    # print(temperatures.isna().sum())

    # verifying_data(temperatures)

    print('--' * 40)


def play_index(temperatures):
    # Index temperatures by city
    print(temperatures.head())

    # temperatures.set_index('city', inplace=True)
    # temperatures = temperatures.set_index('city')
    new_temperatures = temperatures
    temperatures = temperatures.set_index(['country', 'city', 'date'])

    print(
        f"Accesing a single value: \n{temperatures.loc[('Ivory Coast', 'Abidjan', '2000-01-01')]}\n, Type:{type(temperatures.loc[('Ivory Coast', 'Abidjan', '2000-01-01')])}")
    print('**' * 10)
    print(
        f"Accesing a single value: \n{temperatures.loc[[('Ivory Coast', 'Abidjan', '2000-01-01')], 'avg_temp_c']}\n, "
        f"Type:{type(temperatures.loc[[('Ivory Coast', 'Abidjan', '2000-01-01')], 'avg_temp_c'])}")

    # Sort the index of temperatures_ind
    temperatures_srt = temperatures.sort_index()

    # Subset rows from India to Russia
    print(temperatures_srt.loc['India':'Russia'])

    # Try to subset rows from Ahmadabad to Moscow
    print(temperatures_srt.loc['Ahmadabad':'Moscow'])

    # Subset rows from India, Ahmadabad to Russia, Moscow
    print(temperatures_srt.loc[('India', 'Ahmadabad'):('Russia', 'Moscow')])

    # Subset columns from date to avg_temp_c
    print(temperatures_srt.loc[:, 'avg_temp_c'].head())

    # Subset rows from India, Ahmadabad to Russia, Moscow and only the avg_temp_c column
    print(temperatures_srt.loc[('India', 'Ahmadabad'):('Pakistan', 'Lahore'), 'avg_temp_c'].head())


def play_time_index(temperatures):
    # Use Boolean conditions to subset temperatures for rows in 2010 and 2011
    print(temperatures[temperatures.date.isin(['2010', '2011'])].head())

    # set date as index, and sort it
    temperatures = temperatures.set_index('date').sort_index()
    # print(temperatures.tail())

    # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
    print(temperatures.loc['2010':'2011'])

    # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
    print(temperatures.loc['2010-08':'2011-02'])


def play_pivot_index(temperatures):
    # Add a year column to temperatures
    temperatures['year'] = temperatures.date.dt.year

    # Pivot avg_temp_c by country and city vs year
    temp_by_country_city_vs_year = temperatures.pivot_table(index=['country', 'city'], values='avg_temp_c',
                                                            columns='year')

    # Subset for Egypt to India
    print(temp_by_country_city_vs_year.loc['Egypt':'India'])

    # Subset for Egypt, Cairo to India, Delhi,  and 2005 to 2010.
    print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), 2005:2010])

    # Get the worldwide mean temp by year
    mean_temp_by_year = temp_by_country_city_vs_year.mean(axis='rows')
    # print(mean_temp_by_year.head())

    # Filter for the year that had the highest mean temp
    print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

    # Get the mean temp by city
    mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')
    # print(mean_temp_by_city.head())

    # Filter for the city that had the lowest mean temp
    print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

    # Greater than mean temp
    print(mean_temp_by_city[mean_temp_by_city > mean_temp_by_city.min()])


def run():
    # 0: Load dataset
    temperatures = load_dataset()
    # summarize_data(temperatures)

    # 1. Transform Data
    temperatures = transform_data(temperatures)

    # 2. Playing with Index
    # play_index(temperatures)
    # play_time_index(temperatures)
    play_pivot_index(temperatures)

    # X. Summarize Data
    # summarize_data(temperatures)


# run()

# --------------------------------------------------------------
# Pandas - Data Visualization
# --------------------------------------------------------------
def load_dataset():
    avocados = pd.read_pickle(dataset.get_url('avocado_prices_pkl'))
    print(avocados.info())
    return avocados


def pandas_visualization(avocados):
    import matplotlib.pyplot as plt

    # Create Bar Chart: Sales by Avocados size
    # sales_by_size = avocados.groupby(by='size').nb_sold.sum()
    # sales_by_size.plot(kind='bar', title='Avocados - Sales by Size', rot=0)
    # plt.show()

    # Trend Chart: Sales by Date
    # sales_by_date = avocados.groupby(by='date').nb_sold.sum()
    # sales_by_date.plot(kind='line', title='Avocados - Sales Trend Chart', rot=90)
    # plt.show()

    # Scatter plot of nb_sold vs avg_price with title
    # avocados.plot(kind='scatter', x='nb_sold', y='avg_price', title="Number of avocados sold vs. average price")
    # plt.axvline(avocados.nb_sold.mean(), color='r')
    # plt.text(avocados.nb_sold.mean(), avocados.avg_price.max(), s='Average')
    # plt.show()

    # Layering PLots: Conventional Avocados Sale vs Organic Avocados sales histogram layering
    avocados[avocados.type == 'conventional'].avg_price.hist(alpha=0.7, bins=20)
    avocados[avocados.type == 'organic'].avg_price.hist(alpha=0.7, bins=20)
    plt.legend(['conventional', 'organic'])
    plt.show()

    pass


def create_dataframes():
    # List of Dictionaries
    avocados_list = [
        {'date': "2019-11-03", 'small_sold': 10376832, 'large_sold': 7835071},
        {'date': "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348},
    ]
    avocados = pd.DataFrame(avocados_list)
    avocados.date = pd.to_datetime(avocados.date)
    print(avocados.info())

    # Dictionaries of list
    avocados_dict = {
        "date": ["2019-11-17", "2019-12-01"],
        "small_sold": [10859987, 9291631],
        "large_sold": [7674135, 6238096]
    }
    avocados = pd.DataFrame(avocados_dict)
    avocados.date = pd.to_datetime(avocados.date)
    print(avocados.info())

    pass


def write_csv():
    dataset = pd.read_csv('dataset/url.csv', names=['name', 'url'])
    dataset['url'] = dataset.url.str.strip()
    dataset = dataset.sort_values(by='name')

    # dataset.to_csv('dataset/url.csv', index=False)
    print(dataset.head())


def run():
    # 0. Load Dataset
    # avocados = load_dataset()

    # 3. pandas_visualization
    # pandas_visualization(avocados)

    # 4. create_dataframes
    # create_dataframes()

    # 5. write_csv
    write_csv()


run()
