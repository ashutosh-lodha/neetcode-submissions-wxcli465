class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            capacity = (left + right) // 2

            daysNeeded = 1
            currentWeight = 0

            for weight in weights:
                if currentWeight + weight > capacity:
                    daysNeeded += 1
                    currentWeight = 0
                currentWeight += weight

            if daysNeeded <= days:
                right = capacity
            else:
                left = capacity + 1

        return left