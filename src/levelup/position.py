from typing import List

class Position:
    XValue:int
    YValue:int
    def __init__(self, XValue:int, YValue:int):
        self.XValue =  XValue
        self.YValue = YValue

    minimumXValue: int = 0
    maximumXValue: int = 9
    minimumYValue: int = 0
    maximumYValue: int = 9
    Xcoordinates:List[int] = range(minimumXValue,maximumXValue+1)
    Ycoordinates:List[int] = range(minimumYValue,maximumYValue+1)
    
 
    
    pass  
