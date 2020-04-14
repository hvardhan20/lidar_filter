# LIDAR sensor filters

This project provides 2 filters for reducing the noise in a LIDAR sensor scan.
 
### Prerequisites and setup

**Python 2.7 is required to run these filters**.
To use these filters, copy the filters directory into your project and import the filter classes like:
```
from filters.tm_filter import TemporalMedianFilter
from filters.range_filter import RangeFilter
```
See the `main.py` for usage example.


### Initializing

Instantiate the RangeFilter and TemporalMedianFilter objects to create the filters. Pass the LIDAR sensor
scan data to the `update` methods of each filter to clean the noisy updates.

## Running the unittests
For running correctness test, I am using `unittest` from the standard python library
The unit test cases can be run from the project root directory (LIDAR Filter) using

```
python2 -m unittest discover -s ./tests -v
```

#### Author: Sai Harshavardhan Bachina