class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mmap = {}
        for i in range(len(nums)):
            if nums[i] not in mmap:
                mmap[nums[i]] = [i]
            else:
                mmap[nums[i]].append(i)
                
        out = []
        for num in nums:
            
            if target-num in mmap:
                if target-num == num:
                    if len(mmap[num]) == 2:
                        out.append(mmap[num][0])
                        out.append(mmap[num][1])

                        break
                else:
                    out.append(mmap[num][0])
                    out.append(mmap[target-num][0])
                    break




        return out