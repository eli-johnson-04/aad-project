### Definition
$OPT(i, M) =$ The minimized $cost$ of arranging $i$ paintings into rows of width no greater than $M$, where $cost = \sum_{0}^{j}\max_{h_k}r_j$, where $h_k$ is the height of a painting $p_k \in r_j$. A row $r_j$ is initialized to the empty set. 

#### Goal
$OPT(n, W) =$ the minimum cost of arranging $n$ paintings into rows of width no greater than $W$. 

#### Cases
- Case 1: $OPT(i, M)$ adds painting $p_i$ to the beginning of an existing row $r_j$. 
    - $OPT(i, M) = OPT(i-1, M-w_i)$. 
- Case 2: $OPT(i, M)$ adds painting $p_i$ to the beginning of a new row $r_{j+1}$. 
    - $OPT(i, M) = \max_{h_k}r_{j} + OPT(i-1, M-w_i)$.

#### Bellman Equation
$OPT(i, M) = 
\begin{cases}
    0 & \text{if } i=0 \\
    OPT(i-1, M-w_i) & \text{if } w_i \leq M \\
    \max_{h_k}r_{j} + OPT(i-1, M-w_i) & \text{if } w_i > M
 \end{cases}$

 ### Implementation
 Follow the above algorithm as described. The row index $j$ is tracked separately from execution, and addition of paintings to rows is implied, where $j$ is incremented in Case 2.

 - Let $front$ represent the first index in a row $r[j]$, where an assignment of $r[j][front]$ represents *appending* the element in question to the beginning of $r[j]$.

 $\text{OPT-Compute(n, W)} \\
 \quad j \leftarrow 0 \\
 \quad r[j] \leftarrow null, r[j][front] \leftarrow null \\
 \quad \text{For }i=n \text{ to } 1 \text{:} \\
 \qquad 
 $