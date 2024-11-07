# Algorithm and Analysis 3

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 3: Naive Solution
### Definition
$OPT(j) =$ The minimized $cost$ of arranging $j$ sculptures into rows, where $j$ is the *rightmost* sculpture being examined. In this formulation, $cost = \sum_{1}^{j}(\max_{h_k}r_j)$, and $h_k$ is the height of a sculpture $s_k \in r_j$. 

### Goal
$OPT(n) =$ the minimized cost of arranging $n$ sculptures into rows.

### Computing $OPT(j)$
Let $C_{ij}$, where $1 \leq i < j$ represent the cost of a row consisting of all sculptures between and including distinct sculptures $s_i$ and $s_j$. $C_{ij}$ is represented by:
$$
C_{ij} = 
\begin{cases}
    \infty & \text{if } \sum_{k=i}^{j} w_k > W \\
    \max_{i \leq k \leq j}(h_k) & \text{otherwise}
\end{cases}
$$

To compute $OPT(j)$, we take the minimum sum of $C_{ij}$ and $OPT(i-1)$, where $OPT(i-1)$ represents the *last* sculpture in the row preceding sculpture $s_i$. The following Bellman Equation describes $OPT(j)$:
$$
OPT(j) = 
\begin{cases}
    0 & \text{if } j < 1 \\
    \min_{1 \leq i < j}(C_{ij} + OPT(i-1)) & \text{otherwise} \\
\end{cases}
$$

## Analysis
### Time Complexity


### Correctness
<!-- Write Correctness Analysis Here!!!!-->