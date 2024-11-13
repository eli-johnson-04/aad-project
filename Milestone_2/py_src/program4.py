from typing import List, Tuple
import sys

def program4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    '''
    Solution to Program 4

    Parameters:
    n (int): number of paintings
    W (int): maximum row width
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns: 
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    '''
    # Find the cost of the row from painting_start to painting_end.
    def row_cost(start, end):
        max_h = 0  # max height

        # Iterate over all paintings in the row.
        for p in range(start, end + 1):
            max_h = heights[p - 1] if (heights[p - 1] > max_h) else max_h
            
        return max_h
    
    # Set up dynamic programming array of size n + 1. 
    infinity = sys.maxsize
    dp = [infinity] * (n + 1)
    dp[0] = 0

    # For any x where painting x is the end of a row, p[x] contains that row's starting index. 
    p = [0] * (n + 1)

    # Iterate over all paintings 1 to n inclusive. 
    for j in range(1, n + 1):
        total_w = 0 # combined with of all paintings in a row

        # Beginning at cur, iterate backward to zero to check all possible rows ending at j.
        for i in range(j, 0, -1):
            # Add width of current painting to total width.
            total_w += widths[i - 1]

            # Check row validity. 
            if total_w > W:
                break

            # Calculate the cost of row starting at i and ending at j. 
            max_h = row_cost(i, j)

            # The total cost is the sum of the optimal cost of the newly constructed row and of the preceding row, which ends at i - 1.
            total_cost = dp[i - 1] + max_h

            # Update dp[j] if the new height is better. 
            if total_cost < dp[j]:
                dp[j] = total_cost
                p[j] = i

    # This list contains the length of all rows, and its length = the total number of rows. 
    row_lengths = []
    
    # Backtrack to find the number of paintings on each platform. 
    j = n
    while j > 0:
        start = p[j]
        row_lengths.insert(0, j - start + 1)
        
        # Move to the preceding row. 
        j = start - 1

    return len(row_lengths), dp[n], row_lengths


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program4(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
