import pandas as pd

from src.functions.preprocessing.preprocessing import preprocessing
class TestPreprocessing:
    def test_return_type(self):
        df = preprocessing()

        assert type(df) == type(pd.DataFrame)