points = [(2, 1, 2), (2, 1, 3), (1, 2, 3), (1, 2, 2), (3, 1, 2), (3, 3, 1), (2, 3, 1), (1, 3, 3), (2, 4, 1)]
order = "xyz"

sorted_points = sorted(points, key=lambda p: (p[order.index('x')], p[order.index('y')], p[order.index('z')]))

print(sorted_points)
