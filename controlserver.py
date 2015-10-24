
from flask import Flask
from flask import Response
from flask import request
from flask import render_template
from flask import jsonify
from control import left, right
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance("", str):
        headers = ', '.join(x.upper() for x in headers)
    if isinstance("", str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
app = Flask(__name__)

@app.route('/')
@crossdomain(origin='*')
def hello_world():
	a = request.args.get('a', 0, type=int)
	if a==1:
		left()
		return jsonify(rotate="left")

	if a==0:
		right()
		return jsonify(rotate="right")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 4040,debug=True)
