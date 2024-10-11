from typing import List, Tuple
import csv, random, time

    
def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2
    
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
    rows = []                 # num of items on each row
    i = 0                     # index
    cur_row_width = 0         # current row's width
    curr_row = []             # heights in the current row
    total_height = 0          # total height (cost)
    prev_height = heights[0]  # previous painting's height, initialized to height of first painting
    minimum_found = False

    # Iterate through every painting. 
    while i < n:
        
        # Check if the row has space for the painting. 
        if cur_row_width + widths[i] <= W:

            # Proceed if the local minimum has not been found. 
            if not minimum_found:                    
                
                # Proceed if the current painting's height is <= the previous, or if it is equal to the height of the next
                if (heights[i] <= prev_height) or (heights[i] == heights[i + 1]):

                    # Add 1 to the row counter, increase by the width of the current painting, 
                    # and set the previous height to the current painting's height. 
                    curr_row.append(heights[i])
                    cur_row_width += widths[i]
                    prev_height = heights[i]

                # Instead, if there is a next painting and the next painting is taller, mark minimum_found as true
                # and handle the painting. 
                elif (i < n - 1 and heights[i] <  heights [i + 1]):
                    minimum_found = True

                    # Add 1 to the row counter, increase by the width of the current painting, 
                    # and set the previous height to the current painting's height. 
                    curr_row.append(heights[i])
                    cur_row_width += widths[i]
                    prev_height = heights[i]
            
            # Behavior changes if minimum is found, current height must be greater than previous or equal 
            # to next if next exists.
            else:
                if heights[i] >= prev_height or (i < n - 1 and heights[i] == heights[i + 1]):
                    curr_row.append(heights[i])
                    cur_row_width += widths[i]
                    prev_height = heights[i]

            # Next painting.
            i += 1

        # If the current painting will not fit, handle the row. 
        else:
            # if minimum is not found, the element at the beginning is the tallest, otherwise it is at the end. 
            total_height += curr_row[0] if not minimum_found else curr_row[-1]

            # Append the length of the current row to rows, clear the current row, and reset its width.
            rows.append(len(curr_row))
            curr_row.clear()
            cur_row_width = 0

    # Upon completion, add the remaining row if its length > 0, and handle the height of the row.
    if len(curr_row) > 0:
        total_height += curr_row[0] if not minimum_found else curr_row[-1]
        rows.append(len(curr_row))

    ############################

    return len(rows), total_height, rows



if __name__ == '__main__':
    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 5

    # Generate the list of sizes, set the default width. 
    sizes = [number * 1000 for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    sets = []

    print("Number of paintings to be used for Program 2 run: " + str(sizes))

    # Generate a list from the specified size down to 1.
    for size in sizes:
        mid_point = size // 2

        # Create a parabolic set of heights, as in Problem S2.
        set = [i for i in range(mid_point, 0, -1)] + [i for i in range(2, mid_point + 1)]
        
        # Add one element to the end to fix the midpoint chop. 
        set.append(set[-1] + 1)

        sets.append(set)
    
    # Open the output file.
    with open("output2.csv", mode = 'w', encoding = 'utf-8', newline = '') as out:
        
        # Create the writer object.
        writer = csv.writer(out, delimiter = ',')

        # Run a test for every set. Write this data to the csv. 
        for set_ in sets:

            # Get the length, and generate a corresponding list of random integers, 1-10. 
            n = len(set_)
            widths = [random.randint(1, 10) for _ in range(n)]

            # Time the run.
            start_time = time.perf_counter()
            output = program2(n, W, set_, widths)
            end_time = time.perf_counter()

            elapsed_time = end_time - start_time

            # Print the output of the program2 run. 
            #print(output[0])
            #print(output[1])
            #for i in output[2]:
            #    print(i)

            # Write the size and elapsed time to the csv. 
            writer.writerow([n, elapsed_time])
        
        print("Program 2 test complete. Check for output2.csv in program2.py directory.")