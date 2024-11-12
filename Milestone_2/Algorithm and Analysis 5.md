# Algorithm and Analysis 5

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 5: Efficient Dynamic Programming Solution
### Definition
This algorithm closely follows Algorithm 3. To design a $\Theta(n^2)$ algorithm, we can employ memoization to avoid recomputing optimal solutions to subproblems. 

$OPT(j) =$ The minimized $cost$ of arranging $j$ sculptures into rows, where $j$ is the *rightmost* sculpture being examined. In this formulation, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a sculpture $s_k \in r_j$.

### Goal
$OPT(n) =$ the minimized $cost$ of arranging $n$ sculptures into rows. 

### Computing $OPT(j)$
Let $C_{ij}$, where $1 \leq i \leq j$, represent the cost of a row consisting of all sculptures between and including sculptures $s_i$ and $s_j$. We allow $i$ and $j$ to be equivalent because it is possible that a row may have only one sculpture in an optimum solution. $C_{ij}$ is represented by: 
$$
C_{ij} = 
\begin{cases}
    \infty & \text{if } \sum_{k=i}^{j} w_k > W \\
    \max_{i \leq k \leq j}(h_k) & \text{otherwise}
\end{cases}
$$

To compute $OPT(j)$, we take the minimum sum over $i$ for $1 \leq i \leq j$ of $C_{ij}$ and $OPT(i-1)$. In this case, $i-1$ represents the *last* sculpture in the row preceding sculpture $s_i$. The following Bellman Equation describes $OPT(j)$:
$$
OPT(j) =
\begin{cases}
    0 & \text{if } j < 1 \\
    \min_{1 \leq i \leq j}(C_{ij} + OPT(i-1)) & \text{otherwise} \\
\end{cases}
$$

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


<!-- need to explain backtracking...-->

## Analysis
### Time Complexity
#### 5A: Top-Down
Algorithm 5A precomputes all values of $C_{ij}$, taking $\Theta(n^2)$ time to do so, as all $n$ sculptures are checked no fewer and no more than $n$ times each. Afterward, all $n$ values of the OPT-array $M$ require $n$ comparisons against the rest of the sculpture list to determine the minimum possible value. This takes $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

#### 5B: Bottom-Up
Algorithm 5B, just like 5A, precomputes all $C_{ij}$ values in $\Theta(n^2)$ time. The difference is now that we iterate from $1$ to $n$, making $n$ comparisons at each step, traking $O(n^2)$ time. Our total is now $O(n^2 + n^2) = O(2n^2) = \Theta(n^2)$.

### Correctness
We begin by establishing the following assumption: 
$$
\forall 1 \leq k \leq n, \nexists s_k \text{ where } w_k > W.
$$

We will now examine the construction of $C_{ij}$ values. These values represent, at index $C[i][j]$, the cost of a row containing sculptures $[s_i, \cdots, s_j]$ for $1 \leq i \leq j$, calculated as the height of the tallest sculpture on the platform. Thus, any value of $C_{ij}$ can be used to determine the relative *worth* of row $[s_i, \cdots, s_j]$. These values are used to determine the best combination of rows, since rows that cannot exist are marked as $C_{ij} = \infty$ and will therefore never be chosen over a smaller value. We now establish the following invariant:

__$\text{I1}$: at the end of each iteration of the inner loop of $C_{ij}$ computation, $C[i][j]$ correctly stores the maximum height of a row containing sculptures $s_i$ to $s_j$, as long as the combined widths of the sculptures do not exceed $W$.__

From our initial assumption, we also establish the second invariant:

__$\text{I2}$: There always exists an arrangement of $n$ sculptures $s_1, \cdots, s_n$ into rows, as every sculpture is permitted to sit on its own row, whose cost will be $C[k][k] = h_k, \forall 1 \leq k \leq n$.__ 

### 5A: Top-Down
Following the computation of all $C_{ij}$, $\text{TD-OPT}(n)$ is called. This is a recursive, top-down formulation of the generic form of Algorithm 5. We will use induction to prove the correctness of Algorithm 5A. 

*Proof:* For $\text{TD-OPT}(j)$ where $j=1$, the case is simple. A set of one sculpture has only itself to be placed in a row, so the minimum height of the row is $M[1]=C[1][1]+0=h_1$, that of the singular sculpture, upholding $\text{I2}$.

Moving forward, if for $\text{TD-OPT}(j), M[j] = \varnothing$, then it is set equal to the value of the minimum cost over $i$ for $C_{ij} + \text{TD-OPT}(i-1)$. This step will recursively calculate and store the minimum possible cost of a row being created whose rightmost sculpture is $s_j$, and calculate the cost of the next row that begins at $s_{i-1}$. The value of $M[j]$ is minimized at every recursive step, whose solution is calculated upon the existence of optimal solutions to previous subproblems. By using the optimal substructure property of Problem G, Algorithm 5A properly constructs a correct solution, outputting the minimized cost of a set of sculptures by finding the minimum cost of a row, over all possible rows. This completes our proof, and shows that Algorithm 5A correctly computes and stores the minimum-cost arrangement of sculptures in every recursive call from $\text{TD-OPT}(j)$ to $\text{TD-OPT}(1)$.

### 5B: Bottom-Up
Following the computation of all $C_{ij}$, optimal solutions to subproblems of $\text{Bottom-Up-OPT}(n)$ are tabulated, beginning at $1$ and working up to $n$. Given $\text{I1}$, we establish that 5B employs an effective strategy to determine the minimum optimized cost of a row, by building upward. At each step, every possible option over $i$ is considered, from $1 \leq i \leq j \leq n$, and $i$ values for which $\sum_{k=i}^{j} w_k > W$ will never be chosen if any other option exists in accordance with $\text{I1}$. Since $i \leq j$, the possibility of sculpture $s_j$ sitting alone in a row is also considered, which is always a possibility and always preferred to $\infty$, as per $\text{I2}$. We now establish the third invariant:

__$\text{I3}$: at the end of each iteration from $k=1$ to $n$, $M[k]$ correctly stores the minimum combined cost of all valid arrangements of k sculptures.__

Using $\text{I2}$ and $\text{I3}$, we claim that Algorithm 5B correctly tabulates the cost iteratively by considering the cost of all rows ending at $s_j$ as it approaches $s_n$. We will prove this claim via induction. 

*Proof:* Beginning with the case $k=1$, a set of sculptures containing only $s_1$ has only one arrangement where $s_1$ is by itself. Since $1 \leq i \leq k$, it must be the case that $i=k=1$, so $M[1]=C[1][1] + 0 = h_1$, and $\text{I3}$ is maintained. 

For all cases $k>1$, solutions to subproblems are computed using previous subproblem solutions, maintaining $\text{I3}$ by choosing the minimum possible $C_{ik}$ and the solution at $M[i-1]$, which we have already computed. This completes our proof, and shows that Algorithm 5B computes and stores the minimum-cost arrangement of sculptures in every iteration from $k=1$ to $n$.