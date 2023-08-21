# Template

def sliding_window(array, k):
    window_start = 0
    for window_end in range(len(array)):
        # add current element to current_subset

        # if/while condition:  (if for fixed-window, while for dynamic-window)
            # calculate the max/min/contains

            # remove window_start element from current_subset
            # update the window by increasing window_start
            # window_start += 1
        ...


# Given an array, return true if there are two elements within a 
# window of size k that are equal

def close_duplicates(array, k):
    left_ptr = 0
    window = set()

    for right_ptr in range(len(array)):
        if right_ptr - left_ptr + 1 > k:
            window.remove(array[left_ptr])
            left_ptr += 1
        
        if array[right_ptr] in window:
            return True
        
        window.add(array[right_ptr])
    
    return False


arr = [1, 2, 4, 6, 2, 3]
print(close_duplicates(arr, k=1))


# Find the max sum of a subarray of window size k (max sum of subarray with fixed window)
def max_sum(array, k):
    current_sum = 0
    max_sum = float('-inf')
    window_start = 0

    for window_end in range(len(array)):
        current_sum += array[window_end]

        if window_end - window_start == k - 1:
            max_sum = max(max_sum, current_sum)

            current_sum -= array[window_start]
            window_start += 1
    
    return max_sum


arr = [1, -2, 3, -5, 2, -1, 2]
print(max_sum(arr, 3))


# Given  an array of positive integers nums and a positive integer target, return the
# minimal length of a contiguous subarray of which the sum is greater than or equal to target.
# If there is no such subarrray, return O instead.
def minimal_length(nums, target):
    min_len = 0
    current_sum = 0
    window_start = 0

    for window_end in range(len(nums)):

        current_sum += nums[window_end]

        while current_sum >= target:
            min_len = min(min_len, window_end - window_start + 1)
            current_sum -= nums[window_start]
            window_start += 1
    
    return min_len


# Return maximum number in a given sliding window k
def maximum_numbers(nums, k):
    max_numbers = []
    window_start = 0
    current_window_items = []

    for window_end in range(len(nums)):
        current_window_items.append(nums[window_end])

        if len(current_window_items) == k:
            max_numbers.append(max(current_window_items))
            current_window_items.pop(0)
            window_start += 1
        
    return max_numbers


# Return maximum number in a given sliding window k (Optimized solution using monotonic decreasing)
from collections import deque

def max_numbers(nums, k):
    mono_queue = deque()
    left_ptr = 0

    output_max = []

    for right_ptr in range(len(nums)):
        # pop smaller values from q
        while mono_queue and nums[mono_queue[-1]] < nums[right_ptr]:
            mono_queue.pop()
        
        mono_queue.append(right_ptr)

        # remove left val from window
        if left_ptr > mono_queue[0]:
            mono_queue.popleft()
        
        if (right_ptr + 1) >= k:
            output_max.append(nums[mono_queue[0]])
            left_ptr += 1

    return output_max
