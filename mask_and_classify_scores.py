# In this assignment you will write one NumPy function that perform several
# steps of analysis on a square array of scores

# Input rules:
# - arr must be a NumPy array(np.ndarray)
# - arr must be 2-dimensional and square (shape n × n)
# -  n must be at least 4

# If any of these rules are not satisfied,the function should return None

import numpy as np

arr = np.array([
    
    [-11,-12,13,14], 
    [21,22,23,24], 
    [31,32,33,34], 
    [41,42,143,144]
    
])

print("")
print("input array:")
print(arr)


def mask_and_classify_scores(arr):
    
    # Verify it is a 2-d array
    if type(arr) != np.ndarray:
        return None 
    
    if arr.ndim != 2:
        return None
    
    # Control number of rows 
    n_rows, n_cols = arr.shape
    if n_rows != n_cols:
        return None
    
    if n_rows < 4:
        return None
    
    n = n_rows
    
    # PartA;cleaning scores
    # Create a modified copy of the input array, called cleaned, where:
    # - all values less than 0 are replaced with 0
    # - all values greater than 100 are replaced with 100
    # cleaned will be the first element of the return value.
    
    cleaned = arr.copy()
    
    for a in range(n):
        for b in range(n):
            x = cleaned[a, b]
            if x < 0:
                cleaned[a, b] = 0
            elif x > 100:
                cleaned[a, b] = 100
            else:
                cleaned[a, b] = x
                
    # Part B; classifying scores
    # Based on cleaned, create another array with the same shape, called levels.
    # Each entry in levels is an integer that encodes the “level” of the score:
    # - 0 for “low” scores       (< 40)
    # - 1 for “medium” scores    (40 ≤ value < 70)
    # - 2 for “high” scores      (value ≥ 70)
    # levels will be the second element of the return value.
    
    levels = cleaned.copy()

    for a in range(n):
        for b in range(n):
            y = levels[a, b]
            if y < 40:
                levels[a, b] = 0
            elif y >= 40 and y < 70:
                levels[a, b] = 1
            elif y >= 70:
                levels[a, b] = 2

    # Part C; counting passing scores per row
    # A passing score is any value ≥ 50 (in the cleaned array).
    # For each row of cleaned, count how many entries are passing scores.
    # Store these counts in a 1-dimensional NumPy array row_pass_counts of length n.
    # ***Use normal Python loops to do this (you do not need sum with an axis)***
    # row_pass_counts will be the third element of the return value.
    
    row_pass_counts = np.zeros(n, dtype = int)

    for c in range (n):
        count = 0
        row = cleaned[c]
        for d in row:
            if d >= 50:
                count += 1
            
        row_pass_counts[c] = count

    return cleaned, levels, row_pass_counts

# Return value

# If the input is valid, the function must return a tuple:
#     (cleaned, levels, row_pass_counts)
# If the input is invalid, the function must return None.

cleaned, levels, row_pass_counts = mask_and_classify_scores(arr)

print("")
print("Task A: cleaned")
print(cleaned)

print("")
print("Task B: levels")
print(levels)

print("")
print("Task C: row_pass_counts")
print(row_pass_counts)
