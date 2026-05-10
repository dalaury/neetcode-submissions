from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_in_lists = []

    for sublist in nested_arr:
        max_element = 0

        # Find max element in current sublist
        for element in sublist:
            max_element = max(max_element, element)

        # Append max element to list of max elements
        max_in_lists.append(max_element)
    
    return max_in_lists


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
