# Algorithm and Analysis 1

## Problem S1 
### Given the heights $h_1, \cdots, h_n$, where $h_i \geq h_j, \forall i < j$, and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.
#### (Note: The heights of the paintings form a monotonically non-increasing sequence, as in EXAMPLE 1.)

### Example 1
$n = 7, W = 10$\
$h_i = [21, 19, 17, 16, 11, 5, 1]$\
$w_i = [7, 1, 2, 3, 5, 8, 1]$

### Solution 1
$Platform_1 = [s_1 \cdots s_3];$\
$Platform_2 = [s_4 \cdots s_5];$\
$Platform_3 = [s_6 \cdots s_7];$\
$cost = 21 + 16 + 5 = 42$

## Algorithm 1: Greedy Solution
Track $W$ and $cost$ (initialized to $0$). Begin a new row with weight $w(r) = 0$. In the list of paintings, repeat the following for each painting $i$: 
- If $w(r) + w(i) \leq W$:
    - Add painting $p_i$ to row $r$.
    - If $p_i$ is the first painting in the row:
        - Add $h_i$ to $cost$. 
    - Delete painting $p_i$ from the list.
- Otherwise:
    - Begin a new row.

## Correctness Analysis 1
Consider the sequence $P$ of $n$ paintings, whose heights $h_i = [h_1, h_2, \cdots, h_n]$ are monotonically non-increasing. We will prove that the above greedy algorithm is correct and satisfies the following conditions:
- The combined weights of a row $w(r_j) \leq W$.
- For $r$ rows, the total cost $\sum_{0}^{j=r} h_j$, where $h_j$ is the first and tallest painting in a row, is minimized.

Due to the nature of a sequence $P$ of $n$ paintings, whose heights are monotonically non-increasing, this problem focuses more precisely on minimizing the number of rows, or maximizing the number of paintings per row, while preserving the original order. This is because the order of the paintings cannot be such that for two paintings $p_i$ and $p_j$, where $\forall ij, i < j, h_i < h_j$. So, a random selection of paintings placed into rows that preserve the original order of the paintings would create an arrangement such that the first painting in any row is at least the talles. The goal is that the number of rows must be minimized, or the number of paintings per row must be maximized, to minimize the total cost. 

*Pf:* If paintings are selected in such a way that they maximize the number of paintings per row, then the height of the tallest painting in each row will be minimized. If there exists space in a row for a painting $p_i$, meaning $w(r) + w_i \leq W$, then placing it in the row will minimize the cost of the next row, since $h_{i-1} \geq h_i$. If $p_i$ must be placed in a new row, then it will be the shortest possible painting that can be placed there. Therefore, since the greedy algorithm chooses at least the tallest painting that fits in a row, it will maximize the number of paintings per row, minimize the total number of rows, and therefore minimize the total cost. The shortest possible painting will be chosen to be placed first in each row. 

## Question 1
### Give an input example showing that Algorithm 1 does not always solve Problem G. 

### Problem G (Generic Problem)
Given the heights $h_1, \cdots, h_n$ and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height. 

### Solution:
Consider the sequence $P$ of $n$ paintings, with heights $h_i = [2, 3, 1, 4, 3]$ and widths $w_i = [1, 1, 1, 1, 1]$, with $W = 2$. Algorithm 1 chooses as many paintings as can fit in a row while maintaining their original order. So, in this example, Algorithm 1 selects the following:
- $Platform_1 = [2, 3];$
- $Platform_2 = [1, 4];$
- $Platform_3 = [3];$
- $cost = 3 + 4 + 3 = 10$

The ordering of the paintings' heights results in the minimum cost being found by Algorithm 1 as 6, since the cost of each row is decided by the first painting's height ($2 + 1 + 3$). However, the true total height of the display would be 10, the maximum height of each row.

The optimal solution for this setup actually has a height of 8. This arrangement maintains the original order of the paintings, but two of the rows are now shorter. 
- $Platform_1 = [2, 3];$
- $Platform_2 = [1];$
- $Platform_3 = [4, 3];$
- $cost = 3 + 1 + 4 = 8$

Hence, Algorithm 1 does not always produce a minimum-cost solution for Problem G. 

Consider the sequence $P'$, a permutation of $P$ with paintings in decreasing order of height: $h_i = [4, 3, 3, 2, 1]$ and $w_i = [1, 1, 1, 1, 1]$. Then the solution produced by Algorithm 1 is the following:
- $Platform_1 = [4, 3];$
- $Platform_2 = [3, 2];$
- $Platform_3 = [1];$
- $cost = 4 + 3 + 1 = 8$

Because this permutation adheres to the required monotonically non-decreasing ordering of paintings for Algorithm 1, it produces the arrangement of rows with minimum height.

## Question 2 
### Give an input example showing that Algorithm 1 does not always solve Problem S2.

### Problem S2
Given the heights $h_1, \cdots, h_n$, where $\exists k$ such that $\forall i < j \leq k, h_i \geq h_j$, and $\forall k \leq i < j, h_i \leq h_j$, and the base widths $w_1, \cdots, w_n$ of $n$ paintings, along with the width $W$ of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.

### Solution: 
Consider a Problem S2 instance where $h_i = [4, 2, 1, 2, 4]$, and $w_i = [1, 1, 1, 1, 1]$, with $W = 2$. Algorithm 1's output is as follows: 
- $Platform_1 = [4, 2];$
- $Platform_2 = [1, 2];$
- $Platform_3 = [4];$
- $cost = 4 + 2 + 4 = 10$

An optimum output would resemble the following:
- $Platform_1 = [4, 2];$
- $Platform_2 = [1];$
- $Platform_3 = [2, 4];$
- $cost = 4 + 1 + 4 = 9$

This is an optimum solution maintaining original order, as the minimum cost is $9$, the lowest possible cost for the given ordering of the paintings. This demonstrates that Algorithm 1 does not always produce a minimum-cost solution for instances of Problem S2. 