def reverseBits(self, n):
    return int(format(n, 'b').zfill(32)[::-1], 2)