# Experimental Comparative Study

## Method
For Milestone 2, we had program3 written in C++, and programs 4, 5A, and 5B written in Python. As such, program3 was tested individually, but all the tests followed the same format. 

We used five tests for each program, with varying numbers of elements for each. The heights in these tests use a random set of integers in $\mathbb{Z^+}$, where the length of the test set is equivalent to $5$ increasing multiples of $15$ for program3, and $5$ increasing multiples of $1000$ for 4, 5A, and 5B. The difference in the multiple sizes is due to the necessary execution time, as program3 is exponential and a minimum of $1000$ elements would have a worst-case time complexity of $1000 * 2^{1000}$. We simply do not have enough time as a species to test this way. 

Widths are generated as a random number $1$ through $10$ for the same length as the list of heights. The maximum row width is always constant throughout our tests. 

Each test was run five times and averaged to get the performance time for the specified number of elements, and then the dataset size and average time were ouput in a single row in a CSV file for that program, with the number of data rows equaling the number of multiples. 

## Performance Comparison
For our tests, we used five multiples of $15$ for program3, and five multiples of $1000$ for program4, 5A, and 5B. We decided this difference was necessary while waiting excessively for test results from program3. Test set sizes for program3 include: $[15, 30, 45, 60, 75]$. Test set sizes for program4, 5A, and 5B include $[1000, 2000, 3000, 4000, 5000]$. 

Again, heights are randomly generated for a list whose length is equal to each of the aforementioned sizes, and widths are randomly generated $1$ through $10$ for the same size as each height list. Each size has *one* corresponding randomly generated list, which is tested five times in this case, since we wanted the average of five runs. 

Executions of programs 4, 5A, and 5B must occur separately since one test file was written for modularity, and so operate on the same list sizes, but not the same list contents. 

#### NOTE: Plot 3 is logarithmic in base 10 for Execution Time. Plot 7 is logarithmic in base 10 for Input Size. 

### Data
![Algorithm 3 Test Data](Test_Data_A3.png)
![Algorithm 4 Test Data](Test_Data_A4.png)
![Implementation 5A Test Data](Test_Data_A5A.png)
![Implementation 5B Test Data](Test_Data_A5B.png)
![Aggregate Overlay Data](Aggregate_Overlay.png)
![Algorithm 5 Dual Comparison Data](Algorithm_5_Comparison.png)


| Algorithm 3                |                           | Algorithm 4                |                           |
|----------------------------|---------------------------|----------------------------|---------------------------|
| **Input Size**             | **Execution Time (s)**    | **Input Size**             | **Execution Time (s)**    |
| 15                         | 0.000856                  |                            |                           |
| 30                         | 0.002066                  |                            |                           |
| 45                         | 1.31418                   |                            |                           |
| 60                         | 19.2536                   |                            |                           |
| 75                         | 345.194                   |                            |                           |

| Algorithm 5A               |                           | Algorithm 5B               |                           |
|----------------------------|---------------------------|----------------------------|---------------------------|
| **Input Size**             | **Execution Time (s)**    | **Input Size**             | **Execution Time (s)**    |
| 1000                       | 0.00757                   | 1000                       | 2.062898                  |
| 2000                       | 0.031542                  | 2000                       | 15.99108                  |
| 3000                       | 0.071792                  | 3000                       | 53.11088                  |
| 4000                       | 0.126121                  | 4000                       | 131.0691                  |
| 5000                       | 0.196439                  | 5000                       | 268.2222                  |

### Analysis
<!-- Analyze Performance Here!-->