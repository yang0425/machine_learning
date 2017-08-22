import operator
from knn_algorithm.euclidean_distance import point_data_set_distance


def classify(in_x, data_set, labels, k):
    distance = point_data_set_distance(in_x, data_set)
    sorted_distance_indicies = distance.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_distance_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
