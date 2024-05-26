from flask import Blueprint, render_template, request, jsonify
from backend.command_processor import CommandProcessor
from backend.path_planner import PathPlanner
from backend.drone_controller import DroneController

# Create a blueprint for the main routes
main = Blueprint('main', __name__)

# Initialize the command processor, path planner, and drone controller
processor = CommandProcessor(api_key="your-openai-api-key")
planner = PathPlanner()
controller = DroneController(drone_api=None)  # Replace with actual drone API

@main.route('/')
def index():
    """
    Render the index page.
    
    Returns:
    HTML: The rendered index page.
    """
    return render_template('index.html')

@main.route('/control', methods=['POST'])
def control():
    """
    Handle the control command from the user.
    
    Request data:
    - command (str): The natural language command to be processed.
    
    Returns:
    JSON: The interpreted command for drone navigation.
    """
    command = request.form['command']
    interpreted_command = processor.process_command(command)
    return jsonify({"interpreted_command": interpreted_command})

@main.route('/plan-path', methods=['POST'])
def plan_path():
    """
    Handle the path planning request from the user.
    
    Request data:
    - start (int): The starting waypoint ID.
    - end (int): The ending waypoint ID.
    
    Returns:
    JSON: The planned path as a list of waypoint IDs.
    """
    start = request.form['start']
    end = request.form['end']
    path = planner.plan_path(start, end)
    return jsonify({"path": path})

@main.route('/execute', methods=['POST'])
def execute():
    """
    Handle the command execution request from the user.
    
    Request data:
    - command (str): The command to be executed by the drone.
    
    Returns:
    JSON: The status of the command execution.
    """
    command = request.form['command']
    controller.execute_command(command)
    return jsonify({"status": "success"})
