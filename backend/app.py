import os
import time
import threading
from flask import Flask, jsonify, send_from_directory, request
import json

# --- Path Configuration ---
backend_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(backend_dir, '..', 'frontend')
COMMAND_FILE = os.path.join(backend_dir, 'command.txt')

# --- App Configuration ---
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')

# --- State Management ---
global_state = {
    "expression": "neutral",
    "subtitle": ""
}

# All allowed expressions based on available videos (from your avatar folder)
allowed_expressions = [
    "neutral", "orgullosa", "angry", "annoyed", "idle1", "idle2", "idle3", "idle4",
    "nervous", "sad", "sleepy", "happy", "thinking", "talking", "wink", "idea",
    "idea2", "curious", "excited"
]

# --- Command Processing Logic ---
def watch_command_file():
    print("--- Command file watcher started (Simple Logic) ---")
    while True:
        try:
            if os.path.exists(COMMAND_FILE):
                command_data = ""
                with open(COMMAND_FILE, 'r') as f:
                    command_data = f.read().strip()
                
                os.remove(COMMAND_FILE) # Always remove the file after reading

                command = None
                subtitle = ""

                try:
                    cmd_obj = json.loads(command_data)
                    command = cmd_obj.get('expression')
                    subtitle = cmd_obj.get('subtitle', "")
                except json.JSONDecodeError:
                    command = command_data # Assume it's just an expression
                    subtitle = ""

                if command in allowed_expressions:
                    global_state['expression'] = command
                    global_state['subtitle'] = subtitle
                    print(f"State updated: {global_state}")
                else:
                    print(f"Warning: Received invalid command '{command}' from file. Ignoring.")
            
        except Exception as e:
            print(f"Error in command watcher: {e}")
        
        time.sleep(0.5) # Check every 500ms

# --- API & Frontend Routes ---
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify(global_state)

# New route for settings/log window
@app.route('/settings')
def settings_panel():
    return send_from_directory(app.static_folder, 'settings.html')

# New API endpoint to get captured logs
@app.route('/api/logs')
def get_logs():
    captured_output = app.config.get('CAPTURED_OUTPUT')
    if captured_output:
        return jsonify(logs=captured_output.get_output())
    return jsonify(logs="Log capture not initialized."), 500

# New API endpoint for GUI to send commands (simplified for now)
@app.route('/api/terminal_input', methods=['POST'])
def terminal_input_handler():
    data = request.get_json()
    text_input = data.get('text', '').strip()

    if not text_input:
        return jsonify({"success": False, "error": "No text provided"}), 400

    expression_to_set = global_state['expression'] # Default to current expression
    subtitle_to_set = ""

    if text_input in allowed_expressions:
        expression_to_set = text_input
    else:
        subtitle_to_set = text_input

    try:
        with open(COMMAND_FILE, 'w') as f:
            json.dump({'expression': expression_to_set, 'subtitle': subtitle_to_set}, f)
        return jsonify({"success": True, "message": f"Command '{text_input}' processed."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# New API endpoint for GUI to send commands (simplified for now)
@app.route('/api/update_from_gui', methods=['POST'])
def update_from_gui():
    data = request.get_json()
    expression = data.get('expression')
    subtitle = data.get('subtitle', "")

    if expression and expression in allowed_expressions:
        try:
            with open(COMMAND_FILE, 'w') as f:
                json.dump({'expression': expression, 'subtitle': subtitle}, f)
            return jsonify({"success": True, "message": f"Command '{expression}' sent."})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500
    return jsonify({"success": False, "error": "Invalid expression"}), 400

# --- Main Execution ---
watcher_thread = threading.Thread(target=watch_command_file, daemon=True)
watcher_thread.start()
