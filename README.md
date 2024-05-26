# Autonomous Drone Navigation using Large Language Models

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage Instructions](#usage-instructions)

## Introduction
This project leverages a Large Language Model (LLM) to autonomously control drones. The LLM interprets commands, plans flight paths, and navigates drones through complex environments. The project includes modules for natural language processing, drone control, and real-time environmental analysis.

## Features
- **Natural Language Command Processing:** Understand and interpret flight commands.
- **Path Planning:** Generate optimized flight paths.
- **Real-time Navigation:** Adjust drone paths based on live environmental data.
- **Obstacle Detection:** Identify and avoid obstacles.
- **Simulated and Real-World Deployment:** Test in a simulated environment and deploy on real drones.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Docker
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MrOlof/ADNLLM.git
   cd autonomous-drone-navigation
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python frontend/app.py

docker-compose up --build 
```

## Usage Instructions
Web Interface:

Access the web interface at http://localhost:5000.
Use the control panel to issue flight commands.
Monitor drone status on the flight dashboard.
Simulated Environment:

Run the simulation script to test in a simulated environment.
bash
Copy code
`` ./scripts/start_simulation.sh  ``
