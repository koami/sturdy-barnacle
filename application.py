import numpy as np

def chebyshev_distance(p1, p2):
    """Calculate Chebyshev distance using NumPy"""
    p1 = np.array(p1)
    p2 = np.array(p2)
    return np.max(np.abs(p1 - p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
