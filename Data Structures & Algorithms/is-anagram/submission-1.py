class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            count_s = {}
            count_t = {}
            for karakter in s:
                if karakter in count_s:
                    count_s[karakter] += 1
                else:
                    count_s[karakter] = 1

            for karakter in t:
                if karakter in count_t:
                    count_t[karakter] += 1
                else:
                    count_t[karakter] = 1

            return count_s == count_t
        else:
            return False
        