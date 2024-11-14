from typing import List, Tuple
import sys
WIDTH_EXCEEDED = sys.maxsize

    
def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5B
    
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

    # Create a new list for all C_ij values.
    c = [[] for _ in range(n) ]

    '''
    Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
    This list accessed with the n'th painting used as the first index, and the i value used as the second. 
    '''
    for j in range(n, 0, -1):
        max_height = 0
        curr_width = 0

        for i in range(j, 0, -1):
            curr_width += widths[i-1]

            if curr_width > W: max_height = WIDTH_EXCEEDED
            elif max_height < heights[i-1]: max_height = heights[i-1]
                    
            c[j - 1].insert(0, max_height)

    # Initialize M array of tuples to store optimal values (opt(0) to opt(n)).
    M = [None for _ in range(n + 1)]
    M[0] = (0, 0, [])

    # Generate all values of options from 1 to n inclusive. 
    for k in range(1, n + 1):

        # Contains all possible options, formatted the same as the return tuple. 
        options = [
            (
            (k >= 1) + M[i - 1][0],         # [0] - the number of rows from the previous subproblem solution
            c[k - 1][i - 1] + M[i - 1][1],  # [1] - cost, as the sum of C_ik and the combined height of previous rows
            M[i - 1][2][:] + [k - i + 1]    # [2] - the length of the new row we are constructing
            ) 
            for i in range(1, k + 1)        # over all possible options from 1 to k inclusive
        ]

        # Compare all i to k options, and store the arrangement with minimum cost. 
        M[k] = min(options, key=lambda x: x[1])

    return M[n]


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5B(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    