const videoElement = document.getElementById('makima-avatar-video');
const subtitleBox = document.getElementById('subtitle-box');
const subtitleText = document.getElementById('subtitle-text');
const openControlPanelButton = document.getElementById('open-control-panel');
const openLogsPanelButton = document.getElementById('open-logs-panel'); // New button
const minimizeAvatarWindowButton = document.getElementById('minimize-avatar-window');
const closeAvatarWindowButton = document.getElementById('close-avatar-window');
const terminalInput = document.getElementById('terminal-input');
const terminalOutput = document.getElementById('terminal-output');
const terminalContainer = document.getElementById('terminal-container');

const API_URL = 'http://127.0.0.1:5000/api/state';
const TERMINAL_INPUT_API = 'http://127.0.0.1:5000/api/terminal_input';

// Map expressions to video filenames (restored to previous state)
const expressionVideos = {
    "neutral": "avatar/makima_neutral.mp4",
    "orgullosa": "avatar/makima_orgullosa.mp4",
    "angry": "avatar/makima_angry.mp4",
    "annoyed": "avatar/makima_annoyed.mp4",
    "idle1": "avatar/makima_idle1.mp4",
    "idle2": "avatar/makima_idle2.mp4",
    "idle3": "avatar/makima_idle3.mp4",
    "idle4": "avatar/makima_idle4.mp4",
    "nervous": "avatar/makima_nervous.mp4",
    "sad": "avatar/makima_sad.mp4",
    "sleepy": "avatar/makima_sleepy.mp4",
    "happy": "avatar/makima_happy.mp4", 
    "thinking": "avatar/makima_thinking.mp4", 
    "talking": "avatar/makima_talking.mp4", 
    "wink": "avatar/makima_wink.mp4", 
    "idea": "avatar/makima_idea.mp4", 
    "idea2": "avatar/makima_idea2.mp4",
    "curious": "avatar/makima_curious.mp4", 
    "excited": "avatar/makima_excited.mp4",
};

async function updateAvatarState() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const state = await response.json();
        const expression = state.expression || 'neutral';
        const subtitle = state.subtitle || '';

        // Update video source if expression changes
        const newVideoFilename = expressionVideos[expression] || expressionVideos["neutral"];
        const newVideoFullUrl = videoElement.baseURI + newVideoFilename; // Construct full URL for comparison

        if (videoElement.currentSrc !== newVideoFullUrl) {
            videoElement.src = newVideoFilename; // Set src directly on video element
            videoElement.load(); // Reload the video
            videoElement.play(); // Start playing
            videoElement.loop = true; // Ensure it loops indefinitely
        }

        // Update subtitle
        if (subtitle) {
            subtitleText.textContent = subtitle;
            subtitleBox.classList.add('show');
        } else {
            subtitleText.textContent = '';
            subtitleBox.classList.remove('show');
        }

    } catch (error) {
        console.error('Failed to fetch avatar state:', error);
    }
}

// Event listener for the control panel button
if (openControlPanelButton) {
    openControlPanelButton.addEventListener('click', () => {
        window.open('http://127.0.0.1:5000/control', '_blank');
    });
}

// Event listener for the new Logs panel button
if (openLogsPanelButton) {
    openLogsPanelButton.addEventListener('click', () => {
        terminalContainer.classList.toggle('visible');
    });
}

// Event listeners for window control buttons
if (minimizeAvatarWindowButton) {
    minimizeAvatarWindowButton.addEventListener('click', () => {
        window.pywebview.api.minimize_avatar_window();
    });
}
if (closeAvatarWindowButton) {
    closeAvatarWindowButton.addEventListener('click', () => {
        window.pywebview.api.close_avatar_window();
    });
}

// Event listener for terminal input
if (terminalInput) {
    terminalInput.addEventListener('keypress', async (e) => {
        if (e.key === 'Enter') {
            const inputText = terminalInput.value.trim();
            terminalInput.value = ''; // Clear input

            if (inputText) {
                // Add to output (optional, for history)
                const outputLine = document.createElement('div');
                outputLine.textContent = `> ${inputText}`;
                terminalOutput.appendChild(outputLine);
                terminalOutput.scrollTop = terminalOutput.scrollHeight; // Scroll to bottom

                // Limit to 3 lines
                while (terminalOutput.children.length > 3) {
                    terminalOutput.removeChild(terminalOutput.children[0]);
                }

                // Send to backend
                try {
                    const response = await fetch(TERMINAL_INPUT_API, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: inputText }),
                    });
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    const data = await response.json();
                    console.log('Terminal input response:', data);
                } catch (error) {
                    console.error('Error sending terminal input:', error);
                }
            }
        }
    });
}

// Update state every 2 seconds
setInterval(updateAvatarState, 2000);

// Initial update
updateAvatarState();