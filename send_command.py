import sys
import os
import json

COMMAND_FILE = os.path.join(os.path.dirname(__file__), 'backend', 'command.txt')

def send_command(expression, subtitle=""):
    try:
        with open(COMMAND_FILE, 'w') as f:
            json.dump({'expression': expression, 'subtitle': subtitle}, f)
        print(f"Successfully sent command: {expression} with subtitle: {subtitle}")
    except Exception as e:
        print(f"Error writing to command file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression_to_send = sys.argv[1]
        subtitle_to_send = sys.argv[2] if len(sys.argv) > 2 else ""
        send_command(expression_to_send, subtitle_to_send)
    else:
        print("Usage: python send_command.py <expression> [subtitle]", file=sys.stderr)
        sys.exit(1)