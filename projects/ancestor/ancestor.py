from util import  Stack, Graph

def earliest_ancestor(ancestors, starting_node):
    ancestor_tree = Graph()
    for (parent, child) in ancestors:
    	ancestor_tree.add_vertex(parent)
    	ancestor_tree.add_vertex(child)
    	ancestor_tree.add_edge(child, parent)
    stack = Stack()
    stack.push([starting_node])
    longest_path = 1
    earliest_ancestor = -1
    while stack.size() > 0:
    	path = stack.pop()
    	vertex = path[-1]
    	if (len(path) >= longest_path and vertex < earliest_ancestor) or (len(path) > longest_path):
    		earliest_ancestor = vertex
    		longest_path = len(path)
    	for neighbor in ancestor_tree.get_neighbors(vertex):
    		new_path = list(path)
    		new_path.append(neighbor)
    		stack.push(new_path)
    
    return earliest_ancestor