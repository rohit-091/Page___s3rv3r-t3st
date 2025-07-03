from flask import Flask, render_template, request, jsonify
import subprocess
import os
import json

app = Flask(__name__)

# Write content to file
def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Save form data
@app.route("/save", methods=["POST"])
def save():
    data = request.json
    write_to_file("token.txt", data.get("token", ""))
    write_to_file("convo.txt", data.get("convo", ""))
    write_to_file("message.txt", data.get("message", ""))
    write_to_file("time.txt", data.get("time", ""))
    write_to_file("name.txt", data.get("name", ""))
    write_to_file("file.txt", data.get("file", ""))
    return "✅ Data saved"

# Toggle server on/off
@app.route("/toggle", methods=["POST"])
def toggle():
    status = request.json.get("status")
    with open("status.json", "w") as f:
        json.dump({"status": status}, f)

    if status == "on":
        subprocess.Popen(["python3", "original_script.py"])
        return "🟢 Server Started"
    else:
        subprocess.call(["pkill", "-f", "original_script.py"])
        return "🔴 Server Stopped"

# Get current status
@app.route("/status")
def status():
    if not os.path.exists("status.json"):
        return jsonify({"status": "off"})
    with open("status.json") as f:
        return jsonify(json.load(f))

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
