import unittest

from filters.range_filter import RangeFilter
from numpy.testing import assert_array_equal


class TestRangeFilterUpdate(unittest.TestCase):

    def test_range_filter_update(self):
        """
            Test for range filter
        """
        updates = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.]]

        expected = [[0.03, 1., 2., 1., 3.],
                    [1., 5., 7., 1., 3.],
                    [2., 3., 4., 1., 0.03],
                    [3., 3., 3., 1., 3.],
                    [10., 2., 4., 0.03, 0.03]]

        rf = RangeFilter(dist_range=(0.03, 50))
        for i in range(len(updates)):
            assert_array_equal(expected[i], rf.update(updates[i]))


if __name__ == '__main__':
    unittest.main()
