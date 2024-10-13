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
- Let $w_i$ represent the width of painting $p_i$.
- Let $w(r_j)$ represent the width of a row, where each $r_j$ is initialized with $w(r_j) = 0$. 
- Let $cost$ represent the total height of the platforms, initialized to $cost = 0$.
- Let $h_i$ represent the height of a painting $p_i$.
- Let $h(r_j)$ represent the height of a row.
- Keep track of the paintings in the current row $r_j$.
- Keep track of "top rows" $T$ and "bottom rows" $B$, both initialized to $\empty$.

Beginning with $j, i = 0$, repeat the following for each painting $p_i$ until $minimumFound$ is $true$: 
- If $w(r_j) + w_i \leq W$:
    - Append $p_i$ to the *end* of $r_j$.
    - Update the current row's width by adding $w_i$ to $w(r_j)$.
    - If $p_i$ is the first painting in $r_j$, add $h_i$ to $cost$.
- Otherwise if the row $r_j$ is full:
    - Append $r_j$ to the *end* of $T$.
    - Continue; return to the beginning of $p_i$'s iteration. 
- If the $h_{i+1} > h_i$:
    - Append $r_j$ to the end of $T$.
    - Store the current index $i$ as $minIndex$.
    - Set $minimumFound$ to $true$.
- Proceed to the next painting. 

Now that $minimumFound$ is $true$, repeat the following for the remaining paintings, starting from $p_n$ and working inward to, but not including, $p_{minIndex}$: 
- If $w(r_j) + w_i \leq W$:
    - Append $p_i$ to the *beginning* of $r_j$.
    - Add $w_i$ to $w(r_j)$.
    - If $p_i$ is the first painting added to $r_j$, add $h_i$ to $cost$.
- Otherwise if there are no more paintings or if $r_j$ is full:
    - Append $r_j$ to the *beginning* of $B$.
    - Continue; return to the beginning of $p_i$'s iteration. 

When no paintings are left, add what remains of $r_j$ to the *beginning* of $B$. Then:

If $w(T_{end}) + w(B_{start}) \leq W$:
- Merge $T$ and $B$, combining $T_{end}$ and $B_{start}$ into one row. 
- Subtract $min(h(T_{end}), h(B_{start}))$ from $cost$.

Otherwise:
- Merge $T$ and $B$, leaving $T_{end}$ and $B_{start}$ as separate rows.

Return the number of rows, the total $cost$, and the list containing each platform's lengths. 

## Analysis
### Time Complexity
Algorithm 2 has a time complexity of $O(n)$. Algorithm 2 proceeds through the list of paintings only one time, performing some $O(1)$ conditionals and $O(1)$ additions to auxiliary arrays. When the minimum height painting is found, it then proceeds from the other end toward the $minIndex$. However, each painting must be checked and will be processed only once, terminating only when all paintings have been checked, so the total running time is $O(n)$.

### Correctness
[insert analysis here]
