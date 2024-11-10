from typing import List, Tuple
import sys

def program3(n: int, heights: List[int], widths: List[int], C: List[List[int]]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 3
    
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
    # if n < 1 or W == 0:
    #     return 0, 0, []
    
    # best_i = -1
    # min_C = sys.maxsize
    # for i in range(n - 2):
    #     if C[i][n - 1] < min_C:
    #         best_i = i
    #         min_C = C[i][n - 1]
    
    # return (min_C + program3(best_i - 1, W, heights, widths, C)[0], 0, [])
    ############################

    # Check for invalid input.
    if n < 1 or W <= 0:
        return 0, 0, []
    
    # Base case.
    elif n == 1:
        return 1, heights[0], [1]
    
    min_C = min(C[n - 1])
    next_n = C[n - 1].index(min_C) + 1
    ret = program3(next_n, heights[:next_n], widths[:next_n], C)
    return 1 + ret[0], min_C + ret[1], ret[2]

    #return 0, 0, [] # replace with your code


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    # Create a list of all possible c_ij values, instantiating all of them to infinity. 
    c = [[sys.maxsize] * n for _ in range (n)]

    # Iterate over all c_ij values to determine the height of the tallest painting in all possible rows of width W. 
    # This list accessed with the n'th sculpture used as the first index, and the i value used as the second. 
    for j in range(n, 0, -1):
        for i in range(0, j):
            if sum(widths[i:j]) <= W:
                c[j - 1][i] = max(heights[i:j])

    m, total_height, num_paintings = program3(n, heights, widths, c)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    