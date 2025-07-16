from typing import Tuple

class Point:
    
    """
    Represents a point where it has x and y coordinates
    """
    def __init__(self, x_coord: int, y_coord: int):
        self.x = x_coord
        self.y = y_coord
    
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_coord(self) -> Tuple[int, int]:
        return (self.x, self.y)
