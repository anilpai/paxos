from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import hashlib

app = Flask(__name__)
api = Api(app)

MESSAGES = {}


def abort_if_hash_doesnt_exist(hsh):
    if hsh not in MESSAGES.values():
        abort(404, err_msg="Message not found")


def get_msg_for_hsh(hsh):
    for k, v in MESSAGES.items():
        if v == hsh:
            return k


parser = reqparse.RequestParser()
parser.add_argument('message')


# Message resource lets you get the actual message for hash provided and lets you generate hash for any message.

class Message(Resource):
    def get(self, hsh):
        abort_if_hash_doesnt_exist(hsh)
        msg = get_msg_for_hsh(hsh)
        response = {'message': msg}
        return response

    def delete(self, hsh):
        abort_if_hash_doesnt_exist(hsh)
        msg = get_msg_for_hsh(hsh)
        del MESSAGES[msg]
        return '', 204

    def post(self):
        args = parser.parse_args()
        h = hashlib.new("sha256")
        h.update(args['message'].encode('utf-8'))
        hsh = h.hexdigest()
        MESSAGES[args['message']] = hsh
        response = {'digest': hsh}
        return response, 201

    def put(self, hsh):
        pass


api.add_resource(Message,
                 '/messages',
                 '/messages/<string:hsh>')


if __name__ == '__main__':
    app.run()