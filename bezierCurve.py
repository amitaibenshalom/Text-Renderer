"""
Filename: bezierCurve.py
Author: Amitai Ben Shalom
Description: Object representing a Bezier curve
Each letter in the alphabet is represented by one (or more) Bezier curve(s). The user can "insert" a letter by pressing the keyboard.
When the user presses a key, the corresponding letter is drawn on the screen.
"""

from consts import *


class BezierCurve(object):
    """
    Class representing a Bezier curve
    """

    def __init__(self, p0, p1, p2, p3, color, width):
        """
        Initialize a Bezier curve object
        :param p0: tuple of x, y coordinates for the first control point
        :param p1: tuple of x, y coordinates for the second control point
        :param p2: tuple of x, y coordinates for the third control point
        :param p3: tuple of x, y coordinates for the fourth control point
        :param color: tuple of RGB values for the curve color
        :param width: int representing the width of the curve
        """
        self.vertices = [p0, p1, p2, p3]
        self.color = color
        self.width = width

    def __add__(self, other):
        """
        Add two Bezier curves
        :param other: BezierCurve object to add
        :return: BezierCurve object representing the sum of the two curves
        """

        # check for valid input
        if isinstance(other, BezierCurve):

            # add the control points of the two curves
            new_p0 = (self.vertices[0][0] + other.vertices[0][0], self.vertices[0][1] + other.vertices[0][1])
            new_p1 = (self.vertices[1][0] + other.vertices[1][0], self.vertices[1][1] + other.vertices[1][1])
            new_p2 = (self.vertices[2][0] + other.vertices[2][0], self.vertices[2][1] + other.vertices[2][1])
            new_p3 = (self.vertices[3][0] + other.vertices[3][0], self.vertices[3][1] + other.vertices[3][1])

            return BezierCurve(new_p0, new_p1, new_p2, new_p3, self.color, self.width)
        
        if isinstance(other, tuple) or isinstance(other, list):

            if len(other) != 2:
                return None
            
            # add the tuple to each control point
            new_p0 = (self.vertices[0][0] + other[0], self.vertices[0][1] + other[1])
            new_p1 = (self.vertices[1][0] + other[0], self.vertices[1][1] + other[1])
            new_p2 = (self.vertices[2][0] + other[0], self.vertices[2][1] + other[1])
            new_p3 = (self.vertices[3][0] + other[0], self.vertices[3][1] + other[1])

            return BezierCurve(new_p0, new_p1, new_p2, new_p3, self.color, self.width)
        
        return None
    
    def __sub__(self, other):
        """
        Subtract two Bezier curves
        :param other: BezierCurve object to subtract
        :return: BezierCurve object representing the difference of the two curves
        """

        # check for valid input
        if isinstance(other, BezierCurve):

            # subtract the control points of the two curves
            new_p0 = (self.vertices[0][0] - other.vertices[0][0], self.vertices[0][1] - other.vertices[0][1])
            new_p1 = (self.vertices[1][0] - other.vertices[1][0], self.vertices[1][1] - other.vertices[1][1])
            new_p2 = (self.vertices[2][0] - other.vertices[2][0], self.vertices[2][1] - other.vertices[2][1])
            new_p3 = (self.vertices[3][0] - other.vertices[3][0], self.vertices[3][1] - other.vertices[3][1])

            return BezierCurve(new_p0, new_p1, new_p2, new_p3, self.color, self.width)
        
        if isinstance(other, tuple):

            if len(other) != 2:
                return None
            
            # subtract the tuple from each control point
            new_p0 = (self.vertices[0][0] - other[0], self.vertices[0][1] - other[1])
            new_p1 = (self.vertices[1][0] - other[0], self.vertices[1][1] - other[1])
            new_p2 = (self.vertices[2][0] - other[0], self.vertices[2][1] - other[1])
            new_p3 = (self.vertices[3][0] - other[0], self.vertices[3][1] - other[1])

            return BezierCurve(new_p0, new_p1, new_p2, new_p3, self.color, self.width)
        
        return None
    
    def __mul__(self, other):
        """
        Multiply by a scalar
        :param other: scalar to multiply by
        :return: BezierCurve object representing the product of the curve and the scalar
        """

        # check for valid input
        if isinstance(other, (int, float)):

            # multiply each control point by the scalar
            new_p0 = (self.vertices[0][0] * other, self.vertices[0][1] * other)
            new_p1 = (self.vertices[1][0] * other, self.vertices[1][1] * other)
            new_p2 = (self.vertices[2][0] * other, self.vertices[2][1] * other)
            new_p3 = (self.vertices[3][0] * other, self.vertices[3][1] * other)

            return BezierCurve(new_p0, new_p1, new_p2, new_p3, self.color, self.width)
        
        return None

    def compute_bezier_points(self, num_points=NUM_POINTS):
        """
        Compute the points on the Bezier curve
        :param num_points: int representing the number of points to compute
        :return: list of tuples representing the points on the curve
        """

        # check for valid number of points and control points
        if num_points < 2 or len(self.vertices) != 4:
            return None

        result = []  # list to store computed points

        b0x = self.vertices[0][0]
        b0y = self.vertices[0][1]
        b1x = self.vertices[1][0]
        b1y = self.vertices[1][1]
        b2x = self.vertices[2][0]
        b2y = self.vertices[2][1]
        b3x = self.vertices[3][0]
        b3y = self.vertices[3][1]

        # compute polynomial coefficients from Bezier points
        ax = (-b0x + 3 * b1x + -3 * b2x + b3x)
        ay = (-b0y + 3 * b1y + -3 * b2y + b3y)

        bx = (3 * b0x + -6 * b1x + 3 * b2x)
        by = (3 * b0y + -6 * b1y + 3 * b2y)

        cx = (-3 * b0x + 3 * b1x)
        cy = (-3 * b0y + 3 * b1y)

        dx = (b0x)
        dy = (b0y)

        # set up the number of steps and step size
        numSteps = num_points - 1  # arbitrary choice
        h = 1.0 / numSteps  # compute our step size

        # Compute forward differences from Bezier points and "h"
        pointX = dx
        pointY = dy

        firstFDX = (ax * (h * h * h) + bx * (h * h) + cx * h)
        firstFDY = (ay * (h * h * h) + by * (h * h) + cy * h)

        secondFDX = (6 * ax * (h * h * h) + 2 * bx * (h * h))
        secondFDY = (6 * ay * (h * h * h) + 2 * by * (h * h))

        thirdFDX = (6 * ax * (h * h * h))
        thirdFDY = (6 * ay * (h * h * h))

        # Compute points at each step
        result.append((int(pointX), int(pointY)))

        for i in range(numSteps):
            pointX += firstFDX
            pointY += firstFDY

            firstFDX += secondFDX
            firstFDY += secondFDY

            secondFDX += thirdFDX
            secondFDY += thirdFDY

            result.append((int(pointX), int(pointY)))

        return result

    def draw(self, surface, show_control_lines):
        """
        Draw the Bezier curve
        :param surface: pygame.Surface object to draw the curve on
        """

        if surface is None:
            return  # no surface to draw on
        
        if show_control_lines:
            # draw control "lines"
            pygame.draw.lines(surface, CONTROL_LINE_COLOR, False,
                              [(x[0], x[1]) for x in self.vertices], CONTROL_LINE_WIDTH)
            
        # draw bezier curve
        b_points = self.compute_bezier_points()
        pygame.draw.lines(surface, self.color, False, b_points, self.width)