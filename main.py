from filters.tm_filter import TemporalMedianFilter
from filters.range_filter import RangeFilter


def main(ups):
    rf = RangeFilter()
    tmf = TemporalMedianFilter(d=5)
    rfs, tmfs = [], []
    for update in ups:
        rfs.append(rf.update(update))
        tmfs.append(tmf.update(update))
    print 'RFs', rfs
    print 'TMFs', tmfs


if __name__ == '__main__':
    updates = [[0., 1., 2., 1., 3.],
               [1., 5., 7., 1., 3.],
               [2., 3., 4., 1., 0.],
               [3., 3., 3., 1., 3.],
               [10., 2., 4., 0., 0.]]
    main(updates)
