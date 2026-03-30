import os
import sys
import subprocess
import webbrowser
import platform
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt, default=""):
    value = input(f"{prompt} [{default}]: ").strip()
    return value if value else default

def run_command(cmd, cwd=None):
    try:
        subprocess.check_call(cmd, shell=True, cwd=cwd)
        return True
    except Exception as e:
        print(f"❌ Error executing: {cmd}\nDetails: {e}")
        return False

def main():
    clear_screen()
    print("🌹 XYZ Rainbow Technology - Makima Avatar Interactive Installer")
    print("===============================================================")
    
    # 1. Detection
    current_os = platform.system()
    print(f"Detected OS: {current_os}")

    # 2. Choose path
    default_path = os.getcwd()
    install_path = get_input("Where do you want to install the app?", default_path)
    install_path = os.path.abspath(install_path)
    
    if not os.path.exists(install_path):
        os.makedirs(install_path)
        print(f"Created directory: {install_path}")

    # Move files if necessary
    source_dir = os.getcwd()
    if install_path != source_dir:
        print(f"Moving files to {install_path}...")
        for item in os.listdir(source_dir):
            if item != "venv" and not item.startswith("."): # Skip venv and hidden
                s = os.path.join(source_dir, item)
                d = os.path.join(install_path, item)
                if os.path.isdir(s):
                    if os.path.exists(d): shutil.rmtree(d)
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)

    # 3. Choose command alias
    command_name = get_input("What command name do you want to use to launch the app?", "makima")

    # 4. Install Dependencies
    print("\n--- Setting up Virtual Environment & Dependencies ---")
    os.chdir(install_path)
    
    python_exe = sys.executable
    venv_cmd = f'"{python_exe}" -m venv venv'
    run_command(venv_cmd)

    if os.name == 'nt':
        pip_path = os.path.join("venv", "Scripts", "pip")
        launcher_path = os.path.join("venv", "Scripts", "python")
    else:
        pip_path = os.path.join("venv", "bin", "pip")
        launcher_path = os.path.join("venv", "bin", "python")

    run_command(f'"{pip_path}" install --upgrade pip')
    run_command(f'"{pip_path}" install -r requirements.txt')

    # 5. Create Launch Script / Alias
    print(f"\n--- Creating Launcher: {command_name} ---")
    if os.name == 'nt':
        with open(f"{command_name}.bat", "w") as f:
            f.write(f'@echo off\nstart "" "{launcher_path}" run.py')
        print(f"Created {command_name}.bat")
    else:
        # Bash alias instruction
        shell_rc = os.path.expanduser("~/.bashrc") if os.path.exists(os.path.expanduser("~/.bashrc")) else os.path.expanduser("~/.zshrc")
        alias_line = f"alias {command_name}='cd {install_path} && export DISPLAY=:0 && nohup {launcher_path} run.py > /dev/null 2>&1 &'\n"
        print(f"👉 To use '{command_name}', add this line to your shell config ({shell_rc}):")
        print(f"   {alias_line}")

    # 6. Post-install actions
    print("\n" + "="*30)
    open_github = get_input("Do you want to open the GitHub repository page?", "Y").lower()
    if open_github == 'y':
        webbrowser.open("https://github.com/xyz-rainbow/gemini-avatar")

    launch_now = get_input("Do you want to launch Makima now?", "Y").lower()
    if launch_now == 'y':
        print("🚀 Launching...")
        if os.name == 'nt':
            subprocess.Popen([f"{command_name}.bat"])
        else:
            subprocess.Popen([launcher_path, "run.py"], env={{**os.environ, "DISPLAY": ":0"}})

    print("\n✅ Installation Process Finished! Welcome to XYZ Rainbow Technology.")

if __name__ == "__main__":
    main()
