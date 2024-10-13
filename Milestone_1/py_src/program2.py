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
    rows = []                  # Number of items in each row
    i = 0                      # index
    curr_row = []              # heights in the current row
    total_height = 0           # total height (cost)
    minimum_found = False
    min_index = 0              # the index of the minimum element

    top_rows = []              # items in top rows (used during process)
    bottom_rows = []           # items in bottom rows (used during process)
    top_row_width = 0          # current width of top row process
    bottom_row_width = 0       # total width of bottom row process
    top_row_temp_height = 0    # stores height of last row in top_rows
    bottom_row_temp_height = 0 # stores height of last row in bottom_rows

    # Iterate through every painting. 
    while i < n:

        # Add paintings to rows in top_rows until minimum has been found. 
        if not minimum_found:

            # If painting i fits in the current row, add it. 
            if top_row_width + widths[i] <= W:
                curr_row.append(heights[i])

                # If the added painting is the first in the row, add its height to cost, and update the last row's height. 
                if top_row_width == 0:
                    total_height += heights[i]
                    top_row_temp_height = heights[i]

                # Update the width of the current row. 
                top_row_width += widths[i]

            # Otherwise, if the painting does not fit, the row is full. Move to the next row. 
            else:

                # Create a copy of the current row and add it to top_rows. Clear current, and re-test the current painting. 
                top_rows.append(curr_row[:])
                curr_row.clear()
                top_row_width = 0 
                continue
                
            # Check if the minimum has been found. The next painting should be taller than the current. 
            if heights[i + 1] > heights[i]:

                # Add the current row to top_rows, clear current, and mark minimumFound as true. 
                top_rows.append(curr_row[:])
                curr_row.clear()
                min_index = i
                minimum_found = True

            # Proceed to next painting. 
            i += 1

        # Once the min_index has been found, traverse the list from end -> min_index (right -> left)
        else: 
            
            # Check if the current painting (from the right) fits, add it to the current row. 
            # NOTE: -(i - min_index) counts -1, -2, -3, ... until it reaches -min_index
            if bottom_row_width + widths[-(i - min_index)] <= W: 
                curr_row.insert(0, heights[-(i - min_index)])

                # If the painting is the first added to a bottom row, then it is the tallest. 
                # Add its height and store it as the height of the most recent bottom row. 
                if bottom_row_width == 0:
                    total_height += heights[-(i - min_index)]
                    bottom_row_temp_height = heights[-(i - min_index)]

                # Update the width of the current bottom row. 
                bottom_row_width += widths[-(i - min_index)]

            # Otherwise, if the painting does not fit, the row is full. Move to the next row. 
            else:

                # Add the current row to the beginning of bottom_rows. Clear the current row, and re-test the current painting. 
                bottom_rows.insert(0, curr_row[:])
                curr_row.clear()
                bottom_row_width = 0
                continue
            
            # Proceed to next painting. 
            i += 1

    # When there are no more paintings, add the current row to the beginning of bottom_rows. 
    bottom_rows.insert(0, curr_row[:])

    # To combine the last row of top_rows and the last row of bottom_rows, three conditions must be satisfied:
    #   The rows must exist.
    #   Neither row may have a width equal to zero. 
    #   The sum of their widths must not exceed W. 
    rows_exist = top_rows and bottom_rows
    nonzero_widths = (not top_row_width == 0) and (not bottom_row_width == 0)
    sum_less_than_w = top_row_width + bottom_row_width <= W

    if rows_exist and nonzero_widths and sum_less_than_w:

        # Set rows equal to the list of the length of every row in top_rows, 
        # plus the combined lengths of the last in top_rows and the first in bottom_rows, 
        # plus the lengths of rows in bottom_rows.
        rows = ([len(row) for row in top_rows[:-1]] + 
                    [len(top_rows[-1]) + len(bottom_rows[0])] + 
                    [len(row) for row in bottom_rows[1:]])
        
        # Between the two merged rows, subtract the lesser row height from the total. 
        total_height -= min(top_row_temp_height, bottom_row_temp_height)

    # Otherwise, merge the top rows and the bottom rows together. 
    else:

        # Set rows equal to the list of the length of every row in top_rows, plus the length of every row in bottom_rows. 
        rows = [len(row) for row in top_rows] + [len(row) for row in bottom_rows]

    ############################

    # Return the number of rows, the total cost, and the number of paintings in each row. 
    return len(rows), total_height, rows


if __name__ == '__main__':
    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 12
    # Change TEST_AVERAGING to get the average time of n tests.
    NUM_TEST_AVERAGES = 5

    # Name of output file. 
    outFile = "../output2.csv"

    # widths = [5, 5, 3, 3, 4, 2, 2, 5, 2, 5, 3, 3, 3, 5, 5, 4, 3, 4, 1, 3]
    # heights = [9, 8, 8, 8, 7, 7, 6, 6, 6, 5, 4, 3, 2, 1, 1, 4, 6, 7, 8, 10]
    # W = 10
    # n = 10
    # program2(n, W, heights, widths)

    # Generate the list of sizes, set the default width. 
    sizes = [number * 1000 for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    sets = []

    print("Number of paintings to be used for Program 2 run: " + str(sizes))

    # Open the output file.
    with open(outFile, mode = 'w', encoding = 'utf-8', newline = '') as out:
        
        # Create the writer object.
        writer = csv.writer(out, delimiter = ',')

        # Section Labels
        writer.writerow(["Input Size", "Execution Time"])

        # Run a test for every set. Write this data to the csv. 
        for size in sizes:
            minimum = random.randint(1, size - 1)

            # Create a parabolic set of heights, as in Problem S2. The minimum will always be a single value of 1.
            set = (sorted([random.randint(2, 1000) for i in range(minimum)], reverse=True) + [1] +
                    sorted([random.randint(2, 1000) for i in range(size - minimum - 1)]))

            # Get the length, and generate a corresponding list of random integers, 1-10. 
            n = len(set)
            widths = [random.randint(1, 10) for _ in range(n)]

            # Time the run.
            times = []
            for i in range(NUM_TEST_AVERAGES):
                start_time = time.perf_counter()
                output = program2(n, W, set, widths)
                end_time = time.perf_counter()
                times.append(end_time - start_time)

            # Get the average running time. 
            avg = sum(times) / NUM_TEST_AVERAGES

            # Print the output of the program2 run. 
            #print(output[0])
            #print(output[1])
            #for i in output[2]:
            #    print(i)

            # Write the size and elapsed time to the csv. 
            writer.writerow([n, avg])
        
        print("Program 2 test complete. Check for output2.csv in program2.py parent directory.")