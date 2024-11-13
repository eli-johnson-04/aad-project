# Algorithm and Analysis 3

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height. 

## Algorithm 3: Naive Solution
### Definition
$OPT(j) =$ The minimized $cost$ of arranging $j$ paintings into rows, where $j$ is the *rightmost* painting being examined. In this formulation, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a painting $p_k \in r_j$. 

### Goal
$OPT(n) =$ the minimized cost of arranging $n$ paintings into rows.

### Computing $OPT(j)$
Let $C_{ij}$, where $1 \leq i \leq j$, represent the cost of a row consisting of all paintings between and including paintings $p_i$ and $p_j$. We allow $i$ and $j$ to be equivalent because it is possible that a row may have only one painting in an optimum solution. $C_{ij}$ is represented by:
$$
C_{ij} = 
\begin{cases}
    \infty & \text{if } \sum_{k=i}^{j} w_k > W \\
    \max_{i \leq k \leq j}(h_k) & \text{otherwise}
\end{cases}
$$

To compute $OPT(j)$, we take the minimum sum over $i$ for $1 \leq i \leq j$ of $C_{ij}$ and $OPT(i-1)$. In this case, $i-1$ represents the *last* painting in the row preceding painting $p_i$. The following Bellman Equation describes $OPT(j)$:
$$
OPT(j) = 
\begin{cases}
    0 & \text{if } j < 1 \\
    \min_{1 \leq i \leq j}(C_{ij} + OPT(i-1)) & \text{otherwise} \\
\end{cases}
$$

### Backtracking to Determine painting Attendance 
To determine which paintings are present in a given row is not complex, but requires careful attention. At each $OPT$ step, one must find the difference $j - i + 1$, which represents the length of the now-calculated row. This length will  be appended to the end of a row-tracking list, as in our C++ implementation. This way, as recursive calls return upward, the list is generated from the front of the list of paintings to the back. Afterward, one can simply examine the list of paintings, counting the corresponding number for a given row to determine which paintings belong in that row. 

## Analysis
### Time Complexity
We begin by examining the calculation of all $C_{ij}$ values. Beginning at $j = n$ and $i = 1$, with $j$ proceeding backward and $i$ proceeding forward, to and including $j$ in each iteration, we end up with a number of comparisons between painting heights totaling the following: $\Theta(n + (n - 1) + (n - 2) + \cdots + 1) = \Theta(\frac{n(n + 1)}{2}) = \Theta(n^2)$. 

Algorithm 3 recursively chooses the index $i$ for which the sum $C_{ij} + OPT(i - 1)$ is minimized. Given that this index may be arbitrary and all paintings may, in the worst case, optimally belong on each of their own rows, the number of recursive calls can be quite high. However, as soon as a painting is placed in a row, the number of remaining paintings must decrease by at least $1$. Thus, there are $O(2^{n - 1})$ possibilites at each recursive step, followed by an $O(n)$ comparison to determine which produces the minimum cost. In total, we have $O(n2^{n - 1} + n^2) = O(n2^{n - 1})$.

This solution does not memoize or store optimal values from previously-computed subproblem solutions, so it can be no slower than the $C_{ij}$ computation time added to the minimum time needed to recursively calculate all possible values. All possible values must be considered and compared in order to compute an optimum solution, so we arrive at a total complexity of $\Theta(n2^{n-1})$.

### Correctness
To prove the correctness of this algorithm, we can use Induction to establish that the solution of smaller subproblems will subsequently solve the larger subproblem. The function for C precalculates the height of a hypothetical row of paintings i to j. If the paintings in row ij have a width greater than W, the function will assign a height of $\infin$ to that row of paintings. Otherwise, $C_{ij}$ is set to the maximum height of paintings in the row. These values are precalculated and used during the algorithm to save on time complexity.