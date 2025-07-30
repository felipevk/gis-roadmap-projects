import geometry as Geo

print(Geo.Point(20,10))

print(Geo.distance(Geo.Point(3,2), Geo.Point(5,6)))
print(Geo.distance(Geo.Point(2,6), Geo.Point(-2,-2)))

print(Geo.pointIntersectsAABB(Geo.Point(20,20), Geo.AABB(10, 8, 20, 2)))
print(Geo.pointIntersectsAABB(Geo.Point(20,20), Geo.AABB(10, 8, 20, 20)))

print(Geo.aabbIntersectsAABB(Geo.AABB(20,20, 5, 12), Geo.AABB(10, 8, 20, 20)))
print(Geo.aabbIntersectsAABB(Geo.AABB(20,20, 5, 12), Geo.AABB(30, 8, 12, 20)))

print(Geo.aabbFromPolygon(Geo.Polygon([
    Geo.Point(-2,-2),
    Geo.Point(2,6), 
    Geo.Point(5,6),
    Geo.Point(3,2)
])))

print(Geo.pointIntersectsPolygon(
    Geo.Point(3,-2),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))

print(Geo.rayFromPointIntersectsLine(
    Geo.Point(1.8, 3), Geo.Line(Geo.Point(-2,-2), Geo.Point(2,6))
))

print(Geo.pointIntersectsPolygon(
    Geo.Point(8, 4),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))

print(Geo.pointIntersectsPolygon(
    Geo.Point(1.8, 3),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))

print(Geo.pointIntersectsPolygon(
    Geo.Point(-0.76, -0.54),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))

print(Geo.pointIntersectsPolygon(
    Geo.Point(0.4, -0.9),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))

print(Geo.pointIntersectsPolygon(
    Geo.Point(1.9, 5.15),
    Geo.Polygon([
        Geo.Point(-2,-2),
        Geo.Point(2,6), 
        Geo.Point(5,6),
        Geo.Point(3,2)
    ]
)))