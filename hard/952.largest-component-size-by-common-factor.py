#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#

# @lc code=start
class Solution:
  def largestComponentSize(self, nums: List[int]) -> int:
    N = len(nums)
    primes = [True for x in range(100001)]
    primes[0] = False
    primes[1] = False
    
    cf = {}
    pAdj = {}
    
    for num in nums:
      cf[num] = []
    
    for i in range(2, 100001):
      temp = []

      if primes[i] and i*2 < 100001:
        if i in cf:
          temp.append(i)
          cf[i].append(i)
          
        for j in range(i*2, 100001, i):
          primes[j] = False
          
          if j in cf:
            temp.append(j)
            cf[j].append(i)
            
      if temp:
        pAdj[i] = list(temp)
    
    
    vis = [False for x in range(100001)]
    ans = 0
  
    
    def dfs(currPrime):
      cnt = 0
      if not vis[currPrime]:
        vis[currPrime] = True
        if currPrime in cf:
          cnt += 1
        for num in pAdj[currPrime]:
          if not vis[num]:
            vis[num] = True
            cnt += 1
          for adjPrime in cf[num]:
            if not vis[adjPrime]:
              cnt += dfs(adjPrime)
              vis[adjPrime] = True
      
      return cnt
    
    
    for prime in pAdj:
      ans = max(ans, dfs(prime))
    
    return ans
          
# @lc code=end

