"""
Return True if cycle is found, else False
"""

from typing import List
from collections import defaultdict, deque

def canFinish(numCourses:int, prerequisites: List[List[int]]):
    # populating adj graph and indegree array
    graph = defaultdict(list)
    indegree = [0]*numCourses 

    for start, end in prerequisites:
        graph[start].append(end)
        indegree[end] += 1
    
    q = deque()

    for node in range(numCourses):
        if indegree[node] == 0:
            q.append(node)

    visited = 0
    while q:
        cur = q.popleft()
        visited += 1
        if cur in graph:
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
    
    return visited == numCourses



"""
Test case 1 : numCourses = 2, preq = [1, 0]
Expected : True
"""
assert(canFinish(2, [[1,0]])) == True

"""
Test case 2 : numCourses = 2, preq =[[1,0], [0,1]]
"""
assert(canFinish(2, [[1,0], [0,1]])) == False