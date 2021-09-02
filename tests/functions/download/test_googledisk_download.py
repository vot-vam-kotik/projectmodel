import pandas as pd

from src.functions.download.googledisk import googledisk_download
class TestGooglediskDownload:
    def test_return_type(self):
        df = googledisk_download()

        assert type(df) == type(pd.DataFrame)