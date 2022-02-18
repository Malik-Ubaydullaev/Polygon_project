from dis import dis
import math
from turtle import distance
class Polygon:
    """ 
    A class to represent a polygon.
    Polygon is a finite set of vertices in the plane.
    The vertices are stored in a list, each element of the list is a pair of coordinates (x, y).
    attributes:
        vertices: a list of vertices
    methods:
        area: calculate the area of the polygon
        distance: calculate the distance between two points
        sides: get all sides of the polygon
        angles: get all angles of the polygon        
        perimeter: calculate the perimeter of the polygon
        is_valid: validate the polygon
        centroid: calculate the centroid of the polygon
    """
    # Constructor with vertices
    def __init__(self, vertices: list):
        """
        Constructor with vertices.
        vertices: a list of vertices each element of the list is a pair of coordinates (x, y)
        """
        self.vertices = vertices

    #Define the method to validate the polygon
    def is_valid(self) -> bool:
        """
        Validate the polygon.
        Returns:
            True if the polygon is valid
            False if the polygon is invalid
        """

        vertices = self.vertices
        if len(vertices) < 3:
            return False
        else:
            return True 
        
    # Calculate the area of the polygon
    def area(self) -> float:
        """
        Calculate the area of the polygon.
        """
        vertices = self.vertices
        polygon_sides = self.sides()
        perimeter = self.perimeter()

        P = sum(polygon_sides)
        if len(vertices) < 3:
            return 0
        elif len(vertices) == 3:
            a, b, c = polygon_sides
            # Heron's formula
            s = perimeter / 2
            tirangle_are = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return round(tirangle_are, 2)
        elif len(vertices) == 4:
            a, b, c, d = polygon_sides
            # Heron's formula
            s = perimeter / 2
            quadrilateral_are = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d))
            return round(quadrilateral_are, 2)
        elif len(vertices) == 5:
            a, b, c, d, e = polygon_sides
            # Heron's formula
            s = perimeter / 2
            pentagon_are = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e))
            return round(pentagon_are, 2)
        
    

    # Distance between two points
   
    def distance(self, p1: tuple, p2: tuple) -> float:
        """
        Calculate the distance between two points.
        Args:
            p1: a pair of coordinates (x, y)
            p2: a pair of coordinates (x, y)
        Returns:
            the distance between p1 and p2
        """
        # d = √[(x2 − x1)**2 + (y2 − y1)**2]
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt(((x2 - x1)**2)+((y2-y1)**2))

        
    #Define the method to get all sides of the length of the polygon
    def sides(self) -> list:
        """
        Get all sides of the polygon.
        Returns:
            a list of all sides of the polygon
        """
        vertices = self.vertices
        polygon_sides = [self.distance(vertices[-1], vertices[0])] + [self.distance(vertices[i], vertices[i+1]) for i in range(len(vertices)-1)]
        return polygon_sides
     
     # Define the method to calculate the perimeter of the polygon
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the polygon.
        Returns:
            the perimeter of the polygon
        """

        return (sum(self.sides()))
        

    # Calculate the area of the polygon
    def area(self) -> float:
        """
        Calculate the area of the polygon.
        """
        vertices = self.vertices
        polygon_sides = self.sides()
        perimeter = self.perimeter()

        P = sum(polygon_sides)
        if len(vertices) < 3:
            return 0
        elif len(vertices) == 3:
            a, b, c = polygon_sides
            s = perimeter / 2
            tirangle_are = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return round(tirangle_are, 2)
        elif len(vertices) == 4:
            a, b, c, d = polygon_sides
            
            s = perimeter / 2
            quadrilateral_are = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d))
            return round(quadrilateral_are, 2)
        elif len(vertices) == 5:
            a, b, c, d, e = polygon_sides
            
            s = perimeter / 2
            pentagon_are = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e))
            return round(pentagon_are, 2)

    #Define the method to calculate the angle between two sides
    def angles(self) -> list:
        """
        Calculate the angles of the polygon.
        Returns:
            a list of all angles of the polygon
        """

        polygon_area = self.area()
        polygon_sides = self.sides()
        polygon_angles = set()
        for a in polygon_sides:
            for b in polygon_sides:
                if a != b:
                    alpha = math.degrees(math.asin(2*polygon_area/(a*b)))
                    polygon_angles.add(alpha)
        return list(polygon_angles)
        
    #Define the method to calculate the centroid of the polygon
    def centroid(self) -> tuple:
        """
        Calculate the centroid of the polygon.
        Returns:
            a pair of coordinates (x, y)

        vertices = self.vertices
        polygon_area = self.area()
        polygon_sides = self.sides()
        
        x_sum = 0
        y_sum = 0
        for i in range(len(vertices)):
            x_sum += vertices[i][0] * polygon_sides[i]
            y_sum += vertices[i][1] * polygon_sides[i]

        x_centroid = x_sum / (6 * polygon_area)
        y_centroid = y_sum / (6 * polygon_area)
        return (round(x_centroid, 2), round(y_centroid, 2))
    
vert = Polygon([(1.5, 2), (4.,5), (7,2)])
print(vert.is_valid())


