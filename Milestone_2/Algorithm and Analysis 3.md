# Algorithm and Analysis 3

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height. 

## Algorithm 3: Naive Solution
### Definition
$OPT(i, M) =$ The minimized $cost$ of arranging $i$ paintings into rows of width no greater than $M$, where $cost = \sum_{0}^{j}\max_{h_k}r_j$, where $h_k$ is the height of a painting $p_k \in r_j$. A row $r_j$ is initialized to the empty set. 

#### Goal
$OPT(n, W) =$ the minimum cost of arranging $n$ paintings into rows of width no greater than $W$. 

#### Cases
- Case 1: $OPT(i, M)$ adds painting $p_i$ to the beginning of an existing row $r_j$. 
    - $OPT(i, M) = OPT(i-1, M-w_i)$. 
- Case 2: $OPT(i, M)$ adds painting $p_i$ to the beginning of a new row $r_{j+1}$. 
    - $OPT(i, M) = \max_{h_k}r_j + OPT(i-1, M-w_i)$, where $\max_{h_k}{r_j}$ is calculated using a linear search. 

#### Bellman Equation
$OPT(i, M) = 
\begin{cases}
    0 & \text{if } i=0 \\
    OPT(i-1, M-w_i) & \text{if } w_i \leq M \\
    \max_{h_k}r_{j} + OPT(i-1, M-w_i) & \text{if } w_i > M
\end{cases}$

### Implementation
$\text{Minimum-Cost}(n, W, p_1, \cdots, p_n, w_1, \cdots, w_n, h_1, \cdots, h_n): \\
\quad j = 0 \\
\quad \text{return OPT-Compute}(n, W) \\
\quad \\
\text{OPT-Compute}(i, M): \\
\quad \text{if } i=0: \\
\qquad \text{return }0 \\
\quad \text{else if } w_i \leq M: \\
\qquad \text{return OPT-Compute}(i-1, M-w_i) \\
\quad \text{else if } w_i > M: \\
\qquad h_{r_j} \leftarrow \max_{h_k}r_j \\ 
\qquad j \leftarrow j + 1 \\
\qquad \text{return } h_{r_{j-1}} + OPT(i-1,M-w_i)
$

## Analysis
### Time Complexity


### Correctness
<!-- Write Correctness Analysis Here!!!!-->