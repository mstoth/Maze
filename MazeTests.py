import unittest
import turtle
from Maze import Maze

SIZE = 400

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m = Maze()

    def testScreen(self):
        self.assertTrue(type(self.m.s) == turtle._Screen, "No Screen!")

    def testTurtle(self):
        self.assertTrue(type(self.m.turtle) == turtle.Turtle)

    def testBackground(self):
        self.assertTrue(self.m.s.bgcolor() == 'blue')

    def testSize(self):
        self.assertTrue(self.m.s.window_height() == SIZE, f"window height is {self.m.s.window_height()}")
        self.assertTrue(self.m.s.window_width() == SIZE)

    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix) == SIZE / 20)

    def testReset(self):
        self.m.reset()
        self.assertTrue(self.m.turtle.pos() == (-(SIZE / 2 - 20), SIZE / 2 - 20))

    def testCoordinates(self):
        self.m.turtle.goto(-180, 180)
        self.m.turtle.stamp()
        self.m.turtle.goto(-180, 200)
        self.m.turtle.stamp()
        self.m.turtle.goto(200, -180)
        self.m.turtle.stamp()
        self.m.turtle.goto(200, 200)
        self.m.turtle.stamp()
        self.assertTrue((0, 0) == self.m.pos2index((-180, 180)), f"{self.m.pos2index((-180, 180))}")
        self.assertTrue((19, 19) == self.m.pos2index((200, -200)), f"{self.m.pos2index((200, -200))}")

    def testSettingMatrixValues(self):
        self.m.reset()
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(0 == value)
        value = 1
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertEqual(self.m.matrix[0][0], 1)
        self.m.turtle.goto(-160, 180)
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertEqual(self.m.matrix[0][1], 0)
        self.m.turtle.goto(200, -200)
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertTrue(0 == value)
    def testSetMatrixValueAt(self):
        self.m.setMatrixValueAt(self.m.turtle.pos(),1)
        self.assertTrue(self.m.matrix[0][0],1)


if __name__ == "__main__":
    unittest.main()
