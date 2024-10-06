# Algorithm and Analysis 1

## Problem S1 
Given the heights $h_1, \cdots, h_n$, where $h_i \geq h_j, \forall i < j$, and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.\
(Note: The heights of the paintings form a monotonically non-increasing sequence, as in EXAMPLE 1.)

### Example 1
$n = 7, W = 10$\
$h_i = [21, 19, 17, 16, 11, 5, 1]$\
$w_i = [7, 1, 2, 3, 5, 8, 1]$

### Solution 1
$Platform_1 = [s_1 \cdots s_3];$\
$Platform_2 = [s_4 \cdots s_5];$\
$Platform_3 = [s_6 \cdots s_7];$\
$cost = 21 + 16 + 5 = 42$

## Algorithm 1
Track $W$ and $cost$ (initialized to $0$). Begin a new row with $w(r) = 0$. Keep a counter for each row, tracking the number of paintings in that row, intialized to $0$ for each new row. Repeat the following for each painting $i$: 
- If $w(r) + w(i) \leq W$:
    - Add painting $i$ to row $r$. Increment the counter for row $r$.
    - If $i$ is the first painting in the row:
        - Add $h(i)$ to $cost$. 
    - Delete painting $i$.
- Otherwise:
    - Store the number of paintings for the row, then reset the counter to $0$. Begin a new row.

## Analysis 1
[insert analysis here]

## Question 1
Give an input example showing that Algorithm 1 does not always solve Problem G. 

#### Problem G (Generic Problem)
Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height. 

## Question 2 
Give an input example showing that Algorithm 1 does not always solve Problem S2.

#### Problem S2
Given the heights $h_1, \cdots, h_n$, where $\exists k$ such that $\forall i < j \leq k, h_i \geq h_j$, and $\forall k \leq i < j, h_i \leq h_j$, and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.