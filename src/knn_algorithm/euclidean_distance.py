from numpy import tile


def point_distance(point_a, point_b):
    d_value = point_b - point_a
    return calculate_distance(d_value)


def point_data_set_distance(point, data_set):
    data_set_size = data_set.shape[0]
    d_value = tile(point, (data_set_size, 1)) - data_set
    return calculate_distance(d_value, True)


def calculate_distance(d, is_set=False):
    axis = 1 if is_set else 0
    return ((d ** 2).sum(axis=axis)) ** 0.5
