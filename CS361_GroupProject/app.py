from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

records = {}

def check_auth():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return False
    return True


@app.route("/records", methods=["POST"])
def add_record():
    if not check_auth():
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    data = request.json

    record_id = str(uuid.uuid4())
    record = {
        "record_id": record_id,
        "user_id": data.get("user_id"),
        "entry_type": data.get("entry_type"),
        "field_name": data.get("field_name"),
        "value": data.get("value"),
        "timestamp": data.get("timestamp")
    }

    records[record_id] = record

    return jsonify({
        "success": True,
        "message": "Record created",
        "record": record
    }), 201


@app.route("/records/<record_id>", methods=["PUT"])
def edit_record(record_id):
    if not check_auth():
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    if record_id not in records:
        return jsonify({"success": False, "message": "Record not found"}), 404

    data = request.json
    records[record_id].update(data)

    return jsonify({
        "success": True,
        "message": "Record updated",
        "record": records[record_id]
    }), 200


@app.route("/records/<record_id>", methods=["DELETE"])
def delete_record(record_id):
    if not check_auth():
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    if record_id not in records:
        return jsonify({"success": False, "message": "Record not found"}), 404

    del records[record_id]

    return jsonify({
        "success": True,
        "message": "Record deleted",
        "deleted_record_id": record_id
    }), 200


if __name__ == "__main__":
    app.run(port=5004, debug=True)