from typing import List, Tuple, Optional
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

    WIDTH_EXCEEDED = sys.maxsize

    # Compute the cost matrix C
    C = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(WIDTH_EXCEEDED)
        C.append(row)
    for i in range(n):
        for j in range(i, n):
            t_w = sum(widths[i:j+1])
            m_h = max(heights[i:j+1])
            if t_w <= W:
                C[i][j] = m_h
            else:
                C[i][j] = WIDTH_EXCEEDED

    # Initialize dp array M and backtracking array P
    M = [WIDTH_EXCEEDED] * (n + 1)
    P = [-1] * (n + 1)
    M[0] = 0

    # Calculate min cost for each position with values in C
    for i in range(1, n + 1):
        for j in range(i):
            if C[j][i - 1] != WIDTH_EXCEEDED:
                cost = M[j] + C[j][i - 1]
                if cost < M[i]:
                    M[i] = cost
                    P[i] = j

    # Check if valid solution actually exists for M[n]
    if M[n] == WIDTH_EXCEEDED:
        return -1, -1, []

    # Reconstruct platform solution with backtracking with P
    lens = []
    i = n
    while i > 0:
        j = P[i]
        lens.append(i - j)
        i = j
    lens.reverse()

    # Calculate the total number of platforms and the optimal cost
    total_platforms = len(lens)
    total_cost = M[n]
    return total_platforms, total_cost, lens

if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program4(n, heights, widths, W)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
