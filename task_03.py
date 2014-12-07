#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using text files in numpy"""

import numpy as np


def numpy_task03(data_file):
    """Uses numpy to open a text file and determine the mean and standard \
    deviation of the raw data"""

    try:
        table = np.loadtxt(data_file)
    except IOError:
        print "Cannot read file"
    else:
        stdev = np.std(table)
        mean = np.mean(table)
    finally:
        retval = (int(mean), int(stdev))
    try:
        return retval
    except IOError:
        print "Cannot write file"
