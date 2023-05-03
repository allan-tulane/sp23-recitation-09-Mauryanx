from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
       """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
  
  def helper(visited, frontier):
    if len(frontier) == 0:
      return visited
    else:
      distance, num_edges, node = heappop(frontier)
      if node in visited:
        return helper(visited, frontier)
      else:
        visited[node] = (distance, num_edges)
        for neighbor, weight in graph[node]:
          heappush(frontier, (distance + weight, num_edges + 1, neighbor))
        return helper(visited, frontier)

  frontier = []
  heappush(frontier, (0, 0, source))
  visited = dict()
  return helper(visited, frontier)
                
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
     """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
  final = {}
  frontier = {source}
  while len(frontier) > 0:
    source = frontier.pop()
    for n in graph[source]: 
      if n not in final.keys():
        final[n] = source
        frontier.add(n)
  return final

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
  if destination in parents:
    return get_path(parents, parents[destination]) + parents[destination]
  else:
    return ''

def test_get_path():
     """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
