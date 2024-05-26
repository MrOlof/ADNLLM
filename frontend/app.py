from flask import Flask
from routes import main

# Initialize the Flask application
app = Flask(__name__)

# Register the blueprint from the routes module
app.register_blueprint(main)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
