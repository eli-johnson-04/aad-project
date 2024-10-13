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
- Let $h(r_j)$ represent the height of the desired row
- Keep track of the paintings in the current row $r_j$
- Keep track of "top rows" $T$ and "botom rows" $B$, both initialized to $\empty$

In the list of paintings, Repeat the following for each painting $p_i$ until $minimumFound$ is $true$:
- If $w(r_j) + w(p_i) \leq W$:
    - Add $p_i$ to end of $r_j$
    - Add $w(p_i)$ to $w(r_j)$
    - If $p_i$ is the first of $r_j$, add its height to $cost$
- Otherwise:
    - Add $r_j$ to the end of $T$
    - Test $p_i$ again on the next iteration
- If the height of $p_{i+1} >$ the height of $p_i$
    - Add $r_j$ to the end of $T$
    - Store the current index $i$ as $minIndex$
    - Set $minimumFound$ to $true$
- Proceed to the next painting. 

For each of the remaining paintings, repeat for each painting $p_i$ starting from the end and working inward:
- If $w(r_j) + w(p_i) \leq W$:
    - Add $p_i$ to beginning of $r_j$
    - Add $w(p_i)$ to $w(r_j)$
    - If $p_i$ is the first added to $r_j$, add its height to $cost$
- Otherwise:
    - Add $r_j$ to the beginning of $B$
    - Test $p_i$ again on the next iteration
Upon completion, add what remains of $r_j$ to the beginning of $B$

If $w(T_{end}) + w(B_{start}) \leq W$
- Merge $T$ and $B$, combining $T_{end}$ and $B_{start}$ into one element
- Subtract $min(h(T_{end}), h(B_{start}))$ from $cost$

Otherwise:
- Merge $T$ and $B$, leaving $T_{end}$ and $B_{start}$ as separate elements

Return the number of rows, the total $cost$, and the list containing each platform's lengths. 

## Time Complexity Analysis 2
Algorithm 2 has a time coplexity of O(n). This is because algorithm 2 completes only one pass through the list of paintings, meaning that if the list contains n items, the algorithm will execute n operations. So as the input size increases, the time required to process the list grows proportionally. This means that the growth is linear.

## Correctness Analysis 2
[insert analysis here]
