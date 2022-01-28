class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            x = i % 3
            y = i % 5
            if x==0 and y ==0:
                res.append('FizzBuzz')
            elif x == 0:
                res.append('Fizz')
            elif y == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res