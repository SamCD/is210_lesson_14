#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using text files in numpy"""

import numpy as np

def numpy_task03():
    """Uses numpy to open a text file and determine the mean and standard \
    deviation of the raw data"""

    try:
        table = np.loadtxt('data.txt')
    except:
        print "Cannot read file"
    else:
        try:
            sd = np.std(table, dtype=np.int64)
            mean = np.mean(table, dtype=np.int64)
        except:
            print "Cannot calculate values"
    finally:
        retval = (mean, sd)
    return retval
