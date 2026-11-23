class Solution(object):
    def reverse(self, x):
        if x >= 0:
            rev = 0
            n = x
            while n > 0:
                digit = n % 10
                rev = rev * 10 + digit
                n //= 10   
        else:
            n = abs(x)
            sum = 0
            while n > 0:
                digit = n % 10
                sum = sum * 10 + digit
                n //= 10
            rev = -(sum)
        if rev < -2147483648 or rev > 2147483647:
            return 0
        else:
            return rev
x = -123
obj = Solution()
print(obj.reverse(x))