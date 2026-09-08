class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cheftime, total = 0, 0

        for arrival, ordertime in customers:
            # Chef starts when both customer and chef are ready
            cheftime = max(cheftime, arrival)
            cheftime += ordertime
            total += cheftime - arrival

        return total / len(customers)