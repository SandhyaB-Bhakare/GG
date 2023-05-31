visited=[]
stack=[]
def dfs(graph, visited, node):
    visited.append(node)
    stack.append(node)
    print(node)
    while stack:
       m = stack[-1]
       
       found_unvisited_neighbour = False
       for adjacent in graph[m]:
          if adjacent not in visited:
            visited.append(adjacent)
            stack.append(adjacent)
            print(adjacent)
            found_unvisited_neighbour = True
            break
       if not found_unvisited_neighbour:
          stack.pop()
graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
  node = input(f"Enter the node {i+1}: ")
  neighbours = input("Enter the neighbours separated by a space: ").split()
  graph[node] = neighbours
start=input("Enter the root node:")
print("dfs is")
dfs(graph, visited, start)
"""
OUTPUT:
Enter the number of nodes: 10
Enter the node 1: 1
Enter the neighbours separated by a space: 4 2
Enter the node 2: 2
Enter the neighbours separated by a space: 1 5 7 3 6
Enter the node 3: 3
Enter the neighbours separated by a space: 4 2 10 9
Enter the node 4: 4
Enter the neighbours separated by a space: 1 3
Enter the node 5: 5
Enter the neighbours separated by a space: 2 6 7
Enter the node 6: 6
Enter the neighbours separated by a space: 5 2 7 8
Enter the node 7: 7
Enter the neighbours separated by a space: 5 2 6
Enter the node 8: 8
Enter the neighbours separated by a space: 6
Enter the node 9: 9
Enter the neighbours separated by a space: 3
Enter the node 10: 10
Enter the neighbours separated by a space: 3
Enter the root node:1
dfs is
1
4
3
2
5
6
7
8
10
9
"""