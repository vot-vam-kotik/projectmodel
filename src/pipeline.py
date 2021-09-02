from .functions.download.local import local_downloader
from .functions.download.googledisk import googledisk_download
from .functions.preprocessing.preprocessing import preprocessing
from .functions.attributes.attributes import attributes
from .functions.combinations.combinations import combinations
from .functions.gridsearch.gridsearch import grid_search


def pipeline():
    df = local_downloader()
    print("Downloader from local directory was finished")
    df = googledisk_download()
    print("Downloader from googledisk was finished")
    df = preprocessing()
    print("Preprocessing was finished")
    df = attributes()
    print("Adding attributes was finished")
    arr = combinations()
    print("Creation of combinations was finished")
    res = grid_search()
    print("Gridsearch was finished")


if __name__ == '__main__':
    pipeline()
