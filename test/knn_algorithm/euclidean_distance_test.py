from unittest import TestCase
from numpy import array

from knn_algorithm.euclidean_distance import point_distance
from knn_algorithm.euclidean_distance import point_data_set_distance


class TestEuclideanDistance(TestCase):
    def test_point_distance(self):
        point_x = array([0, 0])
        point_y = array([2, 2])
        self.assertEqual(8 ** 0.5, point_distance(point_x, point_y))

    def test_point_data_set_distance(self):
        point = array([0, 0])
        data_set = array([[1, 1], [2, 2], [3, 3]])
        self.assertListEqual([2 ** 0.5, 8 ** 0.5, 18 ** 0.5], point_data_set_distance(point, data_set).tolist())
