# Bubble sort, insertion sort, heap (pyramid) sort, quicksort algorithms implementation.
# swap_elements routine is a classical approach to move values to each other places.


def swap_elements(first_element, second_element):
    first_element -= second_element
    second_element += first_element
    first_element = second_element - first_element

    return [first_element, second_element]


def bubble_sort(input_array):
    input_array_length = len(input_array)

    for outer_loop_index in range(input_array_length):
        for inner_loop_index in range(input_array_length - outer_loop_index - 1):
            if input_array[inner_loop_index] > input_array[inner_loop_index + 1]:
                input_array[inner_loop_index:inner_loop_index + 2] = swap_elements(input_array[inner_loop_index],
                                                                                   input_array[inner_loop_index + 1])

    return input_array


def insertion_sort(input_array):
    input_array_length = len(input_array)

    for outer_loop_index in range(1, input_array_length):
        key = input_array[outer_loop_index]
        inner_loop_index = outer_loop_index - 1
        while inner_loop_index >= 0 and input_array[inner_loop_index] > key:
            input_array[inner_loop_index + 1] = input_array[inner_loop_index]
            inner_loop_index -= 1

        input_array[inner_loop_index + 1] = key

    return input_array


def heap_sort(array):
    # function for normalizing heap to non-increasing property
    def max_heapify(array_part, root_index):
        part_size = len(array_part)
        # minus '1' for left and right nodes is necessary because of the start index -- '0'
        left_node = 2 * (root_index + 1) - 1
        right_node = 2 * (root_index + 1) - 1 + 1

        if left_node <= part_size - 1 and array_part[left_node] > array_part[root_index]:
            largest = left_node
        else:
            largest = root_index
        if right_node <= part_size - 1 and array_part[right_node] > array_part[largest]:
            largest = right_node
        if largest != root_index:
            [array_part[root_index], array_part[largest]] = swap_elements(array_part[root_index], array_part[largest])
            array_part = max_heapify(array_part, largest)

        return array_part

    def build_max_heap(max_heap):
        max_heap_size = len(max_heap)

        for elementN in range(int(max_heap_size / 2), -1, -1):
            max_heap = max_heapify(max_heap, elementN)
        return max_heap

    build_max_heap(array)
    heap_size = len(array)
    sorted_array = [0 for i in range(heap_size)]

    for index in range(heap_size - 1, 0, -1):
        sorted_array[index] = array[0]
        [array[index], array[0]] = swap_elements(array[index], array[0])
        array.remove(array[index])
        array = max_heapify(array, 0)
    sorted_array[0] = array[0]

    return sorted_array


# quick sort algorithm
def partition(array, start, end):
    reference = array[end]
    index_center = start - 1
    for j in range(start, end):
        if array[j] <= reference:
            index_center += 1
            array[index_center], array[j] = \
                array[j], array[index_center]

    array[index_center + 1], array[end] = \
        array[end], array[index_center + 1]

    return index_center+1


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q-1)
        quick_sort(array, q+1, r)

    return array


array_tosort = [10, 5, 4, 6, 2, 8, 7, 1, 3, 9]
bubble_sorted_array = bubble_sort(array_tosort)

array_tosort = [10, 5, 6, 4, 2, 8, 7, 1, 3, 9]
insertion_sorted_array = insertion_sort(array_tosort)

array_tosort = [10, 5, 6, 4, 2, 8, 7, 1, 3, 9]
heap_sorted_array = heap_sort(array_tosort)

array_tosort = [10, 5, 6, 9, 2, 8, 7, 1, 3, 4]
quick_sorted_array = quick_sort(array_tosort, 0, len(array_tosort)-1)

print("Bubble sort:    " + str(bubble_sorted_array))
print("Insertion sort: " + str(insertion_sorted_array))
print("Heap sort:      " + str(heap_sorted_array))
print("Quick sort:     " + str(quick_sorted_array))
