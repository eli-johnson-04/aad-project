### Elijah Johnson, Patrick Kallenbach, Nicholas Lindner
# Algorithm and Analysis 2

## Problem S2
### Given the heights $h_1, \cdots, h_n$, where $\exists k$ such that $\forall i < j \leq k, h_i \geq h_j$, and $\forall k \leq i < j, h_i \leq h_j$, and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.
#### (Note: The heights of the paintings follow a unimodal function with a single local minimum, as in EXAMPLE 3.) 

### Example 3
$n = 7, W = 10$\
$h_i = [12, 10, 9, 7, 8, 10, 11]$\
$w_i = [3, 2, 3, 4, 3, 2, 3]$

### Solution 3
$Platform_1 = [s_1 \cdots s_3];$\
$Platform_2 = [s_4];$\
$Platform_3 = [s_5 \cdots s_7];$\
$cost = 12 + 7 + 11 = 30$

## Algorithm 2
- Let $W$ represent max row width. 
- Let $cost$ represent the total height of the platforms, initialized to $cost = 0$.
- Let $w(r_j)$ represent the width of the current row, initialized to $w(r) = 0$. 
- Maintain the height of the previous painting, $prevH$, initialized to $h_0$ (painting $p_0$). 
- Keep track of the paintings in the current row, and of the total number of rows. 

In the list of paintings, Repeat the following for each painting $p_i$:
- If $w(r_j) + w(p_i) \leq W$:
    - If $!minimumFound$:
        - If $(h_i \leq prevH) \lor (h_i == h_{i+1})$:
            - Add $p_i$ to $r_j$ and update $w(r_j)$. Set $prevH = h_i$.
        - Otherwise if $p_i$ is not the last painting, and $h_i < h_{i+1}$:
            - Set $minimumFound = T$. Add $p_i$ to $r_j$ and update $w(r_j)$. Set $prevH = h_i$.
    - Otherwise if $minimumFound$:
        - If $(h_i \geq prevH) \lor (h_i == h_{i+1})$, and $p_i$ is not the last painting:
            - Add $p_i$ to $r_j$ and update $w(r_j)$. Set $prevH = h_i$.
    - Proceed to the next painting. 
- Otherwise if $r_j$ is full or there are no paintings left:
    - If $minimumFound$:
        - Add the *last* painting in $r_j$ to $cost$. 
    - Otherwise:
        - Add the *first* painting in $r_j$ to $cost$.
    - Record $r_j$'s length and continue.

Return the number of rows, the total $cost$, and the list containing each platform's lengths. 

## Analysis 2
### Time Complexity
Algorithm 2 has a time complexity of $O(n)$. Algorithm 2 proceeds through the list of paintings only one time, performing a few $O(1)$ checks and operations on each painting. However, each painting must be checked and will be checked only once, terminating when the last painting in the list is reached, so the total running time is $O(n)$.

### Correctness
Consider the sequence $P$ of $n$ paintings with heights $h_i = [h_1, h_2, \cdots, h_n]$ and widths $w_i = [w_1, w_2, \cdots, w_n]$, where $\exists k$ such that $\forall i < j \leq k, h_i \geq h_j$, and $\forall k \leq i < j, h_i \leq h_j$. The heights of the paintings follow a unimodal function with a single local minimum, where the goal is to find an arrangement of the paintings on platforms that minimizes the total height. The total height is equal to the sum of the heights of the tallest painting in every platform. 

We will prove that the above greedy algorithm is correct and satisfies the following conditions:
1. The combined widths of a row $w(r_j) \leq W$.
2. For $r$ rows, the total cost $\sum_{0}^{j=r} h_j$, where $h_j$ is the first and tallest painting in a row, is minimized.

In this problem, the heights of the paintings are not strictly decreasing. This means that the sequence $P$ has a unimodal nature, where the paintings' heights decrease to a single local minimum, then increase again. As such, the first painting in a row may not always have the largest height, so it is important that paintings are placed strategically upon their rows to capitalize on the pattern.  

The maximum width constraint is guaranteed to be respected in the above algorithm because for each iteration, there is a check to make sure that for the $i$'th painting, $w_i$ plus the current width of the current row $w(r_j)$ is less than or equal to the maximum allowed width $W$. If so, then the painting can be added to the row. Otherwise, a new row must be started, and $p_i$ is added to it. Doing so ensures that $w(r_j) \leq W$.

Pf:
In order to minimize the total cost $\sum_{j=1}^{r} h_j$, our algorithm maximizes the number of paintings in each row of the platform. Before the local minimum height $i \leq k$, the paintings' heights must be strictly decreasing due to unimodality, so adding more paintings to the current row will never increase the row's height. After the local minimum height is found $i \geq k$, the heights of the paintings must be strictly increasing, meaning that only the last painting in the row has an effect on the row's height. Therefore, the algorithm provides a platform that is optimally arranged, minimizing the total cost of the platform.

The paintings are processed in two phases: handling the top rows before the local minimum, and handling the bottom rows after the local minimum is found. While the decreasing phase runs, the top rows are filled by adding the current painting to the row as long as the row's width is less than the maximum allowed width. This guarantees that top rows are as full as possible, minimizing cost since all taller paintings will be placed before shorter ones. If a new row must be created, height minimization still occurs since the new row will begin with the shortest painting processed up until that point in the algorithm.

When a local minimum is found, the algorithm begins to process the bottom rows from right to left, adding paintings to the current row so that the paintings are increasing in size as they move from right to left, until the current painting cannot fit onto the row. Then, a new bottom row begins, starting with the next avaialbe painting. This minimizes the height of each new row in the increasing sequence.

Finally, if the last row of the top rows and the first row of the bottom rows can be combined without exceeding W, they are merged to further reduce the number of rows. This ensures that the overall height is minimized by reducing the number of row transitions. By using this greedy strategy to maximize the number of paintings per row while managing the transitions between decreasing and increasing phases, the algorithm minimizes the total number of rows and the total height, achieving an optimal solution.
