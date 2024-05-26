import numpy as np

class ObstacleDetector:
    def __init__(self, sensor_data):
        """
        Initialize the ObstacleDetector with sensor data.
        
        Parameters:
        sensor_data (list of dict): Each dictionary contains 'position', 'distance', and 'threshold'
                                    where 'position' is a tuple (x, y), 'distance' is the distance to
                                    an obstacle, and 'threshold' is the minimum distance to consider
                                    an obstacle.
        """
        self.sensor_data = sensor_data

    def detect_obstacles(self):
        """
        Detect obstacles based on sensor data.
        
        Returns:
        list of tuple: A list of positions (x, y) where obstacles are detected.
        """
        obstacles = []
        for data in self.sensor_data:
            if data['distance'] < data['threshold']:
                obstacles.append(data['position'])
        return obstacles

if __name__ == "__main__":
    # Example usage
    sensor_data = [
        {"position": (1, 2), "distance": 1.5, "threshold": 2.0},
        {"position": (3, 4), "distance": 2.5, "threshold": 2.0}
    ]
    
    # Initialize the ObstacleDetector with sensor data
    detector = ObstacleDetector(sensor_data=sensor_data)
    
    # Detect obstacles
    obstacles = detector.detect_obstacles()
    
    # Print the detected obstacles
    print(obstacles)
