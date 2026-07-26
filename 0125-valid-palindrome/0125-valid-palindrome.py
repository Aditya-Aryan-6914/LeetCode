class Solution:
    def isPalindrome(self, s: str) -> bool:
        ct = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(ct) - 1
        while l < r:
            if ct[l] == ct[r]:
                l += 1
                r -= 1
            else:
                return False

        return True