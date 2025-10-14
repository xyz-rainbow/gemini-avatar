import os
import time
import threading
import random
import json
from flask import Flask, jsonify, send_from_directory, request

# --- Path Configuration ---
backend_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(backend_dir, '..', 'frontend')
COMMAND_FILE = os.path.join(backend_dir, 'command.txt')

# --- App Configuration ---
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')

# --- State Management ---
global_state = {
    "expression": "neutral",
    "subtitle": "This is a test subtitle."
}
last_manual_command_time = time.time()

# All allowed expressions based on available videos
allowed_expressions = [
    "neutral", "orgullosa", "angry", "annoyed", "idle1", "idle2", "idle3", "idle4",
    "nervous", "sad", "sleepy", "happy", "thinking", "talking", "wink", "idea",
    "idea2", "curious", "excited"
]

# Sample subtitles for idle mode
sample_subtitles = [
    "Hmm...",
    "¿Qué debería hacer ahora?",
    "Tengo hambre.",
    "Esto es interesante.",
    "...",
    "Zzz...",
    "¡Ah!",
    "¿Has visto mi última actualización?",
    "Me pregunto qué estará pensando."
]

# --- Idle Mode Logic ---
def manage_idle_state():
    global last_manual_command_time
    
    idle_expressions = [e for e in allowed_expressions if e.startswith('idle')]

    last_short_idle_change = time.time()
    last_long_idle_change = time.time()
    last_subtitle_change = time.time()

    next_short_idle_interval = random.randint(4, 10)
    long_idle_interval = 40
    next_subtitle_interval = random.randint(5, 18)

    while True:
        time.sleep(1) # Main loop runs once per second

        # If a manual command was issued recently, pause idle mode
        if time.time() - last_manual_command_time < long_idle_interval:
            continue

        # --- Expression Change Logic ---
        # Prioritize long-term changes over short-term ones
        if time.time() - last_long_idle_change > long_idle_interval:
            new_expression = random.choice(allowed_expressions)
            global_state['expression'] = new_expression
            print(f"[IDLE-LONG] New expression: {new_expression}")
            
            # Reset both timers
            last_long_idle_change = time.time()
            last_short_idle_change = time.time()
            next_short_idle_interval = random.randint(4, 10)

        elif time.time() - last_short_idle_change > next_short_idle_interval:
            if idle_expressions:
                new_expression = random.choice(idle_expressions)
                if global_state['expression'] != new_expression:
                    global_state['expression'] = new_expression
                    global_state['subtitle'] = "" # Clear subtitle on minor idle change
                    print(f"[IDLE-SHORT] New expression: {new_expression}")
            
            last_short_idle_change = time.time()
            next_short_idle_interval = random.randint(4, 10)

        # --- Subtitle Change Logic (Independent) ---
        if time.time() - last_subtitle_change > next_subtitle_interval:
            # 60% chance of showing a subtitle, 40% chance of clearing it
            if random.random() < 0.6 and sample_subtitles:
                new_subtitle = random.choice(sample_subtitles)
                global_state['subtitle'] = new_subtitle
                print(f"[IDLE-SUB] New subtitle: {new_subtitle}")
            else:
                global_state['subtitle'] = ""
                print("[IDLE-SUB] Cleared subtitle")

            last_subtitle_change = time.time()
            next_subtitle_interval = random.randint(5, 18)

# --- Command Processing Logic ---
def watch_command_file():
    global last_manual_command_time
    print("--- Command file watcher started ---")
    while True:
        try:
            if os.path.exists(COMMAND_FILE):
                with open(COMMAND_FILE, 'r') as f:
                    command_data = f.read().strip()
                
                os.remove(COMMAND_FILE)

                command = None
                subtitle = ""

                try:
                    cmd_obj = json.loads(command_data)
                    command = cmd_obj.get('expression')
                    subtitle = cmd_obj.get('subtitle', "")
                except json.JSONDecodeError:
                    command = command_data
                    subtitle = ""

                if command in allowed_expressions:
                    global_state['expression'] = command
                    global_state['subtitle'] = subtitle
                    last_manual_command_time = time.time() # Update timestamp on manual command
                    print(f"[MANUAL] State updated: {global_state}")
                else:
                    print(f"Warning: Received invalid command '{command}' from file. Ignoring.")
            
        except Exception as e:
            print(f"Error in command watcher: {e}")
        
        time.sleep(0.5)

# --- API & Frontend Routes ---
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify(global_state)

@app.route('/settings')
def settings_panel():
    return send_from_directory(app.static_folder, 'settings.html')

@app.route('/api/logs')
def get_logs():
    captured_output = app.config.get('CAPTURED_OUTPUT')
    if captured_output:
        return jsonify(logs=captured_output.get_output())
    return jsonify(logs="Log capture not initialized."), 500

@app.route('/api/terminal_input', methods=['POST'])
def terminal_input_handler():
    data = request.get_json()
    text_input = data.get('text', '').strip()

    if not text_input:
        return jsonify({"success": False, "error": "No text provided"}), 400

    expression_to_set = global_state['expression']
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
# Start the thread that watches for manual commands
command_watcher_thread = threading.Thread(target=watch_command_file, daemon=True)
command_watcher_thread.start()

# Start the thread that manages idle state changes
idle_manager_thread = threading.Thread(target=manage_idle_state, daemon=True)
idle_manager_thread.start()
