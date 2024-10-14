# Conclusions

## Summary
In Milestone 1, we learned how and when to apply greedy algorithms to specific types of problems. Through our efforts, we found that different variations of a similar problem may sometimes require varying implementations of a greedy algorithm, but similar algorithmic design paradigms can easily be implemented across similar problems. 

Upon designing and implementing Algorithm 1, we initially believed we would need to create an entirely new algorithm for Problem S2. However, after attempting from scratch using a left->right scan of the paintings, we discovered that extending the logic of Algorithm 1 was sufficient to solve Problem S2 efficiently. We discovered the novelty and importance of applying algorithmic principles between similar problems, bolstering both correctness and performance. 


## Problem S1
A lot of care went into understanding the problem and all of its nuances, and through careful analysis, we were able to craft highly detailed and well-structured psuedocode for our Problem S1 solution. This allowed us to break down the problem logically and into well-detailed steps, enabling the easy implementation of our algorithm using Python. 

Furthermore, Problem S1 only requires a basic greedy algorithm, so it was fairly straightforward regardless. Our original implementation worked as intended immediately, and the only changes made were ones that optimized the algorithm's performance.

In terms of techincal challenges, the only issue we faced were those that arose from optimizing the code. For example, after our initial changes to optimize the algorithm were made, we found that the algorithm actually performed worse than before. Thankfully, this was resolved quickly. We were also fortunate to have a team member skilled with Python CSV, making the process of handling input and output files very smooth.

## Problem S2
For ProblemS2, our team put even more time than we did with ProblemS1 into fully understanding the nature of the challenge, as it was expected to be more difficult. Because of this, we were able to identify edge cases quickly, and more importantly correct mistakes that we made while implementing Algorithm 2. For example, we initally begun to develop an entirely new greedy algorithm, but quickly understood that ultizing Algorithm 1 in an altered fasion would provide a more straightforward and optimal solution.

One of the main challenges we faced with ProblemS2 was simply getting the algorithm to work correctly. Even though we quickly realized that Algorithm 1 could be added upon and changed to solve ProblemS2, it was difficult to get it to work for all inputs. It took a significant amount of debugging and logic fixes to arrive at our final implementation. However, our final version can consistently find the optimal layout of the platforms to minimize the total height.
