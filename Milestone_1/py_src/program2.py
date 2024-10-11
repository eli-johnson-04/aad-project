from typing import List, Tuple
import csv, random, time

    
def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2
    
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
    rows = []                 # num of items on each row
    i = 0                     # index
    curr_row = []             # heights in the current row
    total_height = 0          # total height (cost)
    minimum_found = False
    min_index = 0             # the index of the minimum element

    top_rows = []             # items in top rows (used during process)
    bottom_rows = []          # items in bottom rows (used during process)
    top_row_width = 0         # current width of top row process
    bottom_row_width = 0      # total width of bottom row process

    while i < n:
        if not minimum_found: # run until minimum has been found
            if top_row_width + widths[i] <= W: # if current item fits within row
                curr_row.append(heights[i]) # add to row
                top_row_width += widths[i] # add painting width to total

            else: # if painting does not fit in row
                top_rows.append(curr_row[:]) # add copy of current row to top rows list
                curr_row.clear() # clear current row
                top_row_width = 0 # set top_row_width to 0 to test with new row values
                i -= 1 # test current painting again
                
            if heights[i + 1] > heights[i]: # if next painting is wider than current painting
                top_rows.append(curr_row[:]) # add current row to list
                curr_row.clear() # clear current row
                min_index = i # document current index
                minimum_found = True # mark minimum found

            i += 1 # test next element

        else: # once minimum is found, approach from right side going left
            # -(i - min_index) counts -1, -2, -3, ... until it reaches -min_index
            if bottom_row_width + widths[-(i - min_index)] <= W: # if current painting fits on row
                curr_row.insert(0, heights[-(i - min_index)]) # add current painting to beginning of row
                bottom_row_width += widths[-(i - min_index)] # update bottom row width
            else: # if painting does not fit on row...
                bottom_rows.insert(0, curr_row[:]) # add on top of bottom rows
                curr_row.clear() # clear current row
                bottom_row_width = 0 # clear bottom orw width
                i -= 1 # test current painting again

            i += 1 # test next element
    else:
        bottom_rows.insert(0, curr_row[:]) # if last item has been tested, add current row to bottom rows

    # if top_rows and bottom_rows both have elements, neither width is 0 (last row is full), and both rows can legally combine...
    if top_rows and bottom_rows and not (top_row_width == 0) and not (bottom_row_width == 0) and top_row_width + bottom_row_width <= W:
        # count rows of top_rows and bottom_rows, combining last row of top_rows with first row in bottom_rows
        rows = [len(curr_row) for curr_row in top_rows[:-1]] + [len(top_rows) + len(bottom_rows[0])] + [len(curr_row) for curr_row in bottom_rows[1:]]
    else:
        # count rows of top_rows and bottom_rows and combine to rows
        rows = [len(curr_row) for curr_row in top_rows] + [len(curr_row) for curr_row in bottom_rows]


    ############################

    return len(rows), total_height, rows



if __name__ == '__main__':
    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 1
    # Change TEST_AVERAGING to get the average time of n tests
    NUM_TEST_AVERAGES = 1

    # Generate the list of sizes, set the default width. 
    sizes = [number * 10 for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    sets = []

    print("Number of paintings to be used for Program 2 run: " + str(sizes))

    # Generate a list from the specified size down to 1.
    for size in sizes:
        minimum = random.randint(1, size - 1)

        # Create a parabolic set of heights, as in Problem S2.
        set = sorted([random.randint(1, 1000) for i in range(minimum)], reverse=True) + sorted([random.randint(1, 1000) for i in range(size - minimum)])

        sets.append(set)
    
    # Open the output file.
    with open("output2.csv", mode = 'w', encoding = 'utf-8', newline = '') as out:
        
        # Create the writer object.
        writer = csv.writer(out, delimiter = ',')

        # Run a test for every set. Write this data to the csv. 
        for set_ in sets:

            # Get the length, and generate a corresponding list of random integers, 1-10. 
            n = len(set_)
            widths = [random.randint(1, 5) for _ in range(n)]

            # Time the run.
            times = []
            for i in range(NUM_TEST_AVERAGES):
                start_time = time.perf_counter()
                output = program2(n, W, set_, widths)
                end_time = time.perf_counter()
                times.append(end_time - start_time)

            # Get the average running time. 
            avg = sum(times) / NUM_TEST_AVERAGES

            # Print the output of the program2 run. 
            #print(output[0])
            #print(output[1])
            #for i in output[2]:
            #    print(i)

            # Write the size and elapsed time to the csv. 
            writer.writerow([n, avg])
        
        print("Program 2 test complete. Check for output2.csv in program2.py directory.")