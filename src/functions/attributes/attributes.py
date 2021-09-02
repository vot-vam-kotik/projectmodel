import pandas as pd


def attributes(data: pd.DataFrame = None) -> pd.DataFrame:
    """ Добавление признаков в данные """
    if data is None or data.empty:
        return pd.DataFrame()

    return pd.DataFrame()


attributes()