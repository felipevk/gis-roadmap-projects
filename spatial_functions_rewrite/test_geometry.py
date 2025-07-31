import geometry as Geo
import unittest

class TestGeo(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(Geo.distance(Geo.Point(3,2), Geo.Point(5,6)), 4.47213595499958)
        self.assertEqual(Geo.distance(Geo.Point(2,6), Geo.Point(-2,-2)), 8.94427190999916)

    def test_pointIntersectsAABB(self):
        self.assertFalse(Geo.pointIntersectsAABB(Geo.Point(20,20), Geo.AABB(10, 8, 20, 2)))
        self.assertTrue(Geo.pointIntersectsAABB(Geo.Point(20,20), Geo.AABB(10, 8, 20, 20)))

    def test_aabbIntersectsAABB(self):
        self.assertTrue(Geo.aabbIntersectsAABB(Geo.AABB(20, 20, 5, 12), Geo.AABB(10, 8, 20, 20)))
        self.assertFalse(Geo.aabbIntersectsAABB(Geo.AABB(20, 20, 5, 12), Geo.AABB(28, 8, 12, 20)))

    def test_aabbFromPolygon(self):
        aabb = Geo.aabbFromPolygon(Geo.Polygon([
                Geo.Point(-2,-2),
                Geo.Point(2,6), 
                Geo.Point(5,6),
                Geo.Point(3,2)
            ]))
        self.assertEqual(aabb.x, -2)
        self.assertEqual(aabb.y, -2)
        self.assertEqual(aabb.w, 7)
        self.assertEqual(aabb.h, 8)
    
    def test_rayFromPointIntersectsLine(self):
        self.assertFalse(Geo.rayFromPointIntersectsLine( Geo.Point(1.8, 3), Geo.Line(Geo.Point(-2,-2), Geo.Point(2,6))))

    def test_pointIntersectsPolygon_convex(self):
        convex = Geo.Polygon([
                Geo.Point(-2,-2),
                Geo.Point(2,6), 
                Geo.Point(5,6),
                Geo.Point(3,2)
            ]
        )
        outsidePoint = Geo.Point(3,-2)
        outsideAABBPoint = Geo.Point(8, 4)
        insidePoint = Geo.Point(1.8, 3)
        self.assertFalse(Geo.pointIntersectsPolygon(outsidePoint, convex))
        self.assertFalse(Geo.pointIntersectsAABB(outsideAABBPoint, Geo.aabbFromPolygon(convex)))
        self.assertFalse(Geo.pointIntersectsPolygon(outsideAABBPoint, convex))
        self.assertEqual(Geo.countRaycastHits(insidePoint, convex), 1)
        self.assertTrue(Geo.pointIntersectsPolygon(insidePoint, convex))

    def test_pointIntersectsPolygon_concave(self):
        concave = Geo.Polygon([
                Geo.Point(-6.69,7.21),
                Geo.Point(-3.64,6.43), 
                Geo.Point(-4.49,1.78),
                Geo.Point(-6.08, 5.22),
                Geo.Point(-7.73, 1.74),
                Geo.Point(-10.37, 2.7),
                Geo.Point(-12.42, 3.79),
                Geo.Point(-10.76, 6.19)
            ]
        )
        insidePoint = Geo.Point(-7.42, 3.77)
        outsidePoint = Geo.Point(-5.99, 2.9)
        self.assertEqual(Geo.countRaycastHits(insidePoint, concave), 3)
        self.assertTrue(Geo.pointIntersectsPolygon(insidePoint, concave))
        self.assertEqual(Geo.countRaycastHits(outsidePoint, concave), 2)
        self.assertFalse(Geo.pointIntersectsPolygon(outsidePoint, concave))
        
if __name__ == '__main__':
    unittest.main()