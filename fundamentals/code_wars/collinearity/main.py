def collinearity(x1:int, y1:int, x2:int, y2:int) -> bool:
    """Checks if the vectors are collinear"""
    # Returns true if collinear
    return x1*y2 == x2*y1

