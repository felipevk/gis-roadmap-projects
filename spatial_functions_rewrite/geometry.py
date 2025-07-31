from dataclasses import dataclass, field
import math
import copy

# shortcut for classes that only hold data and an optional post init method
@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Ray:
    origin: Point
    direction: Point

@dataclass
class Line:
    origin: Point
    end: Point

@dataclass
class AABB:
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0

    def __post_init__(self):
        if self.w < 0 or self.h < 0 : 
            raise ValueError(f"Invalid dimenstions provided: {self.w}, {self.h}")
    
@dataclass
class Polygon:
    # list() called fresh per instance
    # if an empty list is called, the data would be shared between instances
    # if you don't remember why, read about mutable type initialization
    edges: list = field(default_factory=list)  

def distance(a, b):
    return math.sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))

def pointIntersectsAABB(p, box):
    return (
        p.x >= box.x and 
        p.x <= box.x + box.w and 
        p.y >= box.y and 
        p.y <= box.y + box.h
    )

def aabbIntersectsAABB(a, b):
    return (
        ( a.x <= b.x + b.w and
        a.x + a.w >= b.x and
        a.y <= b.y + b.h and
        a.y + a.h >= b.y ) or
        ( b.x <= a.x + a.w and
        b.x + b.w >= a.x and
        b.y <= a.y + a.h and
        b.y + b.h >= a.y )
    )

def aabbFromPolygon(polygon):
    aabb = AABB(float('inf'), float('inf'), 0.0, 0.0)
    maxX, maxY = 0,0

    for edge in polygon.edges:
        aabb.x = edge.x if edge.x < aabb.x else aabb.x
        aabb.y = edge.y if edge.y < aabb.y else aabb.y
        maxX = edge.x if edge.x > maxX else maxX
        maxY = edge.y if edge.y > maxY else maxY
    
    aabb.w = maxX - aabb.x
    aabb.h = maxY - aabb.y
    return aabb

def rayFromPointIntersectsLine(point, line):
    r = Point(line.end.x - line.origin.x, line.end.y - line.origin.y)
    s = Point(1, 0)
    rxs = r.x*s.y - r.y*s.x
    if rxs == 0:
        return False  # lines are parallel (no intersection)
    
    cma = Point(point.x - line.origin.x, point.y - line.origin.y)

    # Scalars where each line segment meets
    # If we multiply each line segment by this scalar, we find the intersection point
    # If it's between 0 and 1, they meet inside the line segment
    # If it's bigger than 1, they meet beyond the line segment
    # If it's smaller than 0, it goes before the line segment
    t = (cma.x*s.y - cma.y*s.x) / rxs
    u = (cma.x*r.y - cma.y*r.x) / rxs

    # no need to check if u > 1 since it's an infinite ray to the right
    return t >= 0 and t <= 1 and u >= 0

def countRaycastHits(point, polygon):
    hits = 0
    # zip creates pairs between 2 groups,
    # in this case, grabs an element from the original list and pairs
    # with the original list, from element 1 to the last, adding element 0
    # This creates pairs where the last one is (last, first)
    for vert1, vert2 in zip(polygon.edges, polygon.edges[1:] + polygon.edges[:1]):
        edgeMin, edgeMax = sorted([vert1, vert2], key=lambda p: p.x)
        hits = hits + 1 if rayFromPointIntersectsLine(point, Line(edgeMin, edgeMax)) else hits

    return hits

def pointIntersectsPolygon(point, polygon):
    if len(polygon.edges) < 3:
        return False

    # aabb collision filter
    aabb = aabbFromPolygon(polygon)
    if not pointIntersectsAABB(point, aabb):
        return False

    return countRaycastHits(point, polygon) % 2 != 0