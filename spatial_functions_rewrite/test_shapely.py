#import geometry as Geo
from shapely import Point, LineString, Polygon, box, distance
import unittest

class TestGeo(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(distance(Point(3,2), Point(5,6)), 4.47213595499958)
        self.assertEqual(distance(Point(2,6), Point(-2,-2)), 8.94427190999916)

    def test_pointIntersectsAABB(self):
        aabb1 = box(10, 8, 30, 10)
        aabb2 = box(10, 8, 30, 28)
        
        self.assertFalse(aabb1.contains(Point(20,20)))
        self.assertTrue(aabb2.contains(Point(20,20)))

    def test_aabbIntersectsAABB(self):
        aabb = box(20, 20, 25, 32)
        self.assertTrue(aabb.intersects(box(10, 8, 30, 28)))
        self.assertFalse(aabb.intersects(box(28, 8, 40, 28)))
    
    def test_rayFromPointIntersectsLine(self):
        origin = Point(1.8, 3)
        direction = (1, 0)
        ray = LineString([origin, Point(origin.x + 1e6 * direction[0],
                                origin.y + 1e6 * direction[1])])
        segment = LineString([(-2,-2), (2,6)])
        self.assertFalse(ray.intersects(segment))

    def test_pointIntersectsPolygon_convex(self):
        convex = Polygon([
                (-2,-2),
                (2,6), 
                (5,6),
                (3,2)
            ]
        )
        outsidePoint = Point(3,-2)
        outsideAABBPoint = Point(8, 4)
        insidePoint = Point(1.8, 3)

        self.assertFalse(convex.contains(outsidePoint))
        self.assertFalse(convex.contains(outsideAABBPoint))
        self.assertTrue(convex.contains(insidePoint))

    def test_pointIntersectsPolygon_concave(self):
        concave = Polygon([
                (-6.69,7.21),
                (-3.64,6.43), 
                (-4.49,1.78),
                (-6.08, 5.22),
                (-7.73, 1.74),
                (-10.37, 2.7),
                (-12.42, 3.79),
                (-10.76, 6.19)
            ]
        )
        insidePoint = Point(-7.42, 3.77)
        outsidePoint = Point(-5.99, 2.9)
        self.assertTrue(concave.contains(insidePoint))
        self.assertFalse(concave.contains(outsidePoint))
        
if __name__ == '__main__':
    unittest.main()