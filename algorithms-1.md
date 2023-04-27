# Algorithms

Data Structures: Method to represent data
Algorithms: Method to solve a problem
Data Structures + Algorithms = Programs

1. Model the Problem: What are the main elements
2. Find an algorithm to solve it
3. Is it fast enough and fits in memory?
4. If not, figure out why and iterate
5. Find a way to address the problem.
6. Iterate until satisfied

## Union Find


### Problem: Dynamic Connectivity

- Set of N Objects
- There is a union command to connect two objects
- Is there a both connecting two objects?
- Objects can be represented by an integer index

#### Applications

- Digital Photos for Pixels
- Computers in a network
- Friends in a social network
- Transistors in a computer chip

#### Data Structure

Components, containing a list of connected objects
- Find Query: Check if two objects are in the same component
- Union Command: Replace components containing two objects with their union


{1 2} {3 4} {5 6} {7 8 9}
{1 2 7 8 9} {3 4} {0 5 6}

#### Quick Find

- Eager Algorithm
- Data Structure: an integer array of size N
- p and q are connected if they have the same id
- Find: Check if p and q have the same id
- Union: To merge components containing p and q, change all entries whose id equals id[p] to id[q]
  - Problem: lot of elements that change; could be inefficent
  - ** Union is too expensive (Number of times the code has to access the array -> N^2) **
  - Quadratic time does not scale well, it gets slower


#### Quick Union

- Lazy Algorithm
- Data Structure: an integer array of size N
- id[i] is parent of i
- Root of i is id\[id\[id\[...id\[i]...]]]
- Find: p and q have the same root
  - Trees can get tall
  - too expensive (could be N array accesses)
- Union: to merge components containing p and q, set the id of p's root to the id of q's root


#### Improvement: Weighted Quick-Union

- weighting the trees
- Balance by linking root of smaller tree to root of larger tree
- Find: takes time proportional to depth of p and q
- Union: takes constant time, given roots
- Depth of any node x is at most log(N)

#### Improvement 2: Path compression
- Just after computing the root of p set the id of each examined node to point to that root
- Keeps tree almost flat
- In Theory -> WQUPC is not quite linear
- In Practive -> WQUPC is linear


#### Implementation in Object-Oriented Paradigm

- Data Structure can be directly manipulated during a step within the algorithm process like with the path compression step


### Applications

- Percolation
- Dynamic connectivity
- Games (Go, Hex)
- Kruskal's Algorithm

#### Perculation

- N x N grid of sites
- each site is open with probability p (or blocked with probability 1 - p)
- System percolates if top and bottom are connected by open sites

Electricity: system -> material | open site -> conductor | blocked site -> insulated | percolates -> conducts
Fluid Flow: system -> material | open site -> empty | blocked site -> blocked | percolates -> porous
Social Interaction: system -> population | open site -> person | blocked site -> empty | percolates -> communicates

- percolation depends on the probability of an open site
- there is a phase transition between the state when it percolates and when it doesn't
- To find this transition value we run a Monte Carlo simulation: Run the solution 1M times on each run open closed sites
- Union is called for each neighboring site that is already open. There are 4 possible neighbors, but some of them may not already be open.
- We check if N-by-N System percolates by creating an object for each site and them 0 to N^2 - 1
- Sites are in the same component if connected by open sites
- Add a virtual root on the top for the top-most row and a virtual root on the bottom for the bottom-most row
( We try to push the new problem into the domain of our existing data-structure )


## Analysis of Algorithms

Analysis of Algorithms is both possible with observation and inference aswell as with mathematical models,
however while they work in principle in practice they often require advanced mathematical concepts and are best left for the experts.
Therefor we use an approximated model.

### Order of Growth Classification

The parameters that determine the runtime of an algorithms are often the patterns inside the algorithm in combination with the amount of data.
Result in common classifications:

- 1 (Constant): Statement / No Loops

- log N: divide in half / binary search

- N (Linear): loop / find the maximum

- N log N (linearithmic):  divide and conquer / mergesort

- N² (Quadratic): double loop / check all pairs

- N³ (Cubic): Triple loop / check all triples

- 2^N / N^2 / N! (Exponential): exhaustive search / check all subpairs

Even nowadays we only can use Constant and LogN for Huge Data amounts (> Trilions of Data)

### Theory of Algorithms

- Design for the worst case
- Randomize and depend on probabilistic guarantee

#### Goals

- Establish difficulty
- Develop "optimal" algorithm

#### Approach

- Suppress details in analysis analyze "to within a constant factor"
- Eliminate variability in input model by focusing on the worst case.

Common misconception: Big O Notation is not equal to approximate model but defines the upper bound in the theory of algorithms.

### Memory

- Each data type occupies some memory
- However arrays occupy N * Data  type
- And objects and references have padding and object header / overhead to keep in mind
- Modern systems are assumed to have 64-bit systems which can adress a huge range of values, but pointers take up more memory