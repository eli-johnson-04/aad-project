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

## Correctness Analysis 2
[insert analysis here]