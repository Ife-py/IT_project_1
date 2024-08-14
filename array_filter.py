def remove_negatives(arr):
    return [num for num in arr if num >= 0]

# Example usage:
input_array = [4, -3, 2, -7, 0, 5, -1]
output_array = remove_negatives(input_array)
print(output_array)  # Output: [4, 2, 0, 5]
