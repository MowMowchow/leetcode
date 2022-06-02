function runningSum(nums: number[]): number[] {
  return nums.map((value, index) =>
    index > 0 ? (nums[index] += nums[index - 1]) : nums[index]
  );
}
