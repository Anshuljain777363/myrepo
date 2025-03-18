from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get server time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Get 'top' command output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    # HTML response
    response = f"""
    <html>
    <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> Anshul Jain</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
