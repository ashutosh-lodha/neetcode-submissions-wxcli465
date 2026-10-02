class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money>=prices[0]+prices[1]:
            money-=(prices[0]+prices[1])
        return money