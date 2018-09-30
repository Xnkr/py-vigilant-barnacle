def dfs_rec(adjLists, visited, v, goal, path):
    visited[v] = True
    path.append(v)
    if v == goal:
    	return True
    for w in adjLists[v]:
        if(not visited[w]):
            boo = dfs_rec(adjLists, visited, w, goal, path)
            if boo:
            	return True
    path.pop()
 
             
# Usually dfs_rec() would be sufficient. However, if we don't want to pass
# a boolean array to our function, we can use another function dfs().
# We only have to pass the adjacency list and the source node to dfs(), 
#as opposed to dfs_rec(), where we have to pass the boolean array additionally.
def dfs(adjLists, s, goal, path):
    visited = [False]*len(adjLists)
    boo = dfs_rec(adjLists, visited, s, goal, path)
 
# ------------------------------------------------------------------
 
# create the graph in adjacency list representation
adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]
 
# test our implementation
path = []
dfs(adjLists, 2, 6, path)
print path
