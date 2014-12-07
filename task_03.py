#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using text files in numpy"""

import numpy as np


def numpy_task03(data_file):
    """Uses numpy to open a text file and determine the mean and standard \
    deviation of the raw data"""

    try:
        table = np.loadtxt(data_file)
    except Exception:
        print "Cannot read file"
    else:
        stdev = np.std(table, dtype=np.int64)
        mean = np.mean(table, dtype=np.int64)
    finally:
        retval = (mean, stdev)
    try:
        return retval
    except Exception:
        print "Cannot write file"
