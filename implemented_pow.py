class Solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.pow(x, -n)

        valor = self.pow(x, n // 2)
        if n % 2 == 0:
            return valor * valor
        return valor * valor * x


x = int(input('Number: '))
n = int(input('Pow: '))
print(Solution().pow(x, n))
