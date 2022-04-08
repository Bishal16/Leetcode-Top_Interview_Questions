class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln, k = len(nums), k % len(nums)
        nums[:] = nums[ln-k:] + nums[0:ln-k]