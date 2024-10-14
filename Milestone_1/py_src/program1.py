from typing import List, Tuple
import csv, random, time

def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1
    
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
    # Add you code here
    ############################

    rows = [] # store list of integers, each index is number of items on row

    i = 0               # Painting index
    curr_row_width = 0  # Current row width
    curr_row = []       # Current row contents
    total_height = 0    # Total height

    # Iterate through every painting. 
    while i < n:

        # Check if the row has space for the painting.
        if curr_row_width + widths[i] <= W: 

            # Add the height of painting i to the current row. 
            curr_row.append(heights[i])

            # Add painting i's width to current row width. 
            curr_row_width += widths[i]

            # Proceed to next painting
            i += 1

        # If the painting does not fit, the row is full. Move to the next row. 
        else: 

            # The first painting in every row is the tallest. 
            total_height += curr_row[0]

            # Document the current row length, clear it and reset its width, and continue. 
            rows.append(len(curr_row))
            curr_row.clear()
            curr_row_width = 0
            continue

    # Once all paintings have been checked, add the last row and its height. 
    total_height += curr_row[0]
    rows.append(len(curr_row))

    return len(rows), total_height, rows # replace with your code


if __name__ == '__main__':
    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 12
    # Change TEST_AVERAGING to get the average time of n tests
    NUM_TEST_AVERAGES = 5

    # Name of output file. 
    outFile = "../output1.csv"

    # Generate the list of sizes, set the default width. 
    sizes = [number * 1000 for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    sets = []

    print("Number of paintings to be used for Program 1 run: " + str(sizes))

    # Generate a list from the specified size down to 1.
    for size in sizes:
        sets.append(sorted([random.randint(1, 1000 * SIZE_MULTIPLES) for x in range(size, 0, -1)], reverse=True))
    
    # Open the output file.
    with open(outFile, mode = 'w', encoding = 'utf-8', newline = '') as out:
        
        # Create the writer object.
        writer = csv.writer(out, delimiter = ',')

        # Section Labels
        writer.writerow(["Input Size", "Execution Time"])

        # Run a test for every set. Write this data to the csv. 
        for set_ in sets:

            # Get the length, and generate a corresponding list of random integers, 1-10. 
            n = len(set_)
            widths = [random.randint(1, 10) for _ in range(n)]

            # Time the run.
            times = []
            for i in range(NUM_TEST_AVERAGES):
                start_time = time.perf_counter()
                output = program1(n, W, set_, widths)
                end_time = time.perf_counter()
                times.append(end_time - start_time)

            # Get the average running time. 
            avg = sum(times) / NUM_TEST_AVERAGES

            # Print the output of the program1 run. 
            #print(output[0])
            #print(output[1])
            #for i in output[2]:
            #    print(i)

            # Write the size and elapsed time to the csv. 
            writer.writerow([n, avg])
        
        print("Program 1 test complete. Check for output1.csv in program1.py parent directory.")