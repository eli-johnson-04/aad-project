# Algorithm and Analysis 4

## Algorithm 4: Inefficient Dynamic Programming Solution
### Definition
$OPT(j)=$ The minimized *cost* of arranging $j$ paintings into platforms, where $j$ is the *rightmost* painting being considered. In this formulation, the cost of a platform is equal to the height of the tallest painting on the platform, and the total cost is the sum of the costs of all platforms. Mathematically, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a painting $p_k \in r_j$.

$OPT(i)$ returns the value $M[i]$, where $M[i]$ represents the minimum combined height required to arrange paintings $p_1, \cdots, p_i$ into rows. This solution uses a cost matrix $C_{ij}$ to precompute the cost of valid platform arrangements. 

### Goal
$OPT(n)=M[n]=$ the minimized cost of arranging $n$ paintings into rows.

### Computing $OPT(j)$
Let $C_{ij}$ represent a cost matrix, providing the height of the tallest painting in the platform $[s_i, \cdots, s_j]$, where a valid row is one such that the sum of the widths of its constituent paintings does not exceed $W$. $C_{ij}$ is represented by:  

$$
C_{ij} = 
\begin{cases}
    \infty & \text{if } \sum_{k=i}^{j} w_k > W \\
    \max_{i \leq k \leq j}(h_k) & \text{otherwise}
\end{cases}
$$

We can represent $M[i]$ using the following recurrence relation:

$$
M[i] = 
\begin{cases}
    0 & \text{if } i=0 \\
    \min_{1 \leq j \leq i}(M[j] + C_{j, i-1}) & \text{if } i > 0 \text{ and } C_{j,i-1} \not= \infty \\
    \infty & \text{ otherwise} \\
\end{cases}
$$

### Backtracking to Determine Painting Attendance
We can use backtracking to determine the exact paintings present in each platform. This is found through the minimum-cost path, which is calculated using the dynamic programming array $M$ and supplementary array $P$. We begin at $i=n$. At each $OPT(i)$ step we take, we add $M[i]$ to our total cost, and trace backward using $P[i]$, where $P[i]$ represents the location of the painting that sits at the *end* of the preceding platform. This provides the starting index of the platform with the smallest cost for arranging the first $i$ paintings. The number of paintings on this platform is equal to $i - P[i]$, so by tracing $i = n$ to $0$ in $P$, we compute lengths of the platforms, but in reversed order. To correct this, we simply reverse the sequence. 

## Analysis
### Time Complexity
To compute the cost matrix $C_{ij}$, the outer loop over $i$ runs $n$ times, the inner loop over $j$ runs from $i$ to $n-1$ for each $i$, requiring $n$ iterations, and the innermost loop over $s$ executes $\Theta(n)$ times in the worst case for each $(i, j)$ pair. In total, computing the cost matrix is $\Theta(n^3)$.

Calculating the minimum cost for every position using $C_{ij}$ necessitates dynamic programming. To fill the $M$ and $P$ arrays, the outer loop over $i$ runs $n$ times, and the inner loop over $j$ runs $0$ to $i - 1$ times. So, the time complexity for this is $\Theta(n^2)$.

Finally, reconstructing the solution uses backtracking, and the loop to backtrack runs once from $i = n$ to $0$, requiring $\Theta(n)$ time.

$\Theta(n + (n - 1) + (n - 2) + \cdots + 1) = \Theta\left(\frac{n(n+1)}{2}\right) = \Theta(n^3)$

$\Theta(n^3)$ dominates our time complexity calculation, so this is our result.

### Correctness
We begin by establishing the following assumption, that no painting is, by itself, too wide to fit on a platform: 
$$
\forall 1 \leq k \leq n, \nexists p_k \text{ where } w_k > W.
$$

We will now examine the construction of $C_{ij}$ values. These values represent, at index $C[i][j]$, the cost of a row containing paintings $[p_i, \cdots, p_j]$ for $1 \leq i \leq j$, calculated as the height of the tallest painting on the platform. Thus, any value of $C_{ij}$ can be used to determine the relative *worth* of row $[p_i, \cdots, p_j]$. These values are used to determine the best combination of rows, since rows that cannot exist are marked as $C_{ij} = \infty$ and will therefore never be chosen over a smaller value. We now establish the following invariant:

__$\text{I1}$: At the end of each iteration of the inner loop of $C_{ij}$ computation, $C[i][j]$ correctly stores the maximum height of a row containing paintings $p_i$ to $p_j$, as long as the combined widths of the paintings do not exceed $W$.__ 

From our initial assumption, we also establish the second invariant:

__$\text{I2}$: There always exists an arrangement of $n$ paintings $p_1, \cdots, p_n$ into rows, as every painting is permitted to sit on its own row, whose cost will be $C[k][k] = h_k, \forall 1 \leq k \leq n$.__ 

This guarantees feasibility.

We will now prove that Algorithm 4 produces correct, minimum-cost output using the optimal substructure property. 

*Proof:* This part resembles Algorithm 3. Let $OPT(j)$ represent the optimal solution for the first $j$ paintings. Then, for any $P[i]$ where $1 \leq i \leq j$, $OPT(j) = \min_{1 \leq i leq j}(C_{ij} + P{T(i-1)})$. We can say that this holds because if we have computed $M[i-1]$ and the cost $C_{ij}$ of the row starting at $i$ and ending at $j$, then the optimal solution must select the split point $P[i]$ that minimizes the sum $M[i-1] + C_{ij}$.

By $\text{I1}$, we know that all valid platform arrangements will be considered, and by $\text{I2}$ we know that a feasible solution exists. As we previously stated, we know that Algorithm 4 must check all possible points in $P$, so all valid solutions will be considered. 

Last, we prove that Algorithm 4 produces the minimum cost. For all values in $M$, we know that $M[k]$ will store the minimum cost for paintings $1$ through $k$. The recurrence relation defined above always takes the minimum over all possible $P$, so no better solution can exist, as it would contradict the optimal substructure property. Thus, we have proven that Algorithm 4 produces a correct, minimum-cost solution. 