from flask import Flask, request, jsonify, send_file, send_from_directory
import os
import time
from generate_image import generate_image

app = Flask(__name__, static_folder="ui", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("ui", "index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    title = data.get("title", "收视冠军")
    date = data.get("date", "2月9日～2月15日")
    
    # Generate unique filename to avoid browser caching issues and allow concurrent users (locally)
    timestamp = int(time.time())
    output_filename = f"generated_{timestamp}.jpg"
    output_path = os.path.join(os.getcwd(), "ui", output_filename)
    
    # Ensure ui directory exists
    os.makedirs(os.path.join(os.getcwd(), "ui"), exist_ok=True)
    
    # Call the generator logic, disable auto_open since it's via web
    try:
        final_path = generate_image(title, date, output_path=output_path, auto_open=False)
        return jsonify({
            "success": True, 
            "image_url": output_filename,
            "message": "Image generated successfully"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Redbook Generator Server on http://0.0.0.0:5001")
    print("Use Ctrl+C to stop the server.")
    app.run(host="0.0.0.0", port=5001, debug=True)
