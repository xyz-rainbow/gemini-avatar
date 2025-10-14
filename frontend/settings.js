document.addEventListener('DOMContentLoaded', () => {
    const logOutput = document.getElementById('log-output');
    const openControlPanelButton = document.getElementById('open-control-panel-settings');
    const quitAppButton = document.getElementById('quit-app');

    async function fetchLogs() {
        try {
            const response = await fetch('/api/logs');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            logOutput.textContent = data.logs;
            logOutput.scrollTop = logOutput.scrollHeight; // Auto-scroll to bottom
        } catch (error) {
            console.error('Error fetching logs:', error);
            logOutput.textContent = 'Error loading logs.';
        }
    }

    // Fetch logs every 1 second
    setInterval(fetchLogs, 1000);
    fetchLogs(); // Initial fetch

    // Open Control Panel button
    if (openControlPanelButton) {
        openControlPanelButton.addEventListener('click', () => {
            window.open('http://127.0.0.1:5000/control', '_blank');
        });
    }

    // Quit Application button
    if (quitAppButton) {
        quitAppButton.addEventListener('click', () => {
            if (confirm('Are you sure you want to quit the application?')) {
                window.pywebview.api.quit_app();
            }
        });
    }
});