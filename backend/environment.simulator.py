import random

class EnvironmentSimulator:
    def __init__(self, size):
        """
        Initialize the EnvironmentSimulator with a given environment size.
        
        Parameters:
        size (int or float): The size of the environment (assumed to be square).
        """
        self.size = size
        self.obstacles = []

    def generate_obstacles(self, num_obstacles):
        """
        Generate a specified number of obstacles within the environment.
        
        Parameters:
        num_obstacles (int): The number of obstacles to generate.
        
        Returns:
        list of dict: A list of obstacle positions, each represented as a dictionary with 'x' and 'y' coordinates.
        """
        for _ in range(num_obstacles):
            obstacle = {
                "x": random.uniform(0, self.size),
                "y": random.uniform(0, self.size)
            }
            self.obstacles.append(obstacle)
        return self.obstacles

# Example usage
if __name__ == "__main__":
    # Initialize the EnvironmentSimulator with an environment size of 100 units
    simulator = EnvironmentSimulator(size=100)
    
    # Generate 5 obstacles within the environment
    obstacles = simulator.generate_obstacles(num_obstacles=5)
    
    # Print the generated obstacles
    print(obstacles)
