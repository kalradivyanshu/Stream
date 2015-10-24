
from flask import Flask
from flask import Response
from flask import request
from flask import render_template
from flask import jsonify
from camera2 import getframe
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
def gen():
	while True:
		frame = getframe()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/frame',methods=['GET'])
def frame():
	return Response(gen(),	mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
