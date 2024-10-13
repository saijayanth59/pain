class UnionFind:
    def __init__(self, n: int) -> None: # initialize the parent and rank of each node
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int: # find the root of x and compress the path
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None: # union x and y by rank
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: #check if both have same parent
            return
        if self.rank[root_x] > self.rank[root_y]: #swap the roots if rank of x is greather the y
            root_x, root_y = root_y, root_x
        self.parent[root_x] = self.parent[root_y] #make parent of higher rank root to the lower rank root
        self.rank[root_y] += self.rank[root_x] #update rank
    
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

