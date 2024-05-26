import numpy as np

class ObstacleDetector:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def detect_obstacles(self):
        obstacles = []
        for data in self.sensor_data:
            if data['distance'] < data['threshold']:
                obstacles.append(data['position'])
        return obstacles

if __name__ == "__main__":
    sensor_data = [
        {"position": (1, 2), "distance": 1.5, "threshold": 2.0},
        {"position": (3, 4), "distance": 2.5, "threshold": 2.0}
    ]
    detector = ObstacleDetector(sensor_data=sensor_data)
    obstacles = detector.detect_obstacles()
    print(obstacles)
