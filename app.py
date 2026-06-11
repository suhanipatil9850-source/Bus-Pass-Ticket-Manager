from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
passes = []


def find_pass(pass_id):
    return next((p for p in passes if p["id"] == pass_id), None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/passes", methods=["GET"])
def list_passes():
    return jsonify(passes)


@app.route("/passes", methods=["POST"])
def create_pass():
    data = request.get_json() or {}
    pass_id = data.get("id")
    name = data.get("name")
    route = data.get("route")
    validity = data.get("validity")

    if not pass_id or not name or not route or not validity:
        return jsonify({"error": "All fields are required."}), 400

    if find_pass(pass_id):
        return jsonify({"error": "Pass ID already exists."}), 400

    new_pass = {"id": pass_id, "name": name, "route": route, "validity": validity}
    passes.append(new_pass)
    return jsonify(new_pass), 201


@app.route("/passes/<pass_id>", methods=["GET"])
def get_pass(pass_id):
    p = find_pass(pass_id)
    if not p:
        return jsonify({"error": "Pass not found."}), 404
    return jsonify(p)


@app.route("/passes/<pass_id>/renew", methods=["PUT"])
def renew_pass(pass_id):
    data = request.get_json() or {}
    validity = data.get("validity")
    p = find_pass(pass_id)
    if not p:
        return jsonify({"error": "Pass not found."}), 404
    if not validity:
        return jsonify({"error": "New validity is required."}), 400
    p["validity"] = validity
    return jsonify(p)


@app.route("/passes/<pass_id>", methods=["DELETE"])
def delete_pass(pass_id):
    p = find_pass(pass_id)
    if not p:
        return jsonify({"error": "Pass not found."}), 404
    passes.remove(p)
    return jsonify({"message": "Pass deleted successfully."})


if __name__ == "__main__":
    app.run(debug=True)
