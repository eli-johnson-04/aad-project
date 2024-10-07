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

    i = 0 # track index
    rowW = 0 # track current row width
    currRow = 0 # track number of items in row
    total_height = 0 # track total height

    while i < n:
        if rowW + widths[i] <= W: # if row width plus next item width <= max allowed width
            currRow += 1 # add item to row counter
            if currRow == 1: # if this is the first item in the row
                total_height += heights[i] # add current height to total height

            rowW += widths[i] # add current width to total row width

            i += 1 # increment index
        else: # if row width plus next item width > max allowed width
            # row is full, move to next row
            rows.append(currRow) # document current row length
            currRow = 0 # reset current row length
            rowW = 0 # reset current row width
            continue # test current index again

    else: # once all items are tested
        rows.append(currRow) # add final row length to list


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
    