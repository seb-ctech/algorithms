from union_find import UnionFind
import random
import statistics
import sys


# Specification: https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php

class Percolation: 

    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n):
      if n > 0:
        self.number_of_sites = (n * n)
        # add virtual sites (one for top and one for bottom)
        self.size = n
        self.sites = ["Top", "Bottom"] # index 0 and 1
        self.open_sites = 0
        # init closed sites
        for i in range(n+1):
          for j in range(n+1):
            self.sites.append(False)
            # print ("Created Site: " + str(i) + "x" + str(j))
        self.quick_union = UnionFind(len(self.sites))
      else:
        raise ValueError(" 'n' must be bigger than 0 ")

    def get_index_of_site(self, x, y):
      return x * y + x

    def get_adjacent_open_sites(self, row, col):
      open_adj_sites = []
      if (row > 1):
        top = self.get_index_of_site(row - 1, col)
        if (self.is_open(row - 1, col)):
          open_adj_sites.append(top)
      if (row < self.size):
        bottom = self.get_index_of_site(row + 1, col)
        if (self.is_open(row + 1, col)):
          open_adj_sites.append(bottom)
      if (col > 1):
        left = self.get_index_of_site(row, col - 1)
        if (self.is_open(row, col - 1)):
          open_adj_sites.append(left)
      if (col < self.size):
        right = self.get_index_of_site(row, col + 1)
        if (self.is_open(row, col + 1)):
          open_adj_sites.append(right)
      return open_adj_sites

    # opens the site (row, col) if it is not open already
    def open_site(self, row, col):
      target_index = self.get_index_of_site(row, col)
      if row > 0 and col > 0:
        if not self.is_open(row, col):
          self.sites[target_index] = True
          self.open_sites += 1
          # print("Opened Site: " + str(row) + "x" + str(col))
          if row > 1:
            if row == self.size:
              self.quick_union.union(target_index, 1)
          else:
            self.quick_union.union(target_index, 0)
          adj = self.get_adjacent_open_sites(row, col)
          for a in adj:
           if not self.quick_union.connected(target_index, a):
            self.quick_union.union(target_index, a)

      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")

    # is the site (row, col) open?
    def is_open(self, row, col):
      if row > 0 and col > 0:
        i = self.get_index_of_site(row, col)
        return self.sites[i]
      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")
      pass

    # is the site (row, col) full?
    def is_full(self, row, col):
      if row > 0 and col > 0:
        return not self.is_open(row, col)
      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")
      pass

    # returns the number of open sites
    def number_of_open_sites(self):
      return self.open_sites

    # does the system percolate?
    def percolates(self):
      return self.quick_union.connected(0, 1)

class PercolationStats:

  # perform independent trials on an n-by-n grid
  def __init__(self, n, trials):
    # exception ValueError
    self.results = []
    print("Running Percolation " + str(trials) + " times")
    for i in range(int(trials)):
      self.run_try(int(n))
    # print(self.results)
    pass

  def run_try(self, n):
    p = Percolation(n)
    
    while(not p.percolates()):
      randx = random.randint(1, n)
      randy = random.randint(1, n)
      p.open_site(randx, randy)
      
    # print((p.number_of_open_sites()) / (n*n))
    self.results.append((p.number_of_open_sites() / (n*n)))
    pass

  # sample mean of percolation threshold
  def mean(self):
    return statistics.mean(self.results)

  # sample standard deviation of percolation threshold
  def stddev(self):
    return statistics.stdev(self.results)
  # low endpoint of 95% confidence interval
  def confidenceLo(self):
    dev = self.stddev()
    return self.mean() - dev
  # high endpoint of 95% confidence interval
  def confidenceHi(self):
    dev = self.stddev()
    return self.mean() + dev
    pass

if __name__ == "__main__":
  args = sys.argv[1:]
  percolate_stats = PercolationStats(args[0], args[1])
  print("Mean is: " + str(percolate_stats.mean()) + " and Standard Deviation is: " + str(percolate_stats.stddev()))
  print("Low threshhold is: " + str(percolate_stats.confidenceLo()))
  print("High threshhold is: " + str(percolate_stats.confidenceHi()))

  
  