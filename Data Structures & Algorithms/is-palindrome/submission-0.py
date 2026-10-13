class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for sayac in s:
            if sayac.isalnum():
                newStr += sayac.lower()
        return newStr == newStr[::-1]

        