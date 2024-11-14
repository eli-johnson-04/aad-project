# Algorithm and Analysis 5

## Algorithm 5: Efficient Dynamic Programming Solution
### Definition
This algorithm closely follows Algorithm 3. To design a $\Theta(n^2)$ algorithm, we can employ memoization to avoid recomputing solutions to subproblems. 

$OPT(j) =$ The minimized $cost$ of arranging $j$ paintings into rows, where $j$ is the *rightmost* painting being examined. In this formulation, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a painting $p_k \in r_j$.

### Goal
$OPT(n) =$ the minimized $cost$ of arranging $n$ paintings into rows. 

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

### Backtracking to Determine Painting Attendance 
Determining painting attendance in rows follows the exact strategy present in Algorithm 3.
At each $OPT$ step, one must find the difference $j - i + 1$, which represents the length of the now-calculated row. This length should be added to the end of a list of row lengths, so that recursive calls create the row list in the correct order as they return upward. Afterward, one can simply examine the list of paintings from left to right, counting the corresponding number for a given row to determine which paintings belong in that row. 

### 5A: Top-Down Recursive Implementation
Algorithm 5A is an implementation of Algorithm 5 that uses memoization and recursion to construct optimal solutions to subproblems of $OPT(j)$ as needed. 

$\begin{aligned}
& \text{Top-Down-OPT}(n, W, h_1, \cdots, h_n, w_1, \cdots, w_n) \text{: } \\
& \quad \text{Precompute all } C_{ij} \text{ for } C[n][n] \text{ (one-based indexing): } \\
& \qquad \text{For } j=n \text{ to } j=1 \text{: } \\
& \qquad \quad \text{For } i=1 \text{ to } i=j \text{: } \\
& \qquad \qquad \text{if (} \sum_{k=i}^{j} w_k \leq W \text{): } \\
& \qquad \qquad \quad C[i][j] \leftarrow \max_{i \leq k \leq j}(h_k). \\
& \qquad \qquad \text{else: } \\
& \qquad \qquad \quad C[i][j] \leftarrow \infty. \\
& \\
& \quad \text{Initialize OPT array } M[n]. \\
& \quad M[0] \leftarrow 0. \\
& \quad \text{Return TD-OPT}(n). \\
& \\
& \text{TD-OPT}(j) \text{: } \\
& \quad \text{if (}M[j] \text{ is uninitialized} \text{): } \\
& \qquad M[j] \leftarrow \min_{1 \leq i \leq j}(C[i][j] + \text{TD-OPT}(i-1)).  \\
& \quad \text{Return } M[j].
\end{aligned}$

### 5B: Bottom-Up Iterative Implementation
Algorithm 5B is an implementation of Algorithm 5 that uses memoization and iteration to construct optimal solutions to subproblems of $OPT(j)$, starting at $OPT(1)$ and working up to $OPT(j)$. 

$\begin{aligned}
& \text{Bottom-Up-OPT}(n, W, h_1, \cdots, h_n, w_1, \cdots, w_n) \text{: } \\
& \quad \text{Precompute all } C_{ij} \text{ for } C[n][n] \text{ (one-based indexing): } \\
& \qquad \text{For } j=n \text{ to } 1 \text{: } \\
& \qquad \quad \text{For } i=1 \text{ to } j \text{: } \\
& \qquad \qquad \text{if (} \sum_{k=i}^{j} w_k \leq W \text{): } \\
& \qquad \qquad \quad C[i][j] \leftarrow \max_{i \leq k \leq j}(h_k). \\
& \qquad \qquad \text{else: } \\
& \qquad \qquad \quad C[i][j] \leftarrow \infty. \\
& \\
& \quad \text{Initialize OPT array } M[n]. \\
& \quad M[0] \leftarrow 0. \\
& \quad \text{For } k=1 \text{ to } n \text{: } \\
& \qquad M[k] = \min_{1 \leq i \leq k}(C_{ik} + M[i-1]). \\
& \\
& \quad \text{Return } M[n].
\end{aligned}$


## Analysis
### Time Complexity
#### 5A: Top-Down
Algorithm 5A precomputes all values of $C_{ij}$, taking $\Theta(n^2)$ time to do so, as all $n$ paintings are checked no fewer and no more than $n$ times each. Afterward, all $n$ values of the OPT-array $M$ require $n$ comparisons against the rest of the painting list to determine the minimum possible value. This takes $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

#### 5B: Bottom-Up
Algorithm 5B, just like 5A, precomputes all $C_{ij}$ values in $\Theta(n^2)$ time. The difference is now that we iterate from $1$ to $n$, making $n$ comparisons at each step, traking $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

### Correctness
We begin by establishing the following assumption, that no painting is, by itself, too wide to fit on a platform: 
$$
\forall 1 \leq k \leq n, \nexists p_k \text{ where } w_k > W.
$$

We will now examine the construction of $C_{ij}$ values. These values represent, at index $C[i][j]$, the cost of a row containing paintings $[p_i, \cdots, p_j]$ for $1 \leq i \leq j$, calculated as the height of the tallest painting on the platform. Thus, any value of $C_{ij}$ can be used to determine the relative *worth* of row $[p_i, \cdots, p_j]$. These values are used to determine the best combination of rows, since rows that cannot exist are marked as $C_{ij} = \infty$ and will therefore never be chosen over a smaller value. We now establish the following invariant:

__$\text{I1}$: At the end of each iteration of the inner loop of $C_{ij}$ computation, $C[i][j]$ correctly stores the maximum height of a row containing paintings $p_i$ to $p_j$, as long as the combined widths of the paintings do not exceed $W$.__ 

From our initial assumption, we also establish the second invariant:

__$\text{I2}$: There always exists an arrangement of $n$ paintings $p_1, \cdots, p_n$ into rows, as every painting is permitted to sit on its own row, whose cost will be $C[k][k] = h_k, \forall 1 \leq k \leq n$.__ 

The proof of Algorithm 5 strongly resembles that of Algorithm 3, and the use of memoization dramatically reduces the running time. We will now prove using induction that Algorithm 5 produces the correct, optimal, minimized cost of organizing the paintings into rows. 

*Proof:* For $\text{OPT}(j)$ where $j=1$, the case is simple. A set of one painting has only itself to be placed in a row, so the maximum height of the row is $C[1][1]+ 0=h_1$, that of the singular painting, following and upholding $\text{I2}$.

Moving forward, when $j > 1$, Algorithm 5 checks for the existence of $M[j]$, the minimum cost of placing $j$ paintings into rows. If $M[j]$ has not been initialized, then $\text{OPT}(j)$ computes the value of the minimum cost over $i$ for $C_{ij} + \text{OPT}(i-1)$, recursively calculating the minimum possible cost of a row being created whose rightmost painting is $p_j$. For $\text{OPT}(i-1)$, Algorithm 5 follows the same check-and-recurse pattern for returning the cost of the next row that ends at $p_{i-1}$. Because we do not modify values in $C$, $\text{I1}$ is upheld, and we are guaranteed to compute the minimum cost for all $M[k]$ for $1 \leq k \leq j$. The value of $\text{OPT}(j)$ is minimized at every recursive step, whose solution is calculated upon the existence of optimal solutions to previous subproblems. By using the optimal substructure property of Problem G, Algorithm 5 properly constructs a correct solution, outputting the minimized cost of a set of paintings by finding the minimum cost of a row, over all possible rows ending on a painting $p_j$, over all $1 \leq j \leq n$. This completes our proof, and shows that Algorithm 5 correctly computes the minimum-cost arrangement of paintings in every recursive call from $\text{OPT}(j)$ to $\text{OPT}(1)$.