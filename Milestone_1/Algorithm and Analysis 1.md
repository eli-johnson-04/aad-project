# Algorithm and Analysis 1
## Problem S1 
Given the heights *h~1~, ..., h~n~*, where *h~i~ $\ge$ h~j~* for all *i $\lt$ j*, and the base widths *w~1~, ..., w~n~* of *n* paintings, along with the width *W* of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.\
*(Note: The heights of the paintings form a monotonically non-increasing sequence, as in EXAMPLE 1.)*

### Example 1
*n* = 7, *W* = 10\
*h~i~* = [21, 19, 17, 16, 11, 5, 1]\
*w~i~* = [7, 1, 2, 3, 5, 8, 1]

### Solution 1
*Platform~1~* = [*s~1~...s~3~*]\
*Platform~2~* = [*s~4~...s~5~*]\
*Platform~3~* = [*s~6~...s~7~*]\
*cost* = 21 + 16 + 5 = 42

## Algorithm 1
Track *W* and *cost* (initialized to 0). Begin a new row with *w(r)* = 0. Keep a counter for each row, tracking the number of paintings in that row, intialized to 0 for each new row. Repeat the following for each painting *i*: 
- If *w(r)* + *w(i)* $\le$ *W*:
    - Add painting *i* to row *r*. Increment the counter for row *r*.
    - If *i* is the first painting in the row:
        - Add *h(i)* to *cost*. 
    - Delete painting *i*.
- Otherwise:
    - Store the number of paintings for the row, then reset the counter to 0. Begin a new row.

## Analysis 1
[insert analysis here]
