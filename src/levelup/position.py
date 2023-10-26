from typing import List

class Position:
    XValue: int = 8
    YValue: int = 8
    minimumXValue: int = 0
    maximumXValue: int = 9
    minimumYValue: int = 0
    maximumYValue: int = 9
  

    Xcoordinates:List[int] = range(minimumXValue,maximumXValue+1)
    Ycoordinates:List[int] = range(minimumYValue,maximumYValue+1)
    pass  
