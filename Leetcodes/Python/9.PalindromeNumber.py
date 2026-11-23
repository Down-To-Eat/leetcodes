class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        n = x
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        if x < 0:
            return False
        elif x == rev:
            return True         
        else:
            return False
x = 101
obj = Solution()
print(obj.isPalindrome(x))