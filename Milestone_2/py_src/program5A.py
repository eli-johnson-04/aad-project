from typing import List, Tuple
import sys
WIDTH_EXCEEDED = sys.maxsize

    
def program5A(n: int, W: int, heights: List[int], widths: List[int], C: List[int], opt: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
    
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

        # Get the return value from opt array if it exists, otherwise calculate recursive value.
        ret = None
        if opt[i] != None:
            ret = opt[i]
        else:
            ret = program5A(i, W, tmpHeights, tmpWidths, C, opt)

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
    opt[n - 1] = result
    return result


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    # Create a new vector for all C_ij values.
    c = [[] for _ in range(n) ]
    opt = [None for _ in range(n)]

    '''
    Iterate over all c_ij values to determine the height of the tallest sculpture in all possible rows of width W. 
    This list accessed with the n'th sculpture used as the first index, and the i value used as the second. 
    '''
    for j in range(n, 0, -1):
        for i in range(j):
            tmpWidths = widths[i:j]
            ij_width = sum(tmpWidths)
            
            # Width check.
            if ij_width <= W:
                c[j - 1].append(max(heights[i:j]))
            else:
                c[j - 1].append(WIDTH_EXCEEDED)


    m, total_height, num_paintings = program5A(n, W, heights, widths, c, opt)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    