#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a list of normally distributed random numbers"""

import numpy.random as rand


def numpy_task02(mean, stdev, number=100):
    """Creates a random assortment of numbers using a normal distribution with\
    a given mean and standard distribution.
    Args: mean = The mean, sd = The Standard Deviation.
    Ex: to get a Standard Normal distribution:
    >>> numpy_task02(0,1)

    This function can be useful for coming up with random number distrubitions
    to replicate or create hypothesis for an experiment on a given sample set.
    """

    randoms = rand.normal(mean, stdev, number)
    return randoms
