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
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program2(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)