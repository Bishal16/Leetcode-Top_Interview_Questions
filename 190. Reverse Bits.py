class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            if n&1== 1:
                ans = ans + 2**i
            n = n>>1
        return ans
