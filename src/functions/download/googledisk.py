from typing import Optional
import pandas as pd


def googledisk_download(file_urls: Optional[list[str]] = None ) -> pd.DataFrame:
    """ Загрузка датафрейм(ов) по ссылке """
    if file_urls is None or not len(file_urls):
        return pd.DataFrame()

    return pd.DataFrame()


googledisk_download(None)