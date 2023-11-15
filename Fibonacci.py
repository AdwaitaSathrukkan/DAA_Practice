class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        a=fib_term=0
        b=1
        for i in range(2,n+1):
            fib_term=a+b
            a=b
            b=fib_term

        return b
        
sol=Solution()
n=int(input())
print(sol.fib(n))