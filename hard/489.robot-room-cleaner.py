# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        vis = {}
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # U R D L
        
        
        def rec(cx, cy, d):
          if (cx, cy) not in vis:
            vis[(cx, cy)] = 1
            robot.clean()
            for i in range(4):
              mx, my = moves[(d+i) % 4]
              if (cx+mx, cy+my) not in vis:
                if robot.move():
                  rec(cx+mx, cy+my, (d+i)%4)
                  robot.turnRight()
                  robot.turnRight()
                  robot.move()
                  robot.turnRight()
                  robot.turnRight()
              robot.turnRight()
      
      
        rec(0, 0, 0)
      
        