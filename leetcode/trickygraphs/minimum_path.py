"""
We can find minimum in a graph using a few different algorithms.
1. Dijkstra algorithm
What it does : Finds shortest paths from the starting node to all nodes
Intuition : Maintains distances to all nodes and reduces them during search.
Pros : Efficient and can be used for processing large graphs
Cons : Only works if there are no negative edges in the graph. Why? Dijsktra always commits to the current shortest path found so far, but it doesnt account for the possibility 
that a longer initial path might be improved by a subsequent negative edge, meaning that it might finalize distances prematurely.

Important properties : 
-Whenever a node is selected, its distance is final.
"""
from typing import List
import heapq

"""
Leetcode 743 : Standard dijkstra algorithm
"""
class Leetcode743:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # convert the adjacency list to a graph representation
        # use dijkstra algorithm to find the shortest path from node k to all nodes
        # return the time when the last node receives the signal
        # number of nodes = n, keep a count for the number of nodes that have received signal
        # decrement node each time one is relaxed, done when n == 0
        # return the last weight we relaxed

        # graph : source node -> [(weight, target node), ...]
        graph = {}
        for node in range(1, n+1):
            graph[node] = [] # initialise array for each node
        
        for source, target, weight in times:
            graph[source].append((weight, target)) # populate graph
        
        minheap = [(0, k)] # initialise with starting node
        visited = set()
        while minheap:
            cur_weight, cur_node = heapq.heappop(minheap)
            if cur_node in visited:
                continue
                
            visited.add(cur_node)
            if len(visited) == n:
                return cur_weight

            for nei_wei, nei_node in graph[cur_node]:
                if nei_node not in visited:
                    heapq.heappush(minheap, (cur_weight+nei_wei, nei_node))

        return -1




"""
Leetcode 64 (Solvable with dp too)
Finding shortest path in a grid where we can only move right or down
Why can we prematurely add the new coordinates to the 'visited' set?

Think about it this way. We pop from the minheap, we have a cost to reach a certain coordinate.
We look at its neighbors to the right and downwards.
Suppose that adding the current cost to the neighbors is not the cheapest way to reach the neighbors. This means that it has to come from another coordinate in the minheap.
But all other coordinates have a higher cost than the popped minimum cost. Thus, it is impossible to find a cheaper cost to reach the neighbor.
And thus, we can prematurely add each neighbor we encounter in the visited set and optmise the modified dijkstra's algorithm.
"""