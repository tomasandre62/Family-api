from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)


jackson_family = FamilyStructure('Jackson')


jackson_family.add_member({"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]})
jackson_family.add_member({"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]})
jackson_family.add_member({"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]})


@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def get_or_delete_member(member_id):
    if request.method == 'GET':
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"message": "Miembro no encontrado"}), 404
    elif request.method == 'DELETE':
        jackson_family.delete_member(member_id)
        return jsonify({"Eliminado": True}), 200

@app.route('/members', methods=['POST'])
def add_member():
    member = request.get_json()
    jackson_family.add_member(member)
    return jsonify(member), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)