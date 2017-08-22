from unittest import TestCase
from numpy import array

from knn_algorithm.knn import classify


class TestKNN(TestCase):
    def test_classify(self):
        group = array([[1.0, 1.1],
                       [1.0, 1.0],
                       [0, 0],
                       [0, 0.1]])
        labels = ['A', 'A', 'B', 'B']
        self.assertEqual('B', classify([0, 0], group, labels, 3))
