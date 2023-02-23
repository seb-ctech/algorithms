class UnionFind:

  def simple_init(self, n):
    self.id = []
    for i in range(n):
      self.id.append(i)

  # Quick Find -- Algorithm implementation

  def qf_union(self, p, q):
    pid = self.id[p]
    qid = self.id[q]
    for i in range(len(self.id)):
      if(self.id[i] == pid):
        self.id[i] = qid

  def qf_connected(self, p, q):
    return self.id[p] == self.id[q]

  # Quick Union -- Algorithm implementation
  
  def get_root(self, i):
    while not i == self.id[i]:
      ## Path Compression
      self.id[i] = self.id[self.id[i]]
      i = self.id[i]
    return i

  def qu_union(self, p, q):
    i = self.get_root(p)
    j = self.get_root(q)
    self.id[i] = j

  def qu_connected(self, p, q):
    return self.get_root(p) == self.get_root(q)

  # Weighted Quick Union -- Algorithm implementation

  def weighted_init(self, n):
    self.id = []
    self.sz = []
    for i in range(n):
      self.id.append(i)
      self.sz.append(1)

  def wqu_union(self, p, q):
    i = self.get_root(p)
    j = self.get_root(q)
    if not i == j:
      if self.sz[i] < self.sz[j]:
        self.id[i] = j
        self.sz[j] += self.sz[i]
      else:
        self.id[j] = i
        self.sz[i] += self.sz[j]

  def __init__(self, N):
    self.weighted_init(N)

  def __str__(self):
    return f"{self.id}"

  def union(self, p, q):
    self.wqu_union(p, q)

  def connected(self, p, q):
    return self.qu_connected(p, q)


if __name__ == "__main__":
  n = input("Enter N: ")
  uf = UnionFind(int(n))
  getInput = True
  while getInput:
    p = input("Tell me one Value: ")
    q = input("Tell me the other Value: ")
    if p and q:
      if not uf.connected(int(p), int(q)):
        uf.union(int(p), int(q))
        print(p + " <-> " + q)
    else:
      getInput = False
  print(uf)