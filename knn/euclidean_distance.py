def calculate(point_a, point_b):
    b_minus_a = point_b - point_a
    b_minus_a_square = b_minus_a ** 2
    distance_square = b_minus_a_square.sum()
    distance = distance_square ** 0.5
    return distance
