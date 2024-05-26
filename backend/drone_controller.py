class DroneController:
    def __init__(self, drone_api):
        self.drone_api = drone_api

    def execute_command(self, command):
        if command == "takeoff":
            self.drone_api.takeoff()
        elif command == "land":
            self.drone_api.land()
        else:
            self.drone_api.fly_to(command['waypoint'])

if __name__ == "__main__":
    class MockDroneAPI:
        def takeoff(self):
            print("Drone taking off")
        
        def land(self):
            print("Drone landing")
        
        def fly_to(self, waypoint):
            print(f"Flying to waypoint {waypoint}")

    controller = DroneController(drone_api=MockDroneAPI())
    controller.execute_command("takeoff")
    controller.execute_command({"waypoint": 3})
    controller.execute_command("land")
