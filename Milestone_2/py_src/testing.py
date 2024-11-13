# Generic Testing Suite for Milestone 2 Implementations
import csv, random, time
from program4 import program4
from program5A import program5A
from program5B import program5B

def run_test(filename, W, sets, fctn):
    # Open the output file.
    with open(filename, mode = 'w', encoding = 'utf-8', newline = '') as out:
        
        # Create the writer object.
        writer = csv.writer(out, delimiter = ',')

        # Section Labels
        writer.writerow(["Input Size", "Execution Time"])

        # Run a test for every set. Write this data to the csv. 
        for set_ in sets:
            print("Testing " + str(len(set_)) + " elements...")

            # Get the length, and generate a corresponding list of random integers, 1-10. 
            n = len(set_)
            widths = [random.randint(1, 10) for _ in range(n)]

            # Time the run.
            times = []
            for i in range(NUM_TEST_AVERAGES):
                start_time = time.perf_counter()
                output = fctn(n, W, set_, widths)
                end_time = time.perf_counter()
                times.append(end_time - start_time)

            # Get the average running time. 
            avg = sum(times) / NUM_TEST_AVERAGES

            # Write the size and elapsed time to the csv. 
            writer.writerow([n, avg])
        
        print(f"Program test complete. Check for {filename} in parent directory.")


if __name__ == '__main__':
    # Ask the user for the program to be tested.
    prgm = str(input("Input the program to be tested (4, 5A, 5B): "))

    # Change SIZE_MULTIPLES for the number of multiples of 1000 to be used in sizes.
    SIZE_MULTIPLES = 12
    # Change TEST_AVERAGING to get the average time of n tests
    NUM_TEST_AVERAGES = 5

    # Name of output files. 
    outFile = None
    fctn = None
    match prgm:
        case "4": 
            outFile = "../test4.csv"
            fctn = program4
        case "5A": 
            outFile = "../test5A.csv"
            fctn = program5A
        case "5B": 
            outFile = "../test5B.csv"
            fctn = program5B
        case _:
            print("Incorrect program")
            exit

    # Generate the list of sizes, set the default width. 
    sizes = [number * 1000 for number in range(1, SIZE_MULTIPLES + 1, 1)]
    W = 10
    height_sets = []

    print(f"Number of paintings to be used for test run: " + str(sizes))

    # Generate a list from the specified size down to 1.
    for size in sizes:
        height_sets.append(sorted([random.randint(1, 1000 * SIZE_MULTIPLES) for x in range(size, 0, -1)], reverse=True))

    
    run_test(outFile, W, sets, fctn)