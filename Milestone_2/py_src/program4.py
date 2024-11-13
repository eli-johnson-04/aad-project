from typing import List, Tuple

############################

def program4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    # find max height in passed-in range
    def find_max(start, end):
        m_h = 0  # max height var
        for p in range(start, end + 1):
            m_h = max(m_h, heights[p - 1])
        return m_h

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    partition_points = [0] * (n + 1)

    # loop through each number of paintings up to n
    for cur in range(1, n + 1):
        total_w = 0
        # loop (backwards) to check all possible partitions ending at cur
        for partition in range(cur, 0, -1):
            # add width of current painting to total width
            total_w += widths[partition - 1]
            if total_w > W:  # skip this partition if over max width
                break

            # find max height in the current partition
            max_h = find_max(partition, cur)
            temp = dp[partition - 1] + max_h  # compute height if partition ends at cur

            # update dp[cur] if this partition gives a smaller total height
            if temp < dp[cur]:
                dp[cur] = temp
                partition_points[cur] = partition  # Record partition start

    # backtrack to find the numbver of paintings on each platform
    platforms = []
    cur = n
    while cur > 0:
        start = partition_points[cur]
        # number of paintings in this platform
        platforms.append(cur - start + 1)
        # move to the previous partition
        cur = start - 1

    # reverse to get the platforms in the original order
    platforms.reverse()
    number_of_platforms = len(platforms)
    optimal_total_height = dp[n]

    return number_of_platforms, optimal_total_height, platforms

############################


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program4(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
