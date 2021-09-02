from typing import Type

import numpy
import pandas as pd


def combinations(data: pd.DataFrame = None) -> Type[numpy.ndarray]:
    """ Добавление признаков в данные """
    if data is None or data.empty:
        return numpy.ndarray

    return numpy.ndarray


combinations(None)
