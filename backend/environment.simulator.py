import random

class EnvironmentSimulator:
    def __init__(self, size):
        self.size = size
        self.obstacles = []

    def generate_obstacles(self, num_obstacles):
        for _ in range(num_obstacles):
            obstacle = {
                "x": random.uniform(0, self.size),
                "y": random.uniform(0, self.size)
            }
            self.obstacles.append(obstacle)
        return self.obstacles

# Example usage
if __name__ == "__main__":
    simulator = EnvironmentSimulator(size=100)
    obstacles = simulator.generate_obstacles(num_obstacles=5)
    print(obstacles)
