# pilfered this from quickcode on github

from node import Node

class DirectedGraph:
  def __init__(self, nodes):
    self.nodes = nodes
  def updateAll(self):
    for node in self.nodes:
      node.outDegree = len(node.edges)
      for node2 in self.nodes:
        if node is node2:
          continue
        if node2.hasEdgeTo(node):
          node.inDegree += 1

def toposort(graph):
  q = []
  count = 0
  list = []
  for node in graph.nodes:
    if node.inDegree == 0:
      q.append(node)
  while q:
    v = q.pop(0)
    list.append(v)
    count += 1
    v.topNum = count
    for w in v.edges:
      w.inDegree -= 1
      if w.inDegree == 0:
        q.append(w)
 
  if count != len(graph.nodes):
    raise RuntimeError("CYCLES_FOUND_EXCEPTION")

  for item in list:
   print(item)