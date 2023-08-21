# Time complexity O(n**2), Space complexity O(1)
# Bubble sort - bubbles coming from beneath water to the surface

def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swappped = False  #Variable to check if there was a swap in the iteration
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swappped = True
        
        # If no swap, break out of the loop (meaning elements are already swapped in the current iteration)
        if not swappped:
            break

    return elements


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    res = bubble_sort(elements)
    print(res)
