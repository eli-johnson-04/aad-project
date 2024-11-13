# Conclusions

## Summary
For this milestone, we were tasked with creating three new algorithms for solving the General form of our original problem definition. In our first milestone, we designed a greedy algorithm to solve special cases of the problem, in which the paintings were arranged in decending order of height, or were organized with heights descending toward one central painting. However, for this milestone we were tasked with solving the general case where paintings can be arranged in any height. We achieved this by designing three different Dynamic Programming algorithms that solve the problem with three different time complexities.

The first algorithm solves the problem using a "Brute Force" algorithm, which uses a running recursion tree to solve every subproblem manually, without storing the output of each iteration. The second variation of the algorithm ____________. Lastly, the third variation performs the same process as the first algorithm, storing the result of each call to save on computation. This algorithm was implemented using both a top-down and bottom-up approach.

## Implementation Challenges
### Program 3
<!-- Write about challenges here!-->

### Program 4
<!-- Write about challenges here!-->

### Program 5A
Because this algorithm was heavily dependent on the structure of Algorithm 3, the implementation was not too much of a challenge. The algorithm needed to store each of the calls to a subproblem $\text{OPT}(j)$, which were kept in an array passed through each recursive function call. By storing these values, redundant calls to $\text{OPT}(j)$ can be stored and retrieved, which significantly reduces the complexity of the algorithm. There were only some slight issues with accidentally referencing variables rather than creating true copies, but there were no other challenges aside from that minor hurdle.

### Program 5B
With the Pseudocode done, converting the Bottom-Up approach into functioning code was not too difficult. There were some complications in converting the Pseudocode to working code in a way that was readable and easy to follow, but it generally resulted in code that was simpler and more straigforward than the Top-Down approach.