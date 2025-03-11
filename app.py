from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def system_info():
    name = "Veeresh B S" 
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except FileNotFoundError:
        top_output = "Error: 'top' command not found."

    return f"""<h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time:</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
