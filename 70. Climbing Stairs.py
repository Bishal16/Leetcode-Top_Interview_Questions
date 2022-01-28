class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        i = 3
        fib = [1, 1]
        x,y = 0, 0
        while i <= 45:
            fib.append(fib[-1] + fib[-2])
            i+=1
        print(len(fib))
        return fib[n-1] + fib[n-2]         