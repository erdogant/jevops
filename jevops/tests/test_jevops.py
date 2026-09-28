import unittest
import jevops as jevops
import matplotlib
# Use non-interactive backend for tests
matplotlib.use('Agg')

class Testjevops(unittest.TestCase):

    def test_import_example(self):
        assert 1==1

    def test_plot(self):
        1==1
