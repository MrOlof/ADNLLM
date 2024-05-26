from flask import Blueprint, render_template, request, jsonify
from backend.command_processor import CommandProcessor
from backend.path_planner import PathPlanner
