from flask import Blueprint, render_template, request, jsonify
from backend.command_processor import CommandProcessor
from backend.path_planner import PathPlanner
from backend.drone_controller import DroneController

main = Blueprint('main', __name__)

processor = CommandProcessor(api_key="your-openai-api-key")
planner = PathPlanner()
controller = DroneController(drone_api=None)  # Replace with actual drone API

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/control', methods=['POST'])
def control():
    command = request.form['command']
    interpreted_command = processor.process_command(command)
    return jsonify({"interpreted_command": interpreted_command})

@main.route('/plan-path', methods=['POST'])
def plan_path():
    start = request.form['start']
    end = request.form['end']
    path = planner.plan_path(start, end)
    return jsonify({"path": path})

@main.route('/execute', methods=['POST'])
def execute():
    command = request.form['command']
    controller.execute_command(command)
    return jsonify({"status": "success"})
