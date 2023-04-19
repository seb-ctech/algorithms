from union_find import UnionFind

class Percolation: 

    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n):
      if n > 0:
        pass
      else:
        raise ValueError(" 'n' must be bigger than 0 ")

    # opens the site (row, col) if it is not open already
    def open_site(self, row, col):

      if row > 0 and col > 0:
        pass
      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")

      pass

    # is the site (row, col) open?
    def is_open(self, row, col):
      if row > 0 and col > 0:
        pass
      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")
      pass

    # is the site (row, col) full?
    def is_full(self, row, col):
      if row > 0 and col > 0:
        pass
      else:
        raise ValueError(" row and col must be in the range of grid and both be bigger than 0 ")
      pass

    # returns the number of open sites
    def number_of_open_sites(self):
      pass

    # does the system percolate?
    def percolates(self):
      pass

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
  p = Percolation(1)
  p.open_site(0, 1)