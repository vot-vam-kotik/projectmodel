import numpy

from src.functions.combinations.combinations import combinations


class TestAttributes:
    def test_return_type(self):
        arr = combinations()

        assert type(arr) == type(numpy.ndarray)