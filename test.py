class sol:
    def bitwiseAnd(self, left: int, right: int) -> int:
        res=left
        for i in range(left, right + 1):
            res &= i
        print(res)
s=sol()
s.bitwiseAnd(1,2147483647)
        