class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n_set = set(nums)
        longest = 1
        for i in n_set :            
            cur_max = 1
            if i-1 in n_set :
                continue # its not the starting atleast
            else:
                x = i
                while x+1 in n_set :
                    cur_max += 1
                    x+=1
                if cur_max > longest:
                    longest = cur_max
        return longest
            