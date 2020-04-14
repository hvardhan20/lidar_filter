import unittest

from filters.tm_filter import TemporalMedianFilter
from numpy.testing import assert_array_equal


class TestTMFilterUpdate(unittest.TestCase):
    """
    Test for temporal median filter
    """
    def test_temporal_medial_filter_update(self):
        updates = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.]]

        expected = [[0., 1., 2., 1., 3.],
                    [0.5, 3., 4.5, 1., 3.],
                    [1., 3., 4., 1., 3.],
                    [1.5, 3., 3.5, 1., 3.],
                    [2.5, 3., 4., 1., 1.5]]

        tmf = TemporalMedianFilter(d=3)
        for i in range(len(updates)):
            assert_array_equal(expected[i], tmf.update(updates[i]))

    def test_temporal_medial_filter_update2(self):
        """
            Test for temporal median filter with D value 5
        """
        updates = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.]]

        expected = [[0., 1., 2., 1., 3.],
                    [0.5, 3., 4.5, 1., 3.],
                    [1., 3., 4., 1., 3.],
                    [1.5, 3., 3.5, 1., 3.],
                    [2, 3., 4., 1., 3.]]

        tmf = TemporalMedianFilter(d=5)
        for i in range(len(updates)):
            assert_array_equal(expected[i], tmf.update(updates[i]))

    def test_temporal_medial_filter_update_without_np(self):
        """
            Test for temporal median filter without using numpy operations
        """
        updates = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.]]

        expected = [[0., 1., 2., 1., 3.],
                    [0.5, 3., 4.5, 1., 3.],
                    [1., 3., 4., 1., 3.],
                    [1.5, 3., 3.5, 1., 3.],
                    [2.5, 3., 4., 1., 1.5]]

        tmf = TemporalMedianFilter(d=3)
        for i in range(len(updates)):
            assert_array_equal(expected[i], tmf.update(updates[i], use_np=False))

    def test_temporal_medial_filter_update_with_range_filter(self):
        """
            Test for temporal median filter by filtering on range first
        """
        updates = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.]]

        expected = [[0.03, 1., 2., 1., 3.],
                    [0.515, 3., 4.5, 1., 3.],
                    [1., 3., 4., 1., 3.],
                    [1.5, 3., 3.5, 1., 3.],
                    [2.5, 3., 4., 1., 1.515]]

        tmf = TemporalMedianFilter(d=3)
        for i in range(len(updates)):
            assert_array_equal(expected[i], tmf.update(updates[i], filter_range=True))


if __name__ == '__main__':
    unittest.main()
