"""
Perfix comulative product
- when adding we add the number in the arr and the product of all numbers in arr-product
- if we have to add  then all last the product will be 0 and any time we need k <= the step when 0 the result is 0
- so we reset all and condition if k > len arr product is 0
- when get product last k we divide last arr-product by step k arr-product which product without k
- SIMPLY DEVIDE ALL BY WITHOUT K SO GETTING K PRODUCTS
"""


class ProductOfNumbers(object):

    def __init__(self):
        self.arr = []
        self.prod = [1]

    def add(self, num):
        if num == 0:
            self.arr = []
            self.prod = [1]
        else:
            self.arr.append(num)
            self.prod.append(self.prod[-1] * num)

    def getProduct(self, k):
        if k > len(self.arr):
            return 0
        return self.prod[-1] // self.prod[-k - 1]


obj = ProductOfNumbers()

obj.add(3)
# [3]
obj.add(0)
# [3,0]
obj.add(2)
# [3,0,2]
obj.add(5)
# [3,0,2,5]
obj.add(4)
# [3,0,2,5,4]
obj.getProduct(2)
# return 20. The product of the last 2 numbers is 5 * 4 = 20
obj.getProduct(3)
# return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
obj.getProduct(4)
# return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
obj.add(8)
# [3,0,2,5,4,8]
obj.getProduct(2)
# return 32. The product of the last 2 numbers is 4 * 8 = 32
