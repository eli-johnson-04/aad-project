### Elijah Johnson, Patrick Kallenbach, Nicholas Lindner
# Experimental Comparative Study

## Method
We have devised a system to easily test Algorithms 1 and 2 in *program1.py* and *program2.py*, using some constants and Python's CSV library to generate a CSV file. These tests will use an integer value in $\mathbb{Z^+}$, and generate sets of Problem S1 and Problem S2 instances for each algorithm, respectively. In *program1.py*, the value, say, $x$, will be used to generate $x$ multiples of $1000$ elements from $1$ to $x$ inclusive, whose elements begin at $x * 1000$ and decrease to $1$. In *program2.py*, the elements are randomly generated, as well as the index of the minimum, but the output fits the problem description. 

Each run of $n$ elements is performed a specific number of times $c$, where $c$ runs are then averaged to get the performance time for $n$ elements. 

## Performance Comparison
