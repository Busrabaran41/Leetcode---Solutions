class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        orijinal = x
        ters = 0
        
        while x > 0:
            son_basamak = x % 10
            ters = (ters * 10) + son_basamak
            x = x // 10
            
        return orijinal == ters
        