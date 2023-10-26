import unittest
from levelup.position import Position

class TestPosition(unittest.TestCase):
    def test_initialization(self):
        testobj = Position()
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


