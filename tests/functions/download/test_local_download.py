import pandas as pd

from src.functions.download.local import local_downloader
class TestLocalDownload:
    def test_return_type(self):
        df = local_downloader()

        assert type(df) == type(pd.DataFrame)