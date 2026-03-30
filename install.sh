#!/bin/bash
# XYZ Rainbow Technology - Makima Avatar Installer
echo "🌹 Gemini Avatar (Makima) Setup"

read -p "Do you want to use the Interactive Installer? (y/n): " choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    python3 interactive_install.py
else
    echo "--- Standard Installation ---"
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✅ Standard installation complete!"
fi
