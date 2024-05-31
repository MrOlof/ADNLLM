import networkx as nx
import numpy as np

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
                    self.graph.add_edge(point['id'], neighbor, weight=self.calculate_distance(point, neighbor))

    def calculate_distance(self, point, neighbor_id):
        """
        Calculate the Euclidean distance between two waypoints.
        
        Parameters:
        point (dict): The current waypoint.
        neighbor_id (int): The ID of the neighboring waypoint.
        
        Returns:
        float: The Euclidean distance.
        """
        neighbor = self.graph.nodes[neighbor_id]
        x1, y1 = point['x'], point['y']
        x2, y2 = neighbor['pos']
        return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_waypoint(self, waypoint_id, new_x, new_y):
        """
        Update the position of an existing waypoint.
        
        Parameters:
        waypoint_id (int): The ID of the waypoint to update.
        new_x (float): The new x-coordinate.
        new_y (float): The new y-coordinate.
        """
        self.graph.nodes[waypoint_id]['pos'] = (new_x, new_y)
        # Update distances for edges connected to this waypoint
        for neighbor in self.graph.neighbors(waypoint_id):
            self.graph.edges[waypoint_id, neighbor]['weight'] = self.calculate_distance(self.graph.nodes[waypoint_id], neighbor)

    def add_obstacle(self, obstacle_id, connected_waypoints):
        """
        Add an obstacle to the graph by increasing the edge weights significantly.
        
        Parameters:
        obstacle_id (int): The ID of the obstacle waypoint.
        connected_waypoints (list of int): The IDs of waypoints connected to the obstacle.
        """
        for neighbor in connected_waypoints:
            if self.graph.has_edge(obstacle_id, neighbor):
                self.graph.edges[obstacle_id, neighbor]['weight'] *= 10  # Increase weight to avoid this path

    def remove_obstacle(self, obstacle_id, connected_waypoints):
        """
        Remove an obstacle from the graph by restoring the original edge weights.
        
        Parameters:
        obstacle_id (int): The ID of the obstacle waypoint.
        connected_waypoints (list of int): The IDs of waypoints connected to the obstacle.
        """
        for neighbor in connected_waypoints:
            if self.graph.has_edge(obstacle_id, neighbor):
                self.graph.edges[obstacle_id, neighbor]['weight'] /= 10  # Restore weight

    def plan_path(self, start, end, constraints=None):
        """
        Plan the shortest path between two waypoints using Dijkstra's algorithm with optional constraints.
        
        Parameters:
        start (int): The starting waypoint ID.
        end (int): The ending waypoint ID.
        constraints (dict): Optional constraints such as no-fly zones.
        
        Returns:
        list of int: The ordered list of waypoint IDs in the planned path.
        """
        if constraints:
            for no_fly_zone in constraints.get('no_fly_zones', []):
                self.add_obstacle(no_fly_zone['id'], no_fly_zone['connected_waypoints'])
                
        path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
        
        if constraints:
            for no_fly_zone in constraints.get('no_fly_zones', []):
                self.remove_obstacle(no_fly_zone['id'], no_fly_zone['connected_waypoints'])
                
        return path

if __name__ == "__main__":
    # Example usage
    planner = PathPlanner()
    
    # Define waypoints with coordinates and neighbors
    waypoints = [
        {"id": 1, "x": 0, "y": 0, "neighbors": [2]},
        {"id": 2, "x": 1, "y": 1, "neighbors": [1, 3, 4]},
        {"id": 3, "x": 2, "y": 2, "neighbors": [2]},
        {"id": 4, "x": 1, "y": 3, "neighbors": [2]}
    ]
    
    # Add waypoints to the planner
    planner.add_waypoints(waypoints)
    
    # Plan the path from waypoint 1 to waypoint 3
    path = planner.plan_path(1, 3)
    
    # Print the planned path
    print(f"Planned path without constraints: {path}")
    
    # Define constraints such as no-fly zones
    constraints = {
        "no_fly_zones": [
            {"id": 4, "connected_waypoints": [2]}
        ]
    }
    
    # Plan the path from waypoint 1 to waypoint 3 with constraints
    path_with_constraints = planner.plan_path(1, 3, constraints)
    
    # Print the planned path with constraints
    print(f"Planned path with constraints: {path_with_constraints}")
