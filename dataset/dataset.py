import pandas as pd
import os

url_file = "C:/MANOJ/Academic/SelfStudy/Python/USF_Python/Sunbeam/dataset/url.csv"


def list_datasets():
    # print(os.getcwd())

    datasets = pd.read_csv(url_file, names=['name', 'url'])
    print('--' * 40)
    print('Avaialbale Datasets:')
    print('--' * 40)
    for dataset in datasets.name.values:
        print(dataset.strip())


def get_url(dataset_name):
    datasets = pd.read_csv(url_file, names=['name', 'url'])
    dataset_url = datasets[datasets.name == dataset_name].url.values[0].strip()
    return dataset_url


def load_dataset(dataset_name):
    df = pd.read_csv(get_url(dataset_name), index_col=0)
    return df


def sort_dataset_file():
    dataset = pd.read_csv('dataset/url.csv', names=['name', 'url'])
    dataset['url'] = dataset.url.str.strip()
    dataset = dataset.sort_values(by='name')

    dataset.to_csv('dataset/url.csv', index=False, header=False)
