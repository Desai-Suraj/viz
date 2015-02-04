""" This is the Bokeh charts testing interface.

"""
#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2014, Continuum Analytics, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENCE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from collections import OrderedDict
import unittest

import numpy as np
from numpy.testing import assert_array_equal
import pandas as pd

from bokeh.charts import DataAdapter

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class TestDataAdapter(unittest.TestCase):
    def setUp(self):
        self.values = OrderedDict()
        self.values['first'] = [2., 5., 3.]
        self.values['second'] = [4., 1., 4.]
        self.values['third'] = [6., 4., 3.]

    def test_list(self):
        values = list(self.values.values())
        da = DataAdapter(values)

        self.assertEqual(da.values(), list(self.values.values()))
        self.assertEqual(da.columns, ['0', '1', '2'])
        self.assertEqual(da.keys(), ['0', '1', '2'])
        self.assertEqual(da.index, ['a', 'b', 'c'])

    def test_array(self):
        values = np.array(list(self.values.values()))
        da = DataAdapter(values)

        assert_array_equal(da.values(), list(self.values.values()))
        self.assertEqual(da.columns, ['0', '1', '2'])
        self.assertEqual(da.keys(), ['0', '1', '2'])
        self.assertEqual(da.index, ['a', 'b', 'c'])

    def test_pandas(self):
        values = pd.DataFrame(self.values)
        da = DataAdapter(values)

        # TODO: THIS SHOULD BE FIXED..
        #self.assertEqual(da.values(), list(self.values.values()))
        self.assertEqual(da.columns, ['first', 'second', 'third'])
        self.assertEqual(da.keys(), ['first', 'second', 'third'])
        # We expect data adapter index to be the same as the underlying pandas
        # object and not the default created by DataAdapter
        self.assertEqual(da.index, [0, 1, 2])

    def test_ordered_dict(self):
        da = DataAdapter(self.values)

        self.assertEqual(da.values(), list(self.values.values()))
        self.assertEqual(da.columns, ['first', 'second', 'third'])
        self.assertEqual(da.keys(), ['first', 'second', 'third'])
        self.assertEqual(da.index, ['a', 'b', 'c'])

