# Algorithm and Analysis 5

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 5: Efficient Dynamic Programming Solution
### Definition
This algorithm follows Algorithm 3 closely. To design a $\Theta(n^2)$ algorithm, we can employ memoization to avoid recomputing optimal solutions to subproblems. 

$OPT(j) =$ The minimized $cost$ of arranging $j$ sculptures into rows, where $j$ is the *rightmost* sculpture being examined. In this formulation, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a sculpture $s_k \in r_j$.

### Goal
$OPT(n) =$ the minimized $cost$ of arranging $n$ sculptures into rows. 

### Computing $OPT(j)$
Let $C_{ij}$, where $1 \leq i \leq j$ represents the cost of a row consisting of all sculptures between and including sculptures $s_i$ and $s_j$. We allow $i$ and $j$ to be equivalent because it is possible that a row may have only one sculpture in an optimum solution. $C_{ij}$ is represented by: 
$$
C_{ij} = 
\begin{cases}
    \infty & \text{if } \sum_{k=i}^{j} w_k > W \\
    \max_{i \leq k \leq j}(h_k) & \text{otherwise}
\end{cases}
$$

To compute $OPT(j)$, we take the minimum sum of $C_{ij}$ and $OPT(i-1)$, where $i-1$ represents the *last* sculpture in the row preceding sculpture $s_i$. The following Bellman Equation describes $OPT(j)$:
$$
OPT(j) =
\begin{cases}
    0 & \text{if } j < 1 \\
    \min_{1 \leq i \leq j}(C_{ij} + OPT(i-1)) & \text{otherwise} \\
\end{cases}
$$

### 5A: Top-Down Recursive Implementation
Algorithm 5A is an implementation of Algorithm 5 that uses memoization and recursion to construct optimal solutions to subproblems of $OPT(j)$ as needed. 

$
\text{Top-Down-OPT}(n, W, h_1, \cdots, h_n, w_1, \cdots, w_n) \text{: } \\
\quad \text{Precompute all } C_{ij} \text{ for } C[n][n] \text{ (one-based indexing): } \\
\qquad \text{For } j=n \text{ to } j=1 \text{: } \\
\qquad \quad \text{For } i=1 \text{ to } i=j \text{: } \\
\qquad \qquad \text{if (} \sum_{k=i}^{j} w_k <= W \text{): } \\
\qquad \qquad \quad C[i][j] \leftarrow \max_{i \leq k \leq j}(h_k). \\
\qquad \qquad \text{else: } \\
\qquad \qquad \quad C[i][j] \leftarrow \infty. \\
\quad \\
\quad \text{Initialize OPT array } M[n]. \\
\quad M[0] \leftarrow 0. \\
\quad M[1] \leftarrow C[1][1]. \\
\quad \text{TD-OPT}(n). \\
\quad \\
\text{TD-OPT}(j) \text{: } \\
\quad \text{if (}M[j] \text{ is uninitialized} \text{): } \\
\qquad M[j] \leftarrow \min_{1 \leq i \leq j}(C[i][j] + \text{TD-OPT}(i-1)).  \\
\quad \text{Return } M[j].
$

### 5B: Bottom-Up Iterative Implementation
Algorithm 5B is an implementation of Algorithm 5 that uses memoization and iteration to construct optimal solutions to subproblems of $OPT(j)$, starting at $OPT(1)$ and working up to $OPT(j)$. 

$
\text{Bottom-Up-OPT}(n, W, h_1, \cdots, h_n, w_1, \cdots, w_n) \text{: } \\
\quad \text{Precompute all } C_{ij} \text{ for } C[n][n] \text{ (one-based indexing): } \\
\qquad \text{For } j=n \text{ to } 1 \text{: } \\
\qquad \quad \text{For } i=1 \text{ to } j \text{: } \\
\qquad \qquad \text{if (} \sum_{k=i}^{j} w_k <= W \text{): } \\
\qquad \qquad \quad C[i][j] \leftarrow \max_{i \leq k \leq j}(h_k). \\
\qquad \qquad \text{else: } \\
\qquad \qquad \quad C[i][j] \leftarrow \infty. \\
\quad \\
\quad \text{Initialize OPT array} M[n]. \\
\quad M[0] \leftarrow 0. \\
\quad M[1] \leftarrow C[1][1]. \\
\quad \text{For } k=1 \text{ to } n \text{: } \\
\qquad M[k] = \min_{1 \leq i \leq j}(C_{ij} + M[i-1]). \\
\quad \\
\quad \text{Return } M[n]. \\
$


## Analysis
### Time Complexity
#### 5A: Top-Down
Algorithm 5A precomputes all values of $C_{ij}$, taking $\Theta(n^2)$ time to do so, as all $n$ sculptures are checked no fewer and no more than $n$ times each. Afterward, all $n$ values of the OPT-array $M$ require $n$ comparisons against the rest of the sculpture list to determine the minimum possible value. This takes $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

#### 5B: Bottom-Up
Algorithm 5B, just like 5A, precomputes all $C_{ij}$ values in $\Theta(n^2)$ time. The difference is now that we iterate from $1$ to $n$, making $n$ comparisons at each step, traking $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

### Correctness
<!-- Write Correctness Analysis Here!!!!-->