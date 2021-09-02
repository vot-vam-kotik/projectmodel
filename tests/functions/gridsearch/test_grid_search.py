from typing import Type
from src.functions.gridsearch.gridsearch import grid_search


class TestAttributes:
    def test_return_type(self):
        res = grid_search()

        assert type(res) == Type[float]