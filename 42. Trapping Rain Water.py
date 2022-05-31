class Solution:
    def trap(self, height: List[int]) -> int:
        #applied divide and conqure method
        def recursion_div_conqr(p,q):
            if q-p <= 1:
                return 0
            else:
                x = max(height[p+1 : q])                                    
                if x > min(height[p],height[q]):
                    piv = height[p+1 : q].index(x) + (p+1)
                    return recursion_div_conqr(p, piv) + recursion_div_conqr(piv, q) 
                else:
                    return min(height[p],height[q])*(q-p-1) - sum(height[p+1: q])         
        return recursion_div_conqr(0,len(height)-1) 
            
        