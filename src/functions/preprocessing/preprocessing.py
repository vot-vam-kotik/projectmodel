import pandas as pd

def preprocessing(data: pd.DataFrame = None) -> pd.DataFrame:
    """ Обработка данных: удаление мусорных данных, заполнение пустых """
    if data is None or data.empty:
        return pd.DataFrame()

    return data


preprocessing(None)