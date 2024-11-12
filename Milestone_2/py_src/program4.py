from typing import List, Tuple

def algo4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 4

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
    # cache for memoization and also cache for tracking platforms and counts
    cache = {}
    platform_count_cache = {}
    paintings_on_platforms_cache = {}

    def calc_min_height(num_paintings):
        # base case (no paintings left)
        if num_paintings == 0:
            return 0

        # return cached results if they already exist
        if num_paintings in cache:
            return cache[num_paintings]

        # initialize minimum height for this number of paintings
        min_height = float('inf')
        min_platforms = 0
        best_platform_counts = []

        # try all possible start points for partitions stopping at `num_paintings`
        start = 0
        while start < num_paintings:
            total_width_for_current_partition = 0
            max_height_in_partition = 0
            painting_index = start

            # try adding paintings to the current partition (`start` to `num_paintings`)
            while painting_index < num_paintings:
                total_width_for_current_partition += widths[painting_index]
                max_height_in_partition = max(max_height_in_partition, heights[painting_index])
                painting_index += 1

            # check if current partition width is within W limit
            if total_width_for_current_partition <= W:
                # Calculate the total height for this partition
                total_height = calc_min_height(start) + max_height_in_partition

                # if this partition yields a better total height, update min_height
                if total_height < min_height:
                    min_height = total_height
                    min_platforms = platform_count_cache.get(start, 0) + 1
                    best_platform_counts = paintings_on_platforms_cache.get(start, []) + [num_paintings - start]

            start += 1

        # cache results for the num paintings
        cache[num_paintings] = min_height
        platform_count_cache[num_paintings] = min_platforms
        paintings_on_platforms_cache[num_paintings] = best_platform_counts
        return min_height

    # calculate minimum total height and retrieve platform details
    optimal_total_height = calc_min_height(n)
    number_of_platforms = platform_count_cache.get(n, 0)
    paintings_per_platform = paintings_on_platforms_cache.get(n, [])

    return number_of_platforms, optimal_total_height, paintings_per_platform

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
    
