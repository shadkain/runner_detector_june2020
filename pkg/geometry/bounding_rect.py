from .all import Point, Rect


def boundingRect(points: list) -> Rect:
    '''Returns min bounding all points in list rect. Returns `None` if no valid points in list.'''
    hasPoint = False

    for i in range(0, len(points)):
        point = points[i]
        if point:
            minX = point.x; minY = point.y
            maxX = minX; maxY = minY
            n = i; hasPoint = True; break

    if not hasPoint:
        return None

    for i in range(n+1, len(points)):
        point = points[i]
        if point:
            minX = min(point.x, minX)
            minY = min(point.y, minY)
            maxX = max(point.x, maxX)
            maxY = max(point.y, maxY)
    
    return Rect(Point(minX, minY), Point(maxX, maxY))
    