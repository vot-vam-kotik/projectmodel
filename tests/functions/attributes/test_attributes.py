import pandas as pd

from src.functions.attributes.attributes import attributes


class TestAttributes:
    def test_return_type(self):
        df = attributes()

        assert type(df) == type(pd.DataFrame)
