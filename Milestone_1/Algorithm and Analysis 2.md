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

## Algorithm 2: Greedy Split Solution
- Let $W$ represent max row width. 
- Let $w_i$ represent the width of painting $p_i$.
- Let $w(r_j)$ represent the width of a row, where each $r_j$ is initialized with $w(r_j) = 0$. 
- Let $cost$ represent the total height of the platforms, initialized to $cost = 0$.
- Let $h_i$ represent the height of a painting $p_i$.
- Let $h(r_j)$ represent the height of a row.
- Keep track of the paintings in the current row $r_j$.
- Keep track of "top rows" $T$ and "bottom rows" $B$, both initialized as empty sets.

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
Algorithm 2 has a time complexity of $\theta(n)$. Algorithm 2 proceeds through the list of paintings only one time, performing some $O(1)$ conditionals and $O(1)$ additions to auxiliary arrays. When the minimum height painting is found, it then proceeds from the other end toward the $minIndex$. Each painting must be checked and will be processed only once, terminating only when all paintings have been checked. At the end, two rows may be merged. If this is the case, it may take a maximum of $n$ accesses to merge the rows into one, and then a $O(1)$ operation to get the minimum between their heights, but this still results in a $\theta(n)$ total complexity, as every painting must be checked, but none will be checked more than twice. 

### Correctness
Consider the sequence $P$ of $n$ paintings, whose heights $h_i = [h_1, h_2, \cdots, h_n]$ follow a unimodal function with a single local minimum. We will prove that the above greedy algorithm is correct and satisfies the following conditions:
- The order of the paintings is not changed. 
- The combined widths of a row $w(r_j) \leq W$.
- For $r$ rows, the total cost $\sum_{0}^{j=r} h_j$, where $h_j$ is the tallest painting in a row, is minimized.

An instance of Problem S2 can be understood as two Problem S1 instances, where the latter is reversed in order, and there exists one $p_i$ whose height is the least of all paintings. 

Algorithm 2 is constructed in a manner resembling that of two runs of Algorithm 1 with the latter in reverse order. The former proceeds until a minimum index is found, and the latter proceeds backward from the end until the minimum index is reached. 

Using correctness of Algorithm 1, we can say that Algorithm 2 is also correct. 

*Proof*: Let $R$ represent the set of paintings from $p_0$ to $p_m$ inclusive, where $\exists m$ such that $\forall i < j \leq m, h_i \geq h_j$, and $\forall m \leq i < j, h_i \leq h_j$. In this case, $m$ represents the index of the minimum-height painting in $P$. $R$, then, has heights ordered in a monotonically non-increasing fashion, which can be understood as an instance of Problem S1. Let the remaining paintings $S$ represent the reverse of another instance of Problem S1, since all paintings *after* $R$ are monotonically non-decreasing. Therefore, an instance of Problem S2 can be treated as an instance of Problem S1 directly followed by another reversed instance. 

Algorithm 2 follows the same logic as Algorithm 1, whose correctness we have already proved, but is designed to handle the now deconstructed Problem S2 structure. For the set of paintings $R$, A2 follows the same steps as A1, just performing an extra check to determine if, for painting $p_i$, whether $h_{i+1} > h_i$. If this is the case, the minimum value has been found, and its index is stored as $minIndex$. Along the way, paintings are added to the *ends* of rows of *decreasing* order in a set of rows $T$.

From there, A2 proceeds in a backwards fashion from the end of the list to $minIndex$, following the same steps as A1, only now in reverse order from the end of the list. In this case, paintings are added to the *beginnings* of rows of *increasing* order in a set of rows $B$. *(NOTE: A2 does not check* $p_{minIndex}$ *twice.)*

However, A2 is not finished after all paintings have been checked. The last row of $T$ and the first row of $B$ are of unknown widths, each with their own tallest paintings, and can be combined to minimize $cost$. A2 checks that their combined widths $w(T_{end}) + w(B_{start})$ are less than or equal to $W$, and merges them if so. It then subtracts the minimum of $T_{end}$'s and $B_{start}$'s tallest paintings from the total cost, meaning only the height of the tallest painting in the new combined row is accounted for. If their combined widths exceed $W$, no further action is taken. 

We have shown that $R$ is assessed by $T$ in A2, and $S$ is assessed by $B$, and their (potential) overlap is addressed accordingly. Therefore, Algorithm 2 produces a correct output for an instance of Problem S2, satisfying the aforementioned conditions. 