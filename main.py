import flask
import time
import remote
from flask import Flask, render_template, jsonify, request
from take_photo import take_photo
from random import randint
app = Flask(__name__)

@app.route('/')
def home():
    rand_string = str(randint(1, 1e9))
    return render_template('index.html', rand_string=rand_string)

@app.route('/take_photo', methods=['POST'])
def photo():
    photo_file = '/home/pi/MobileAC2/static/test.jpg'
    take_photo(photo_file)
    #return jsonify(photo_file=photo_file)
    return flask.redirect(flask.url_for('home'))

@app.route('/send_command', methods=['POST'])
def send_command():
    r = remote.get_connection()
    cmd = str(request.form.get('command', ''))
    print(cmd, len(cmd))
    remote.send_command(r, cmd)
    photo_file = '/home/pi/static/test.jpg'
    take_photo(photo_file)
    return flask.redirect(flask.url_for('home'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
