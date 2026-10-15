class Solution:
    def reverseBits(self, n: int) -> int:
        nb = bin(n)[2:].zfill(32)
        new = nb[::-1]
        num = int(new,2)
        return num
