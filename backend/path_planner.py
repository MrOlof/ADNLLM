import networkx as nx

class PathPlanner:
    def __init__(self):
        self.graph = nx.Graph()

    def add_waypoints(self, waypoints):
        for point in waypoints:
            self.graph.add_node(point['id'], pos=(point['x'], point['y']))
            if 'neighbors' in point:
                for neighbor in point['neighbors']:
                    self.graph.add_edge(point['id'], neighbor)

    def plan_path(self, start, end):
        path = nx.shortest_path(self.graph, source=start, target=end, weight='distance')
        return path

# Example usage
if __name__ == "__main__":
    planner = PathPlanner()
    waypoints = [
        {"id": 1, "x": 0, "y": 0, "neighbors": [2]},
        {"id": 2, "x": 1, "y": 1, "neighbors": [1, 3]},
        {"id": 3, "x": 2, "y": 2, "neighbors": [2]}
    ]
    planner.add_waypoints(waypoints)
    path = planner.plan_path(1, 3)
    print(path)
