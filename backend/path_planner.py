import networkx as nx

class PathPlanner:
    def __init__(self):
        """Initialize the PathPlanner with an empty graph."""
        self.graph = nx.Graph()

    def add_waypoints(self, waypoints):
        """
        Add waypoints to the graph.
        
        Parameters:
        waypoints (list of dict): Each dictionary contains an 'id', 'x', 'y' for coordinates,
                                  and optionally 'neighbors' which is a list of connected waypoint IDs.
        """
        for point in waypoints:
            # Add a node for each waypoint with its position
            self.graph.add_node(point['id'], pos=(point['x'], point['y']))
            # Add edges to the graph for each neighbor connection
            if 'neighbors' in point:
                for neighbor in point['neighbors']:
                    self.graph.add_edge(point['id'], neighbor)

    def plan_path(self, start, end):
        """
        Plan the shortest path between two waypoints using Dijkstra's algorithm.
        
        Parameters:
        start (int): The starting waypoint ID.
        end (int): The ending waypoint ID.
        
        Returns:
        list of int: The ordered list of waypoint IDs in the planned path.
        """
        path = nx.shortest_path(self.graph, source=start, target=end, weight='distance')
        return path

if __name__ == "__main__":
    # Example usage
    planner = PathPlanner()
    
    # Define waypoints with coordinates and neighbors
    waypoints = [
        {"id": 1, "x": 0, "y": 0, "neighbors": [2]},
        {"id": 2, "x": 1, "y": 1, "neighbors": [1, 3]},
        {"id": 3, "x": 2, "y": 2, "neighbors": [2]}
    ]
    
    # Add waypoints to the planner
    planner.add_waypoints(waypoints)
    
    # Plan the path from waypoint 1 to waypoint 3
    path = planner.plan_path(1, 3)
    
    # Print the planned path
    print(path)

