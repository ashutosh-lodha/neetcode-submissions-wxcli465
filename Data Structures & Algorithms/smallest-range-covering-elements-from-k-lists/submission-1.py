class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Step 1: Combine all numbers into one list.
        # Store each number along with the index of the list it came from.
        # This helps us identify which lists are represented in our window.
        items = []
        for i in range(len(nums)):
            for number in nums[i]:
                items.append((number, i))
        items.sort()
        # Step 2: Create a frequency array count[i] tells us how many numbers from the ith list are currently present inside our sliding window.
        count = [0] * len(nums)
        # left represents the starting position of our window.
        left = 0
        # Keeps track of how many different lists are currently represented inside our window.
        covered_lists = 0
        # Initially, consider the range from the smallest number to the largest number as our answer.
        smallest_range = [items[0][0], items[-1][0]]
        # Step 3: Move the right pointer forward to expand the window.
        for right in range(len(items)):
            number, list_index = items[right]
            # Check whether this is the first number from this list entering our current window.
            if count[list_index] == 0:
                covered_lists += 1
            # Increase the frequency of this list in the window.
            count[list_index] += 1

            # Step 4: If every list is represented in the window, we have a valid range. Now try to make it smaller.
            while covered_lists == len(nums):
                # Get the number at the left end of our window and identify which original list it belongs to.
                left_number, left_list = items[left]
                # Calculate the width of the current valid range.
                current_range = number - left_number
                # Calculate the width of the best range found so far.
                best_range = smallest_range[1] - smallest_range[0]
                # Update the answer if:
                # 1. The current range is smaller, OR
                # 2. Both ranges have the same width, but the current range starts with a smaller number.
                if (current_range < best_range or (current_range == best_range and left_number < smallest_range[0])):
                    smallest_range = [left_number, number]
                # Step 5: Remove the leftmost number from our window.
                # Decrease the frequency of the list it belongs to.
                count[left_list] -= 1
                # If its frequency becomes zero, that means this list is no longer represented in the window.
                if count[left_list] == 0:
                    covered_lists -= 1
                left += 1
        return smallest_range
