# Algorithm and Analysis 2

## Problem S2
Given the heights *h~1~, ..., h~n~*, where there exists a *k* such that for all *i $\lt$ j $\le$ k*, *h~i~ $\ge$ h~j~*, and for all *k $\le$ i $\lt$ j*, *h~i~ $\le$ h~j~*, and the base widths *w~1~, ..., w~n~* of *n* paintings, along with the width *W* of the display platform, find an arrangement of the paintings on platforms that minimizes the total height.\
*(Note: The heights of the paintings follow a unimodal function with a single local minimum, as in EXAMPLE 3.)* 

### Example 3
*n* = 7, *W* = 10\
*h~i~* = [12, 10, 9, 7, 8, 10, 11]\
*w~i~* = [3, 2, 3, 4, 3, 2, 3]

### Solution 3
*Platform~1~* = [*s~1~...s~3~*]\
*Platform~2~* = [*s~4~*]\
*Platform~3~* = [*s~5~...s~7~*]\
*cost* = 12 + 7 + 11 = 30

## Algorithm 2
Track *W* and *cost* (initialized to 0) and begin iterating for a new row with *w(r)* = 0. Keep a counter for each row, tracking the number of paintings in that row., intialized to 0 for each new row. Repeat the following for each painting *i*:
- Maintain the height of the previous painting, *prevH*, initialized to *h(0)* (painting 0). 
    - If *w(r)* + *w(i) $\le$ W*:
        - If *i* is the first painting in the row:
            - Add *h(i)* to *cost*. 
        - If *!minimumFound*:
            - If *h(i) $\le$ prevH* OR *h(i) == h(i+1)*:
                - Add painting *i* to row. Increment the counter for that row. Set *prevH = h(i)*.
            - Otherwise if *h(i) $\lt$ h(i+1)*:
                - Mark *minimumFound* as true. Store the counter, place *i* in a new row, then reset counter to 1. Set *prevH = h(i)*.
        - Otherwise if minimumFound:
            - If *h(i) $\gt$ prevH* OR *h(i) == h(i+1)*:
                - Add painting *i* to row. Increment the counter for that row. Set *prevH = h(i)*.
        - Delete painting *i*.
    - Otherwise:
        - Store the counter for the current row, then reset it to 0. Begin a new row. Set *prevH = h(i)*.

## Analysis 2
[insert analysis here]