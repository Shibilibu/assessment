def find_shortest_path(edges, start_node, end_node):
    # Initialize the distances dictionary with infinity for all nodes except the start node
    distances = {node: float('inf') for node in set(sum(([edge['from'], edge['to']] for edge in edges), []))}
    distances[start_node] = 0

    # Create a dictionary to store the predecessors of each node in the shortest path
    predecessors = {}

    # Loop until all nodes have been visited
    while distances:
        # Get the node with the smallest distance from the start node
        current_node = min(distances, key=distances.get)

        # If the current node is the end node, break the loop
        if current_node == end_node:
            break

        # Update distances and predecessors for neighbors of the current node
        for edge in edges:
            if edge['from'] == current_node:
                neighbor = edge['to']
                new_distance = distances[current_node] + edge['cost']
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node

        # Remove the current node from distances as it has been visited
        del distances[current_node]

    # Construct the shortest path from the dictionary
    shortest_path = [end_node]
    while end_node in predecessors:
        end_node = predecessors[end_node]
        shortest_path.append(end_node)
    shortest_path.reverse()

    return shortest_path

# input data (generated from Assignment 2)
edges = [{"from": "AA", "to": "BC", "cost": 1}, {"from": "BC", "to": "CW", "cost": 3},
         {"from": "BC", "to": "EF", "cost": 3.5}, {"from": "CW", "to": "EF", "cost": 4},
         {"from": "CW", "to": "DM", "cost": 2.5}, {"from": "DM", "to": "GQ", "cost": 2.5},
         {"from": "GQ", "to": "FO", "cost": 3.5}, {"from": "EF", "to": "FO", "cost": 2},
         {"from": "FO", "to": "HP", "cost": 2.5}, {"from": "HP", "to": "IK", "cost": 1}]

start_node = 'AA'
end_node = 'EF'
shortest_route = find_shortest_path(edges, start_node, end_node)
print("Shortest Route:", shortest_route)