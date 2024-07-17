from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))
    @classmethod
    def respond_with_error(cls, data, status=400):
        return make_response(jsonify(data=data), status)