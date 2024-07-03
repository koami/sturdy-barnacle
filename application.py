def chebyshev_distance(p1, p2):
    """Calculate Chebyshev distance using a for loop."""
    max_diff = 0
    for x, y in zip(p1, p2):
        diff = abs(x - y)
        if diff > max_diff:
            max_diff = diff
    return max_diff

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
