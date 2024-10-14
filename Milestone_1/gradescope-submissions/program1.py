from typing import List, Tuple


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
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program1(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)