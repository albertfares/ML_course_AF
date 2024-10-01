# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    poly = np.array([x**d for d in range(degree + 1)]).T
    return poly
