class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(start, k, subsetSum):

            if k == 1:
                return True

            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            prev = -1

            for i in range(start, len(nums)):

                if used[i]:
                    continue

                if subsetSum + nums[i] > target:
                    continue

                # Skip duplicate values
                if nums[i] == prev:
                    continue

                used[i] = True

                if backtrack(i + 1, k, subsetSum + nums[i]):
                    return True

                used[i] = False
                prev = nums[i]

                # Important pruning
                if subsetSum == 0:
                    return False

            return False

        return backtrack(0, k, 0)