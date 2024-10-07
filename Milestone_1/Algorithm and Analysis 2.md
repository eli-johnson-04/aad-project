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
Track $W$ and $cost$ (initialized to $0$) and begin iterating for a new row with $w(r) = 0$. Keep a counter for each row, tracking the number of paintings in that row, intialized to $0$ for each new row. In the list of paintings, Repeat the following for each painting $p_i$:
- Maintain the height of the previous painting, $prevH$, initialized to $h_0$ (painting $p_0$). 
    - If $w(r) + w_i \leq W$:
        - If $p_i$ is the first painting in the row:
            - Add $h_i$ to $cost$. 
        - If $!minimumFound$:
            - If $(h_i \leq prevH) \lor (h_i == h_{i+1})$:
                - Add $p_i$ to row. Increment the counter for that row. Set $prevH = h_i$.
            - Otherwise if $h_i < h_{i+1}$:
                - Mark $minimumFound$ as true. Store the counter, place $p_i$ in a new row, then reset counter to $1$. Set $prevH = h_i$.
        - Otherwise if $minimumFound$:
            - If $(h_i > prevH) \lor (h_i == h_{i+1})$:
                - Add $p_i$ to row. Increment the counter for that row. Set $prevH = h_i$.
        - Delete painting $p_i$ from the list.
    - Otherwise:
        - Store the counter for the current row, then reset it to $0$. Begin a new row. Set $prevH = h_i$.

## Analysis 2
[insert analysis here]