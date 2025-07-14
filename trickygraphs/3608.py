"""
Approach 1 :
Binary Search + DFS 
Time complexity : 
Space complexity :

Approach 2 :
Binary Search + UnionFind
Time complexity : 
Space complexity :

Approach 3 :
Union find in Reverse
Time complexity : 
Space complexity :

Edges with weight time <= t, will be removed. The greater the value of t, the greater the number of components.
We want to find the minimum value of t that will give us at least k connected components.
"""

# Approach 1

from typing import List


class Approach1:
    """
    Binary search on the range space of the possible t values
    We can check for the number of components using DFS / UnionFind
    """

    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        # populating graph
        graph = {}
        min_weight = 0
        max_weight = 0
        for i in range(n):
            graph[i] = []
        for u, v, w in edges:
            graph[u].append((w, v)) # (weight, neighboring node)
            graph[v].append((w, u))
            max_weight = max(max_weight, w) # find upper bound for binary search
        
        def find_components_dfs(time): # finding components by dfs
            visited = set()
            def dfs(point):
                if point in visited:
                    return
                visited.add(point)
                for wei, nei in graph[point]:
                    if wei > time:
                        dfs(nei)
            
            count = 0
            for node in range(n):
                if node not in visited:
                    dfs(node)
                    count += 1
            return count

        while min_weight <= max_weight:
            mid = (min_weight + max_weight) // 2
            if find_components_dfs(mid) >= k: # search lower range, finding components can be done with either using binary search or union find
                res = mid
                max_weight = mid - 1
            else: # search higher range
                min_weight = mid + 1

        return res


# We define a dsu class outside the solution class for simplicity
class DSU:
    def __init__(self, n):
        # initially each node is a parent of itself
        self.parent = list(range(n))
        self.rank = [1]*n 
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur 

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False # both nodes are already in the same component
        if self.rank[parent1] > self.rank[parent2]:
            parent1, parent2 = parent2, parent1

class Approach2:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        num_components = n
        min_weight = 0 
        max_weight = 0
        
        for u, v , w in edges:
            if dsu.union(u, v):
                num_components -= 1
            max_weight = max(max_weight, w)
        
        if num_components >= k:
            return 0
        
        def find_components(time):
            new_dsu = DSU(n)
            comps = n
            for u, v, w in edges:
                if w > time:                    
                    if new_dsu.union(u,v):
                        
                        comps -= 1
            return comps
        
        while min_weight <= max_weight:
            mid = (min_weight + max_weight) // 2
            if find_components(mid) >= k: # search lower range
                res = mid
                max_weight = mid - 1
            else:
                min_weight = mid + 1
        
        return res
    
"""
Intuition behind reverse union find:
We want to find the minimum time to form at least k components
We can start from the biggest possible value of t, i.e. we have n different components as there are no edges
We union edges from heaviest to lightest weight, and decrement our component count if the we have a successful union
If the number of components decreases below k, this tells us that that specific edge is the tipping point between
having just enough components and not having enough components
Thus this edge cannot be included for us to have the smallest value, hence we set the result to be equal to the weight of the edge itself so that 
it will not be included
"""

class Approach3:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        num_components = n
        edges.sort(key = lambda e: -e[2]) # sort from heaviest to lightest edge
        parents = list(range(n)) # initially, each node is a parent of itself
        rank = [1]*n # initially rank of all nodes is 1

        def find(node): # find parent
            cur = node
            while cur != parents[cur]:
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            return cur
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]: # standardise p1 to be the parent with the smaller rank
                p1, p2 = p2, p1
            parents[p1] = p2
            rank[p2] += rank[p1]
            return True
    
        for u, v, t in edges:
            if union(u, v):
                num_components -= 1
            if num_components < k:
                return t
        
        return 0
