from typing import List
from point import Point

class Square:
    
    """
    Represents a square with the following properties
    1. Has 4 equal sides
    2. Each side is right angled to each other
    """

    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None:
        self.points = [point1, point2, point3, point4]
    

    def calc_dist_squared(self, first_point: Point, second_point: Point):
        """
        Calculates the difference between 2 points using Pythagoras' Theorem, but we do not square root the sum of the squared distances
        """
        first_x, first_y = first_point.get_x(), first_point.get_y()
        second_x, second_y = second_point.get_x(), second_point.get_y()
        distance = (first_x-second_x)**2 + (first_y-second_y)**2
        return distance

    def check_all_same_points(self) -> bool:
        points = self.get_points()
        for i in range(1, len(points)):
            # compare consecutive elements, if they are differet immediately return false
            first_point = points[i-1]
            second_point = points[i]
            first_coord = first_point.get_coord()
            second_coord = second_point.get_coord()
            if first_coord != second_coord:
                return False
        return True

    def check_valid_square(self) -> bool:
        """
        We calculate all the distances between any 2 points
        We should have a total of 6 distances
        1. 4 distances that are equal to represent the 4 equal sides
        2. 2 distances that are equal to represent the 2 equal diagonals
        Any deviation from the 2 conditions means that it is not a valid square
        """

        # check if all 4 points are the same, in this case return false
        if self.check_all_same_points():
            return False

        dists = []
        points = self.get_points()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                first_point = points[i]
                second_point = points[j]
                distance = self.calc_dist_squared(first_point, second_point)
                dists.append(distance)
        
        dists.sort()
        # check if first 4 distances are equal
        for i in range(1, 4):
            first_dist = dists[i-1]
            second_dist = dists[i]
            if first_dist != second_dist:
                return False
        # check last 2 distances are equal
        return dists[4] == dists[5]


    def get_points(self) -> List[Point]:
        """
        Returns array of points
        """
        return self.points
        



