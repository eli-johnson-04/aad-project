from typing import List, Tuple

    
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
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    