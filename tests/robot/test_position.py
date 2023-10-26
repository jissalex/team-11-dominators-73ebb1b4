import unittest
from levelup.position import Position

class TestPosition(unittest.TestCase):
    def test_validate_alternate_construtor (self):
        testobj = Position (8,9)



    def test_initialization(self):
        testobj = Position(9,8)
        expected_minimumXValue = (0)
        expected_maximumXValue = (9)
        expected_minimumYValue = (0)
        expected_maximumYValue = (9)       
        self.assertEqual( 
            expected_minimumXValue,
            testobj.minimumXValue
        )
        self.assertEqual( 
            expected_maximumXValue,
            testobj.maximumXValue
        )
        self.assertEqual( 
            expected_minimumYValue,
            testobj.minimumYValue
        )        
        self.assertEqual( 
            expected_maximumYValue,
            testobj.maximumYValue
        )

    def test_validate_Values_Within_Limits (self):
        testobj = Position(9,9)
        expected_minimumXValue = (0)
        expected_maximumXValue = (9)
        expected_minimumYValue = (0)
        expected_maximumYValue = (9)       
        self.assertGreaterEqual(
            testobj.XValue,
            expected_minimumXValue
        )
        self.assertLessEqual(
            testobj.XValue,
            expected_maximumXValue
        )
        self.assertGreaterEqual(
            testobj.YValue,
            expected_minimumYValue
        )
        self.assertLessEqual(
            testobj.YValue,
            expected_maximumYValue
        )        
    def test_validate_Coordinates_in_Range (self):
        testobj = Position(8,9)
        expected_minimumXValue = (0)
        expected_maximumXValue = (9)
        expected_minimumYValue = (0)
        expected_maximumYValue = (9)       
        self.assertIn(
            testobj.XValue,
            testobj.Xcoordinates
        )
        self.assertIn(
            testobj.YValue,
            testobj.Ycoordinates
        )