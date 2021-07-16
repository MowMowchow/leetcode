#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
	def isRobotBounded(self, instructions: str) -> bool:
		x = 0
		y = 0
		direc = 0 # N E S W

		for t in range(4):
			for step in instructions:
				if step == "R":
					direc += 1+4
					direc %= 4
				elif step == "L":
					direc -= 1+4
					direc %= 4
				
				else:
					if direc == 0:
						y += 1
					elif direc == 1:
						x += 1
					elif direc == 2:
						y -= 1
					elif direc == 3:
						x -= 1
			
			if x == 0 and y == 0:
				return True
		return False		


# @lc code=end

