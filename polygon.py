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
        a = distance(self.vertices[0], self.vertices[1])
        b = distance(self.vertices[1], self.vertices[2])
        c = distance(self.vertices[0], self.vertices[2])
        
        if a + b > c:
            if a + c > b:
                if b + c > a:
                    return True
                
        return False
    
    # Calculate the area of the polygon
    def area(self) -> float:
        """
        Calculate the area of the polygon.
        """
        a = distance(self.vertices[0], self.vertices[1])
        b = distance(self.vertices[1], self.vertices[2])
        c = distance(self.vertices[0], self.vertices[2])
        p = (a + b + c) / 2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
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
        return math.sqrt(math.pow(abs(x2 - x1), 2) + math.pow(abs(y2 - y1), 2))
        

    #Define the method to get all sides of the length of the polygon
    def sides(self) -> list:
        """
        Get all sides of the polygon.
        Returns:
            a list of all sides of the polygon
        """
        side_a = distance(self.vertices[0], self.vertices[1])
        side_b = distance(self.vertices[1], self.vertices[2])
        side_c = distance(self.vertices[0], self.vertices[2])
        
        sides_op = []
        sides_op.append(side_a)
        sides_op.append(side_b)
        sides_op.append(side_c)
        return sides_op
     
     # Define the method to calculate the perimeter of the polygon
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the polygon.
        Returns:
            the perimeter of the polygon
        """
        peri_metr = 0
        peri_metr += distance(self.vertices[0], self.vertices[1])
        peri_metr += distance(self.vertices[1], self.vertices[2])
        peri_metr += distance(self.vertices[0], self.vertices[2])
        
        return peri_metr

    #Define the method to calculate the angle between two sides
    def angles(self) -> list:
        """
        Calculate the angles of the polygon.
        Returns:
            a list of all angles of the polygon
        """
        a = distance(self.vertices[0], self.vertices[1])
        b = distance(self.vertices[1], self.vertices[2])
        c = distance(self.vertices[0], self.vertices[2])
        alpha = math.cos((math.pow(a,2) + math.pow(c,2) - math.pow(b,2))/(2*a*c))
        betta = math.cos((math.pow(a,2) + math.pow(b,2) - math.pow(c,2))/(2*a*b))
        gamma = math.cos((math.pow(b,2) + math.pow(c,2) - math.pow(a,2))/(2*c*b))
        return [alpha, betta, gamma]
        
    #Define the method to calculate the centroid of the polygon
    def centroid(self) -> tuple:
        """
        Calculate the centroid of the polygon.
        Returns:
            a pair of coordinates (x, y)
        """ 
        i = 0
        x = 0
        y = 0
        while i < len(self.vertices):
            x += self.vertices[i][0]
            y += self.vertices[i][1]
            i += 1
        centr_oid = (x/3, y/3)
        return centr_oid
    
vert = Polygon([(4,5), (1.5,2), (7,2)])
print(vert.angles())
    

