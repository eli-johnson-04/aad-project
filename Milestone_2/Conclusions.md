# Conclusions

## Summary
For this milestone, we were tasked with creating three new algorithms for solving the General form of our original problem definition. In our first milestone, we designed a greedy algorithm to solve special cases of the problem, in which the paintings were arranged in decending order of height, or were organized with heights descending toward one central painting. However, for this milestone we were tasked with solving the general case where paintings can be arranged in any height. We achieved this by designing three different Dynamic Programming algorithms that solve the problem with three different time complexities.

The first algorithm solves the problem using a "Brute Force" algorithm, which uses a running recursion tree to solve every subproblem manually, without storing the output of each iteration. The second variation of the algorithm ____________. Lastly, the third variation performs the same process as the first algorithm, storing the result of each call to save on computation. This algorithm was implemented using both a top-down and bottom-up approach.

## Implementation Challenges
### Program 3
Program3 was difficult because an exponential-time algorithm is basically guaranteed to hit Python's recursion limit, and attempting to find an upper limit that can handle the recursion is difficult. C++ was chosen instead, as it would (hopefully) be faster, at the expense of being harder to write. C++ is pickier with typing, and mutability and indexing between the two languages can feel like a guessing game. 

Aside from language challenges, Algorithm 3 was not exceedingly difficult to implement into code, it just required some hack-y solutions and careful, thorough debugging to resolve rampant indexing issues. Given that the description of Algorithm 3 is relatively generic and lacks pseudocode, program3 required mental acrobatics for designing a recursive solution. For example, it would have been asinine to attempt to create needed values on the fly when determining the minimum solution in the __options__ vector, and devising a lambda function to compare the second values of all the tuples was not expected to show up on the to-do list. 

There was also some confusion related to determining what value of $C_{ij}$ to use in the case that a row could not exist, as well as a redefinition of bounds in the original algorithm that was not initially accounted for, that would allow individual paintings to sit on their own rows. Algorithm 3 was the first and possibly most difficult algorithm we completed for this Milestone, and it was just as difficult to implement correctly. 

### Program 4
Although algorithm 4 is slower and has a larger time complexity ( $\Theta(n^3)$ ) than algorithms 5A and 5B, it was exceptionally difficult to program. Creating a structure of code that runs in $\Theta(n)$ time within the already functioning $\Theta(n^2)$ algorithm (since we decided creating the $\Theta(n^2)$ first and then extrapolating it from there would be the easiest), turned out to be more difficult than anticipated. To make it work we ended up having to alter the dynamic programming approach to construct a cost matrix. Unlike our initial $\Theta(n^2)$ time algorithm, we had to explicitly recomputate all possible groupings of paintings so that we could evalueate their total widths and max heights.

This required a triple-nested loop, where the first loop iterates through all potential starting paintings, the second loop iterates through all possible ending paintings for the current start point, and the third loop gets the total width and max height for the group of paintings from i to j.

Another difficulty of algorithm 4 was that backtracking became a lot more complicated, since now we could no longer just follow the recursive calls, but instead traverse the P array and reconstruct the optimal assignment only using the cost matrix. So overall, it seems that algorithm 4 was more complicated to create than expected.

### Program 5A
Because this algorithm was heavily dependent on the structure of Algorithm 3, the implementation was not too much of a challenge. The algorithm needed to store each of the calls to a subproblem $\text{OPT}(j)$, which were kept in an array passed through each recursive function call. By storing these values, redundant calls to $\text{OPT}(j)$ can be stored and retrieved, which significantly reduces the complexity of the algorithm. There were only some slight issues with accidentally referencing variables rather than creating true copies, but there were no other challenges aside from that minor hurdle.

### Program 5B
With the Pseudocode done, converting the Bottom-Up approach into functioning code was not too difficult. There were some complications in converting the Pseudocode to working code in a way that was readable and easy to follow, but it generally resulted in code that was simpler and more straigforward than the Top-Down approach.
