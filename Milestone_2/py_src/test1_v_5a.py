from typing import List, Tuple
import sys
import csv, random
WIDTH_EXCEEDED = sys.maxsize

    
def program5A(n: int, heights: List[int], widths: List[int], C: List[int], M: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
    
    Parameters:
    n (int): number of paintings
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings
    C (List[List[int]]): max painting height for row p_i, ..., p_j inclusive

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    # Check for invalid input.
    if n < 1:
        return (0, 0, [])

    # Base case.
    elif n == 1:
        return (1, heights[0], [1])
    
    # Create a list of all possible return options over i, for 0 <= i <= n - 1.
    options = []
    c_n = C[n - 1]
    for i in range(n):
        # Get the value of C for the current i and n values.
        c_val = c_n[i]
        
        # Only include values for which the width is valid.
        if c_val == WIDTH_EXCEEDED:
            continue

        # Use the remaining heights and widths.
        tmpHeights = heights[:i]
        tmpWidths = widths[:i]

        # Get the return value from opt array if it exists, and calculate it recursively if not. 
        ret = None
        if M[i] != None:
            ret = M[i]
        else:
            ret = program5A(i, tmpHeights, tmpWidths, C, M)

        # Only add a row if we are not in the n < 1 case.
        rows = (n >= 1) + ret[0]
        
        # Calculate the cost of the now-constructed row.
        cost = c_val + ret[1]
        
        # Create a temporary list to be used in the tuple at the front, and add the length of its row.
        row_lengths = ret[2]
        
        # Bounds check.
        if n >= 1:
            # Insert length of row.
            row_lengths.append(n - i)

            # Add the tuple to the list.
            options.append((rows, cost, row_lengths[:]))

    # Construct final return value.
    result = min(options, key=lambda x: x[1])
    M[n - 1] = result
    return result


def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1
    
    Parameters:
    n (int): number of paintings
    W (int): width of the platform
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    ############################
    # Add you code here
    ############################

    rows = [] # store list of integers, each index is number of items on row

    i = 0               # Painting index
    curr_row_width = 0  # Current row width
    curr_row = []       # Current row contents
    total_height = 0    # Total height

    # Iterate through every painting. 
    while i < n:

        # Check if the row has space for the painting.
        if curr_row_width + widths[i] <= W: 

            # Add the height of painting i to the current row. 
            curr_row.append(heights[i])

            # Add painting i's width to current row width. 
            curr_row_width += widths[i]

            # Proceed to next painting
            i += 1

        # If the painting does not fit, the row is full. Move to the next row. 
        else: 

            # The first painting in every row is the tallest. 
            total_height += curr_row[0]

            # Document the current row length, clear it and reset its width, and continue. 
            rows.append(len(curr_row))
            curr_row.clear()
            curr_row_width = 0
            continue

    # Once all paintings have been checked, add the last row and its height. 
    total_height += curr_row[0]
    rows.append(len(curr_row))

    return len(rows), total_height, rows # replace with your code


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    # Change SIZE_FACTOR to use multiples of SIZE_FACTOR for generating input instances. 
    SIZE_FACTOR = 100
    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 5
    # Change TEST_AVERAGING to get the average time of n tests
    NUM_TEST_AVERAGES = 5

    # Name of output file.
    outFile = "test1v5A.csv"
    
    # Generate the list of sizes, set the default width. 
    sizes = [number * SIZE_FACTOR for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    height_sets = []

    # Generate a list from the specified size down to 1.
    for size in sizes:
        height_sets.append([random.randint(1, SIZE_FACTOR * SIZE_MULTIPLES) for x in range(size, 0, -1)])

    # Open the output file. 
    with open(outFile, mode = 'w', encoding = 'utf-8', newline = '') as out:
        # Create the writer. 
        writer = csv.writer(out, delimiter = ',')

        # Section Labels
        writer.writerow(["Input Size", "Program 1 Optimum Cost Error"])

        # Run a test for every height set. Write this data to the csv. 
        for set_ in height_sets:
            # Get the length of the current height set. 
            n=len(set_)

            print("Testing " + str(n) + " paintings...")

            # Generate a corresponding list of random widths, 1-10.
            widths = [random.randint(1, 10) for _ in range(n)]

            # Create a new list for all C_ij values.
            c = [[] for _ in range(n) ]
            optimum = [None for _ in range(n)]

            '''
            Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
            This list accessed with the n'th painting used as the first index, and the i value used as the second. 
            '''
            for j in range(n, 0, -1):
                for i in range(j):
                    tmpWidths = widths[i:j]
                    ij_width = sum(tmpWidths)
                    
                    # Width check.
                    if ij_width <= W:
                        c[j - 1].append(max(set_[i:j]))
                    else:
                        c[j - 1].append(WIDTH_EXCEEDED)

            # Get the optimized cost of each algorithm's output and calculate program1's error.
            p1 = set_
            p5 = set_       
            h_g = program1(n, W, p1, widths)[1]
            h_o = program5A(n, p5, widths, c, optimum)[1]
            error = (h_g - h_o) / h_o

            # Write the error to the csv as a function of input size. 
            writer.writerow([n, error])

            # Force flush the file.
            out.flush()

    print("Comparison test complete. Check for " + outFile + " in parent directory.")
