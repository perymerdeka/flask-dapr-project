from flask import Blueprint, jsonify

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates/dashboard")


@dashboard_blueprint.route("/")
def index():
    message = {"message": "hello world"}
    return jsonify(message)