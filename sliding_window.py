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
# -----------------------------------------------------------


# -----------------------------------------------------------

# Given an array, return true if there are two elements within a 
# window of size k that are equal

# Answer 1: Optimized
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

# Answer 2
def close_duplicates(array, k):
    window_start = 0
    sub_array = []

    for window_end in range(len(array)):
        sub_array.append(array[window_end])

        if (window_end - window_start) == (k - 1):
            for i in range(len(sub_array) - 1):
                if sub_array[i] in sub_array[i+1:]:
                    return True
            
            sub_array.pop(0)
            window_start += 1
    
    return False

arr = [1, 2, 4, 6, 2, 3]
print(close_duplicates(arr, k=1))
# ------------------------------------------------------



# ------------------------------------------------------

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

# -------------------------------------------------------



# ------------------------------------------------------

# Given  an array of positive integers nums and a positive integer target, return the
# minimal length of a contiguous subarray of which the sum is greater than or equal to target.
# If there is no such subarrray, return O instead.
def minimal_length(nums, target):
    min_len = float('inf')
    current_sum = 0
    window_start = 0

    for window_end in range(len(nums)):
        current_sum += nums[window_end]

        while current_sum >= target:
            min_len = min(min_len, window_end - window_start + 1)
            current_sum -= nums[window_start]
            window_start += 1

    return 0 if min_len == float('inf') else min_len


arr = [1, 2, 4, 6, 7, 3, 4]
print(minimal_length(arr, 7))


# Same Question as above put return the minimal length and the subarray 
# which makes up the minimal length, if no match return 0, []
def minimal_length_with_subarray(nums, target):
    min_len = float('inf')
    current_sum = 0
    window_start = 0
    min_subarray = []

    for window_end in range(len(nums)):
        current_sum += nums[window_end]

        while current_sum >= target:
            # min_len = min(min_len, window_end - window_start + 1)
            window_diff = window_end - window_start + 1
            if window_diff < min_len:
                min_len = window_diff
                min_subarray = nums[window_start:window_end + 1]

            current_sum -= nums[window_start]
            window_start += 1

    if min_len == float('inf'):
        return 0, []
    else:
        return min_len, min_subarray

# ----------------------------------------------------



# ---------------------------------------------------

# Return maximum number in a given sliding window k
# Answer 1
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


# Answer 2: Optimized solution using monotonic decreasing
from collections import deque

def maximum_numbers(nums, k):
    mono_queue = deque() #You can use a deque or a list(as stack)
    window_start = 0
    max_outputs = []

    for window_end in range(len(nums)):
        while mono_queue and (mono_queue[-1] < nums[window_end]):
            mono_queue.pop()
        
        mono_queue.append(nums[window_end])

        if (window_end - window_start) == (k - 1):
            max_outputs.append(mono_queue[0])
            window_start += 1

    return max_outputs


arr = [1, 2, 4, 6, 2, 3]
print(maximum_numbers(arr, k=1))
# -------------------------------------------------------

