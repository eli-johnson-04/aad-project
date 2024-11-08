from typing import List, Tuple
import sys

def calc_C(first: int, last: int):
    return 0

    
def program3(n: int, W: int, heights: List[int], widths: List[int], C: List[List[int]]) -> Tuple[int, int, List[int]]:
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
    if n < 1 or W == 0:
        return 0, 0, []
    
    best_i = -1
    min_C = sys.maxsize
    for i in range(n - 2):
        if C[i][n - 1] < min_C:
            best_i = i
            min_C = C[i][n - 1]
    
    return (min_C + program3(best_i - 1, W, heights, widths, C)[0], 0, [])


    ############################


    #return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    c = [[-1] * n for _ in range (n)]
    for i in range(n - 1, 0, -1):
        for j in range(0, i - 1):
            if sum(widths[j:i]) <= W:
                c[i][j] = max(heights[j:i])

    m, total_height, num_paintings = program3(n, W, heights, widths, c)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    