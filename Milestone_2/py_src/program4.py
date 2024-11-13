from typing import List, Tuple
import sys

WIDTH_EXCEEDED = sys.maxsize


def program4(n: int, heights: List[int], widths: List[int], W: int) -> Tuple[int, int, List[int]]:
    """
    Parameters:
    n (int): number of paintings
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings
    W (int): maximum width of the platform

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """

    # Precompute C[i][j] (the max height of placing paintings from i to j on a platform)
    C = []
    for i in range(n):
        row = [WIDTH_EXCEEDED] * n
        C.append(row)
    for i in range(n):
        for j in range(i, n):
            t_w = sum(widths[i:j + 1])
            m_h = max(heights[i:j + 1])
            if t_w <= W:
                C[i][j] = m_h

    # Initialize the dytnamic programming array M as well as backtracking array P
    M = [WIDTH_EXCEEDED] * (n + 1)
    P = [-1] * (n + 1)
    M[0] = 0

    # Calc min cost for each position using prev computed values
    for i in range(1, n + 1):
        cuts = []
        for j in range(i):
            c_val = C[j][i - 1]
            if c_val != WIDTH_EXCEEDED:
                cost = M[j] + c_val
                cuts.append((cost, j))

        M[i], P[i] = min(cuts, key=lambda x: x[0])

    # Reconstruct the platform solution using backtracking with P array
    row_lens = []
    i = n
    while i > 0:
        j = P[i]
        row_lens.append(i - j)
        i = j
    row_lens.reverse()

    # Calculate the total number of platforms and the optimal total cost
    total_platforms = len(row_lens)
    total_cost = M[n]
    return total_platforms, total_cost, row_lens


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program4(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
