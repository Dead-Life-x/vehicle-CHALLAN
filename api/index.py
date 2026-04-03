from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if "api/challan" in path:
        vehicle = request.args.get("vehicle_number")
        return jsonify({
            "vehicle": vehicle,
            "status": "working 🚀"
        })
    
    return "API Running 🚀"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
