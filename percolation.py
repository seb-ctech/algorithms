from union_find import UnionFind

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
            print ("Created Site: " + str(i) + "x" + str(j))
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
          print("Opened Site: " + str(row) + "x" + str(col))
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
    pass

  # sample mean of percolation threshold
  def mean():
    pass

  # sample standard deviation of percolation threshold
  def stddev():
    pass
  # low endpoint of 95% confidence interval
  def confidenceLo():
    pass
  # high endpoint of 95% confidence interval
  def confidenceHi():
    pass

if __name__ == "__main__":
  print("Percolation")
  n = 10
  p = Percolation(n)
  print("Perculates? -> " + str(p.percolates()))
  for i in range(n):
    p.open_site(i + 1, round(n/2))
  print("Perculates? -> " + str(p.percolates()))

  
  