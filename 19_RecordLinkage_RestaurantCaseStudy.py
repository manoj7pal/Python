import recordlinkage as rl
from dataset import dataset


# Step0
def load_data():
    restaurants = dataset.load_dataset('restaurant_csv')
    restaurants_dirty = dataset.load_dataset('restaurant_dirty_csv')

    print(restaurants.info())
    print(restaurants_dirty.info())

    # print(restaurants.type.unique())
    # print(restaurants_dirty.type.unique())

    # print(np.sort(restaurants.phone.unique())[:5])
    # print(np.sort(restaurants_dirty.phone.unique())[:5])
    return restaurants, restaurants_dirty


# Step1
def generate_pairs(restaurants, restaurants_dirty):
    # Generate Pairs
    indexer = rl.Index()
    indexer.block(['city'])
    # indexer.block(['city', 'phone'])
    pairs = indexer.index(restaurants, restaurants_dirty)
    # print(pairs)
    return pairs


# Step2
def configure_compare_object():
    compare_cl = rl.Compare()
    compare_cl.exact('city', 'city', label='city')
    compare_cl.string('type', 'type', label='cuisine_type', threshold=0.8)
    compare_cl.string('addr', 'addr', label='address', threshold=0.8)
    compare_cl.string('name', 'name', label='restaurant_name', threshold=0.8)
    return compare_cl


# Step4
def treat_duplicates(pot_matches, restaurants_dirty):
    # Find duplicate rows
    dup_rows = pot_matches[pot_matches.sum(axis=1) >= 3]
    dup_rows_index = dup_rows.index.get_level_values(1)

    # Isolate dup rows from dirty df
    restaurants_new = restaurants_dirty[~ restaurants_dirty.index.isin(dup_rows_index)]

    return dup_rows, restaurants_new


# Step4.1
def verify_duplicates(dup_rows, restaurants, restaurants_dirty):
    # Verify the Duplicate rows/matches - Print Duplicate rows
    print(dup_rows)
    print(restaurants[restaurants.index.isin(dup_rows.index.get_level_values(0))][['name', 'phone']])
    print(restaurants_dirty[restaurants_dirty.index.isin(dup_rows.index.get_level_values(1))][['name', 'phone']])


# Step5
def link_df(restaurants, restaurants_dirty, restaurants_new):
    # Link DF
    full_restaurants = restaurants.append(restaurants_new)
    print(restaurants.shape, restaurants_new.shape)
    print(full_restaurants.shape)


def run():
    # 0. Load Dataset
    restaurants, restaurants_dirty = load_data()

    # 1. Generate Pairs
    pairs = generate_pairs(restaurants, restaurants_dirty)

    # 2. Configure Compare Object
    compare_cl = configure_compare_object()

    # 3. Score and fetch the potential matches - Generate Potential matches
    pot_matches = compare_cl.compute(pairs, restaurants, restaurants_dirty)
    # print(pot_matches[pot_matches.sum(axis=1) >= 3])

    # 4. Treat Duplicates and return unique df
    dup_rows, restaurants_new = treat_duplicates(pot_matches, restaurants_dirty)
    # verify_duplicates(dup_rows, restaurants, restaurants_dirty)

    # 5. Link new Dataframe
    link_df(restaurants, restaurants_dirty, restaurants_new)


run()
