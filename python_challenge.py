
"""
========== INFORMATION ABOUT INDEXES IN LISTS ==========
Say we have a list...
    some_list = ["apple", "banana", "pear"]

"apple" is at index 0 (first position in some_list)
"banana" is at index 1 (2nd position in some_list)
"pear" is at index 2 (last position in some_list)
"""


"""
========== HOW sort_list(numbers_list) FUNCTION WORKS ==========
1. First, copy and duplicate numbers_list (so we don't change the original numbers_list)
2. Find the smallest number and swap positions with the number at index 0
3. Find the 'next smallest number' and swap positions with the number at index 1
4. Find the 'next smallest number' and swap positions with the number at index 2
5. Find the 'next smallest number' and swap positions with the number at index 3
... etc
"""

def sort_list(numbers_list):
    # Copy and duplicate numbers_list
    new_numbers_list = numbers_list.copy()

    # num_items = number of items/numbers in new_numbers_list
    num_items = len(new_numbers_list)

    # Loop through every position in new_numbers_list
    for i in range(0, num_items):
        # Initially, assume the smallest number is at index i
        min_number_index = i

        # Loop through every position from i to the last index to find index of the 'next smallest number'
        for j in range(i, num_items):
            if new_numbers_list[j] < new_numbers_list[min_number_index]:
                min_number_index = j

        # We have found the 'next smallest number', which we will swap positions with the number at index i
        new_numbers_list[i], new_numbers_list[min_number_index] = new_numbers_list[min_number_index], new_numbers_list[i]

    # Return sorted list! :D
    return new_numbers_list


""" ========== TESTING =========="""


# ========== TEST 1: Try sorting a list of integers (whole numbers) ==========
print("TEST 1: Try sorting a list of integers (whole numbers)")

original_list = [5, 8, 3, 1, 4]
sorted_list = sort_list(original_list)

print("Original list:", original_list)
print("Sorted list:", sorted_list)


# ========== TEST 2: Try sorting a list of floating points (decimal numbers) ==========
print("\nTEST 2: Try sorting a list of floating points (decimal numbers)")

original_list = [5.4, 5.3, 3.1, 3.2, 4.0]
sorted_list = sort_list(original_list)

print("Original list:", original_list)
print("Sorted list:", sorted_list)


# ========== TEST 3: Try sorting a list with one number ==========
print("\nTEST 3: Try sorting a list with one number")

original_list = [100]
sorted_list = sort_list(original_list)

print("Original list:", original_list)
print("Sorted list:", sorted_list)


# ========== TEST 4: Try sorting an empty list ==========
print("\nTEST 4: Try sorting an empty list")

original_list = []
sorted_list = sort_list(original_list)

print("Original list:", original_list)
print("Sorted list:", sorted_list)
