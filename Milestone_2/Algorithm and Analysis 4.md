# Algorithm and Analysis 4

## Algorithm 4: Inefficient Dynamic Programming Solution
### Definition
Let n be the number of paintings that must be arranged on platforms. Each painting, si, has a height hi and a width wi. Furthermore, each platform has the same maximum width W, and the paintings must be displayed in the order they are provided. The cost of placing a group of paintings on a platform is defined by the height of the tallest painting on that platform.

To design this $\Theta(n^3)$ algorithm algorithm, we can use the approach of utilizing a cost matrix and dynamic programming to calculate the minimum height arrangement.

OPT(j): The minimized total height cost of arranging the first j paintings on platforms, where j is the rightmost painting being considered. In this formulation, the cost is calculated as

\[
\text{cost} = \sum_{i=1}^{m} \left( \max_{k \in r_i} h_k \right)
\]

where \( h_k \) is the height of a painting \( p_k \) assigned to platform \( r_i \).
The sum iterates over all platforms \( r_1, r_2, \ldots, r_m \). Every platform cost is decided by the height of the tallest painting on that platform.

### Goal
The goal of the algorithm is to make the total cost (height) of the structure minimal. There are two main components to accomplish this goal. First, no platform can have a width that is larger than W, the maximum allowed platform width. And second, the sum of the heights of the tallest painting on each platform is minimized.

OPT(n) = the minimized cost of arranging n paintings into rows.

### Computing $OPT(j)$
Let $OPT(j)$ be the minimum height cost for placing the first j paintings onto platforms. To compute $OPT(j)$ we must look at the a starting point, i, where i <= j, for the last platform holding paintings si to sj.

C[i][j] is the cost matrix, and it provides the height of the tallest painting for a range si to sj, as long as it is a valid height (W >= width). We can express OPT(j) as:

\[
OPT(j) = \min_{0 \leq i < j} \left( OPT(i) + C[i][j - 1] \right)
\]

where OPT(i) is the minimum cost of arranging the first i paintings, and C[i][j−1] provides the cost of placing the paintings from i to j − 1 on the last platform. Iterating over all starting points for each platform confirms that OPT(j) is the minimal possible height for the first j paintings.

### Backtracking Strategy
In order to find the best arragment of paintings on platforms, backtracking is used to reconstruct the specific grouping of paintings on every platform. This is found by the minimum-cost path, which is calculated using the dynamic programming arrays M and P. At each OPT(i) step we trace back using P[i]. This gives us the starting index of the platform that has the smallest cost for arranging the first i paintings. i - P[i] is the number of paintings on this platform, so by tracing i = n to 0 in P, we get the lengths of the platforms, but in reversed order. To correct this, we simply reverse the sequence. This finally provies the correct optimal sequence.



## Analysis
### Time Complexity
To computer the Cost Matrix, the outer loop over i runs n times, the inner loop over j runs from i to n-1 for each i, requiring around n iterations, and the innermost loop over s executes $\Theta(n)$ times in the worst case for each (i, j) pair. This means that the total time complexity for computing the cost matrix is $\Theta(n^3)$.

Calculating the minimum cost for every position using the C Matrix requires dynamic programming. To fill the M and P arrays, the outer loop over i runs n times, and the inner loop over j runs 0 to i - 1 times. Thus, the time complexity for this segment of the code involved in dynamic programming is $\Theta(n^2)$.

Finally, reconstructing the solution requries backtracking, and the loop to backtrack runs once from i = n to i = 0, giving it $\Theta(n)$ time complexity.

\Theta(n + (n - 1) + (n - 2) + \dots + 1) = \Theta\left(\frac{n(n+1)}{2}\right) = \Theta(n^3)

Because $\Theta(n^3)$ is the time complexity for the matrix computation, this dominates the algorithm, giving it an overall time complexity of $\Theta(n^3)$.



### Correctness

Algorithm 4 uses dynamic programmingt to find the minimum height cost for arrancing n paintings on a structure of platforms, where the paintings but stay in the order they are provided and the width of any platform cannot be greater than W. 

We can establish:
\forall \, 1 \leq k \leq n, \, \nexists \, p_k \text{ where } w_k > W.

Doing so guarantees that the width of any given painting is less W and can fit on a playform.

Next, the values at any C[i][j] in the Cost Matrix are the minimum height cost for puting paintings si to sj on one platform (the height of the tallest painting there). For each pair (i, j), if the total widths from si to sj is less than W, C[i][j] is set to this max height. If not, then it is set to WIDTH_EXCEEDED (infinity). Doing so guarantees that all platform setups are actually possible. We establish the folliwng invariant: 

Invariant I1: At the end of each iteration of the innermost loop in the C[i][j] computation, C[i][j] cirrectly stores the max height for a valid setup of paintings si to sj, as long as their total widths are less than W.

Our initial assumption also allows us to establish the folliwing invariant:

Invariant I2: Since each painting can be given a platform of its own, there will always be a possible arrangment of n s1, ....., sn. If so, the cost of each painting sk with its own platform is C[k][k] = hk, where 1 <= k <= n.

This guarentees feasibility.

So, thanks to these invariants, the algorithm's correctness is shown, since it verifies that each subproblem will make a contribution to the optimal arrangment.

