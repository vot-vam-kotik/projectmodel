from typing import Optional
import pandas as pd


def local_downloader(file_names: Optional[list[str]] = None) -> pd.DataFrame:
    """ загрузка датафрейм(ов) по пути к файлу"""
    if file_names is None or not len(file_names):
        return pd.DataFrame()

    return pd.DataFrame()


local_downloader(None)
