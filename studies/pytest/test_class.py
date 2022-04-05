#!/usr/bin/env python
import pytest

@pytest.mark.parametrize(
    "param_1", "param_2",
    [
        ('a', 'b'),
        ('c', 'd')
    ], indirect=True
)
class TestGroup:
    """A class with common parameters, 'param1' and 'param2' """

    @pytest.fixture
    def fixt(self):
        """ This fixture will only be available within the scope of TestGroup """
        return 123

    def test_one(self, param_1, param_2, fixt):
        print('\ntest_one', param_1, param_2, fixt)

    def test_two(self, param_1, param_2, fixt):
        print('\ntest_two', param_1, param_2)