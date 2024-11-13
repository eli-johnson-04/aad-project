# Algorithm and Analysis 4

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 4: Inefficient Dynamic Programming Solution
### Definition
This algorithm closely follows Algorithm 3. Algorithm 4 uses a dynamic programming approach to solve Problem G. It iteratively determines the optimal arrangement of sculptures on platforms to minimize the total height. However, this solution employs an approach that recomputes the maximum height in each partition from scratch, leading to an inefficient, Θ(n³) algorithm.

Let $OPT(j)$ denote the minimized cost of arranging the first $j$ paintings into rows, where $j$ is the rightmost painting in the arrangement.

OPT(j) = minimum total height required to arrange paintings up to j.

The sum of the maximum heights of all rows is calculated as "Total Cost":
$$
\text{cost} = \sum_{r=1}^{m} \left( \max_{h_k} \text{ in } r_j \right)
$$
Here, $h_k$ is the height of painting $p_k$ in row $r_j$.

### Goal
The goal of the algorithm is to compute:
$$
OPT(n) = \text{the minimized total height for arranging all } n \text{ paintings into rows, subject to the width constraint } W.
$$

## Analysis
### Time Complexity
<!-- Write Time Complexity Analysis Here!!!!-->

### Correctness
<!-- Write Correctness Analysis Here!!!!-->

### Code

# Algorithm and Analysis 4

## Problem G
### Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ sculptures, along with the width $W$ of the display platform, find an arrangement of the sculptures on platforms that minimizes the total height. 

## Algorithm 4: Dynamic Programming Solution
<!-- Write Algorithm Details Here!!!!-->

## Analysis
### Time Complexity
<!-- Write Time Complexity Analysis Here!!!!-->

### Correctness
<!-- Write Correctness Analysis Here!!!!-->


