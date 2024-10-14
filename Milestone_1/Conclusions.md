# Conclusions

## Summary
In Milestone 1, we learned how and when to apply greedy algorithms to specific types of problems. Through our efforts, we found that different variations of a similar problem may sometimes require varying implementations of a greedy algorithm, but similar algorithmic design paradigms can easily be implemented across similar problems. 

Upon designing and implementing Algorithm 1, we initially believed we would need to create an entirely new algorithm for Problem S2. However, after attempting from scratch using a left->right scan of the paintings, we discovered that extending the logic of Algorithm 1 was sufficient to solve Problem S2 efficiently. We discovered the novelty and importance of applying algorithmic principles between similar problems, bolstering both correctness and performance. 


## Problem S1
A lot of care went into understanding the problem and all of its nuances, and through careful analysis, we were able to craft highly detailed and well-structured psuedocode for our Problem S1 solution. This allowed us to break down the problem logically and into well-detailed steps, enabling the easy implementation of our algorithm using Python. 

Furthermore, Problem S1 only requires a basic greedy algorithm, so it was fairly straightforward regardless. Our original implementation worked as intended immediately, and the only changes made were ones that optimized the algorithm's performance.

In terms of techincal challenges, the only issue we faced were those that arose while optimizing the code. For example, after our initial optimization changes, we found that the algorithm actually performed worse than before. Thankfully, this was resolved quickly with some careful reading and problem-solving skills. We were also fortunate to have a team member experienced with Python CSV, making it easy to generate test results.

## Problem S2
While attacking Problem S2, we invested more time than with Problem S1 into fully understanding the nature of the challenge, as it was expected to be more difficult. Because of this, we were able to identify edge cases quickly, and more importantly, correct careless mistakes that were made when designing Algorithm 2. We initially created an entirely new greedy algorithm that attempted to read the list of paintings from left to right, but we discovered that applying Algorithm 1's strategy to two separate sub-problems was more effective (and performant). 

One of the main challenges we faced with Problem S2 was simply achieving correct output. Even though we knew that Algorithm 1 could be the foundation, and modified to solve Problem S2, it was difficult to get it to work for all inputs. A significant amount of debugging and logic fixes were necessary to arrive at our final implementation. Even still, inputs with large sizes (roughly $>9000$) seem to cause widly varying performance times, however the trends show that our time complexity analyses are still correct, and that Algorithm 2 still performs well. 
