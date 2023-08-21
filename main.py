from flask import Flask, jsonify, Response, request
from data_base import *


app = Flask(__name__, template_folder='templates')


@app.route('/create_user', methods=['POST'])
def create_user():
    body_json_data = request.get_json()
    user_name = body_json_data['user_name']
    user_x = body_json_data['user_x']
    user_y = body_json_data['user_y']
    add_user_to_db(user_name, user_x, user_y)
    return Response(status=200)


@app.route('/find_neighbors')
def find_neighbors():
    body_json_data = request.json
    radius = body_json_data['choose_radius']
    count = body_json_data['choose_count']
    id = body_json_data['user_id']
    result = get_users_from_db(id, count, radius)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
    create_table()
