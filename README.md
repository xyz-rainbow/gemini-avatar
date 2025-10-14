# Gemini Avatar

An interactive animated avatar application with personality, featuring multiple expressions, idle animations, and a chat interface. Built with Flask backend and pywebview for a native desktop experience.

![Gemini Avatar](frontend/Makima.webp)

## Features

- **Animated Avatar**: 19 different expressions and idle animations
- **Interactive Control Panel**: Real-time control of avatar expressions and subtitles
- **Intelligent Idle System**: Avatar automatically cycles through idle animations and displays random thoughts
- **Chat Interface**: Send messages to the avatar and receive animated responses
- **External Command Support**: Control the avatar programmatically via command files or API
- **Native Desktop App**: Built with pywebview for a seamless desktop experience
- **Frameless Window**: Transparent, always-on-top avatar window

## Available Expressions

The avatar supports the following expressions:

**Emotional States:**
- `neutral` - Default neutral expression
- `happy` - Happy/joyful expression
- `sad` - Sad expression
- `angry` - Angry expression
- `annoyed` - Slightly annoyed
- `excited` - Excited expression
- `nervous` - Nervous/anxious
- `sleepy` - Tired/sleepy

**Actions:**
- `talking` - Speaking animation
- `thinking` - Thinking/pondering
- `curious` - Curious/interested
- `wink` - Winking gesture
- `orgullosa` - Proud/confident

**Ideas:**
- `idea` - Having an idea
- `idea2` - Alternative idea animation

**Idle Animations:**
- `idle1`, `idle2`, `idle3`, `idle4` - Various idle state animations

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xyz-rainbow/gemini-avatar.git
   cd gemini-avatar
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask (web framework)
   - pywebview (desktop GUI)

## Usage

### Starting the Application

**Method 1: Direct Python execution**
```bash
python run.py
```

**Method 2: Hidden startup (Windows)**
```bash
start_hidden.bat
```

The application will:
1. Start a Flask server on `http://127.0.0.1:5000`
2. Open the main avatar window (frameless, always-on-top)
3. Wait for interactions

### Controlling the Avatar

**1. Using the Control Panel**
- Right-click on the avatar window to open the control panel
- Select expressions from the dropdown menu
- Add custom subtitles
- Send commands to the avatar

**2. Using the Command Line**
```bash
python send_command.py <expression> [subtitle]
```

Examples:
```bash
python send_command.py happy "Hello there!"
python send_command.py thinking
python send_command.py excited "I have an idea!"
```

**3. Using the Chat Interface**
- Type messages in the control panel chat
- The avatar will respond with appropriate expressions and subtitles

**4. Using the API**

Send POST requests to control the avatar:
```bash
curl -X POST http://127.0.0.1:5000/api/update_from_gui \
  -H "Content-Type: application/json" \
  -d '{"expression": "happy", "subtitle": "Hello!"}'
```

## Project Structure

```
gemini-avatar/
├── backend/
│   ├── app.py              # Flask application with API endpoints
│   └── command.txt         # Command file (auto-generated)
├── frontend/
│   ├── index.html          # Main avatar display
│   ├── control.html        # Control panel interface
│   ├── settings.html       # Settings panel
│   ├── script.js           # Avatar display logic
│   ├── control.js          # Control panel logic
│   ├── settings.js         # Settings logic
│   ├── style.css           # Main styling
│   ├── settings.css        # Settings styling
│   ├── Makima.webp         # Avatar thumbnail
│   └── avatar/             # Video files for expressions
│       ├── makima_neutral.mp4
│       ├── makima_happy.mp4
│       └── ... (19 expression videos)
├── run.py                  # Main application entry point
├── send_command.py         # Command-line tool for controlling avatar
├── start_hidden.bat        # Windows hidden startup script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## API Endpoints

### GET Endpoints

- `GET /` - Main avatar interface
- `GET /control` - Control panel interface
- `GET /settings` - Settings panel interface
- `GET /api/state` - Get current avatar state (expression and subtitle)
- `GET /api/logs` - Get application logs

### POST Endpoints

- `POST /api/update_from_gui` - Update avatar expression and subtitle
  ```json
  {
    "expression": "happy",
    "subtitle": "Hello there!"
  }
  ```

- `POST /api/terminal_input` - Send command via terminal input
  ```json
  {
    "text": "happy Hello!"
  }
  ```

- `POST /api/chat` - Send chat message and get response sequence
  ```json
  {
    "message": "Hello avatar!"
  }
  ```

## Idle Mode

The avatar features an intelligent idle system that activates after 7 seconds of inactivity:

- **Short Idle Changes**: Cycles through idle animations every 4-10 seconds
- **Long Idle Changes**: Major expression changes every 40 seconds
- **Random Thoughts**: Displays random subtitles or emotional events
- **Emotional Events**: Occasionally triggers special events with matching expressions

## Customization

### Adding New Expressions

1. Add a new video file to `frontend/avatar/` (e.g., `makima_custom.mp4`)
2. Add the expression name (without `makima_` prefix) to `allowed_expressions` in `backend/app.py`:
   ```python
   allowed_expressions = [
       "neutral", "happy", ..., "custom"
   ]
   ```

### Modifying Idle Behavior

Edit the following variables in `backend/app.py`:
- `inactivity_delay` - Time before idle mode starts
- `long_idle_interval` - Time between major expression changes
- `sample_subtitles` - List of random thought subtitles
- `emotional_events` - List of special event tuples (subtitle, expression)

## Troubleshooting

**Avatar window doesn't appear:**
- Ensure Flask server started successfully
- Check if port 5000 is available
- Wait 1-2 seconds after starting the application

**Videos don't play:**
- Verify all video files exist in `frontend/avatar/`
- Check video file format compatibility (MP4 recommended)
- Ensure proper file naming convention (`makima_<expression>.mp4`)

**Control panel doesn't connect:**
- Verify Flask server is running on port 5000
- Check firewall settings
- Try accessing `http://127.0.0.1:5000/control` in a browser

## Development

To run in development mode with debug output:
```python
# In backend/app.py, modify the run command
app.run(host='127.0.0.1', port=5000, debug=True)
```

## License

This project is open source. Please check the repository for license details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add new expressions or animations

## Acknowledgments

- Avatar character and animations
- Flask framework
- pywebview library

---

**Note**: This application is designed for personal use and entertainment. Enjoy your interactive avatar companion!
