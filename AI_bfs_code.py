visited=[]
queue=[]
def bfs(graph,visited,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m+" ")
        for adjacent in graph[m]:
          if adjacent not in visited:
            visited.append(adjacent)
            queue.append(adjacent)
graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
    node = (input(f"Enter the node {i+1}: "))
    neighbours = (input("Enter the neighbours separated by a space: ")).split()
    graph[node] = neighbours
start=input("Enter the starting vertex:")
print("bfs is")
bfs(graph,visited,start)
