from flask import Flask, jsonify
from datetime import datetime
import sys
import importlib.metadata  # To get the version of packages

# Create Flask app instance
app = Flask(__name__)

# Root route to display current time and version details in a table format
@app.route('/', methods=['GET'])
def home():
    # Get the current time in hh:mm:ss format
    current_time = datetime.now().strftime('%H:%M:%S')

    # Get the Python version
    python_version = sys.version.split()[0]

    # Get Flask version using importlib.metadata
    flask_version = importlib.metadata.version('Flask')

    # Get Werkzeug version using importlib.metadata
    werkzeug_version = importlib.metadata.version('werkzeug')

    # Get the project path (current directory where the app is running from)
    project_path = sys.path[0]

    # Prepare the data to be displayed in a tabular format
    data = [
        {"SNo": 1, "Project Detail": "Current Time", "Value": current_time},
        {"SNo": 2, "Project Detail": "Python Version", "Value": python_version},
        {"SNo": 3, "Project Detail": "Flask Version", "Value": flask_version},
        {"SNo": 4, "Project Detail": "Werkzeug Version", "Value": werkzeug_version},
        {"SNo": 5, "Project Detail": "Project Path", "Value": project_path}
    ]

    # Return the data in JSON format (use jsonify to format the response as JSON)
    return jsonify(data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
