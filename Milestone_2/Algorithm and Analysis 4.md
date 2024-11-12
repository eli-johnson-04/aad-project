# Algorithm and Analysis 4

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 4: Dynamic Programming Solution
<!-- Write Algorithm Details Here!!!!-->

## Analysis
### Time Complexity
<!-- Write Time Complexity Analysis Here!!!!-->

### Correctness
<!-- Write Correctness Analysis Here!!!!-->

### Code
def algo4(n, W, heights, widths):
    cache = {}

    # Recursive func. for calculating min total height for first num_paintings paintings
    def calc_min_height(num_paintings):

        # Base case (no paintings left)
        if num_paintings == 0:
            return 0

        # return cached result if already there
        if num_paintings in cache:
            return cache[num_paintings]

        min_height = float('inf')

        #try all possible start points for partitions stopping at `num_paintings`
        start = 0
        while start < num_paintings:
            total_width_for_current_partition = 0
            max_height_in_partition = 0
            painting_index = start

            # try  adding paintings to current partition (`start` to `num_paintings`)
            while painting_index < num_paintings:
                # Get total width for all the paintings in the current partition
                total_width_for_current_partition += widths[painting_index]
                # Track the max height in partition
                max_height_in_partition = max(max_height_in_partition, heights[painting_index])
                painting_index += 1

            # See if current partition width is within W limit
            if total_width_for_current_partition <= W:
                # Calculate total height if we end this partition here
                total_height = calc_min_height(start) + max_height_in_partition
                # if this partition is better, change min_height
                min_height = min(min_height, total_height)

            start += 1

        cache[num_paintings] = min_height
        return min_height

    return calc_min_height(n)
