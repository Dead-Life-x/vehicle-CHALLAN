from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/challan", methods=["GET"])
def get_challan():
    vehicle = request.args.get("vehicle_number")

    if not vehicle:
        return jsonify({
            "error": "vehicle_number required"
        }), 400

    return jsonify({
        "vehicle": vehicle,
        "status": "working 🚀"
    })


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def home(path):
    return "API Running 🚀"
