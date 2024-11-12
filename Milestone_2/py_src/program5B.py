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

    # Create a new vector for all C_ij values.
    c = [[] for _ in range(n) ]

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

    opt = [None for _ in range(n + 1)]

    opt[0] = (0, 0, [])
    for k in range(1, n + 1):
        options = []
        for i in range(1,k+1):
            rows = (k >= 1) + opt[i - 1][0]
            cost = c[k - 1][i - 1] + opt[i - 1][1]
            row_lengths = opt[i - 1][2][:]
            row_lengths.append(k - i + 1)
            options.append((rows, cost, row_lengths))

        opt[k] = min(options, key=lambda x: x[1])

    return opt[n] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5B(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    