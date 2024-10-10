# Kadane Algo Approach to solving for the maximum sum of a subarray (max sum of subarray with dynamic window)


def max_sum_subarray(array):
    max_sum = float('-inf')
    current_sum = 0

    for number in array:
        current_sum = max(current_sum, 0)
        current_sum += number

        max_sum = max(max_sum, current_sum)
    
    return max_sum



# Find the left and right index of the max sum subarray of a given array
def find_index_of_max_sum(array):
    max_sum = float('-inf')
    current_sum = 0
    left_ptr = 0
    max_left_ptr, max_right_ptr = 0, 0

    for right_ptr in range(len(array)):
        if current_sum < 0:
            current_sum = 0
            left_ptr = right_ptr
        
        current_sum += array[right_ptr]

        if current_sum > max_sum:
            max_sum = current_sum
            max_left_ptr , max_right_ptr = left_ptr, right_ptr
    
    return [max_left_ptr, max_right_ptr]


# Test
arr = [1, -2, 3, 5, 2, -1, -2]
arr2 = [-1, -3, -2]
print(find_index_of_max_sum(arr2))
print(max_sum_subarray(arr2))
