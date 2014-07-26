import flask
import time
import remote
from flask import Flask, render_template, jsonify, request
from take_photo import take_photo
from random import randint
from hashlib import sha1
app = Flask(__name__)

PHOTO_FILE = '/home/pi/MobileAC2/static/test.jpg'

#class remote(object):
#    @classmethod
#    def send_command(cls, r, cmd):
#        print(cmd)

@app.route('/')
def home():
    rand_string = str(randint(1, 1e9))
    take_photo(PHOTO_FILE)
    #return jsonify(photo_file=photo_file)
    return render_template('index.html', rand_string=rand_string)


@app.route('/send_command', methods=['POST'])
def send_command():
    toggle_power = str(request.form.get('power', 'off'))
    temperature = int(request.form.get('temperature', 0))
    fan = int(request.form.get('fan', 0))
    coolness = str(request.form.get('coolness', 'no'))
    password = str(request.form.get('password'))
    print('toggle power', toggle_power)
    print('temperature', temperature)
    print('fan speed', fan)
    print('coolness', coolness)
    print('password', password)
    if open('password.txt').read() == sha1(password).digest():
        send_commands(toggle_power, temperature, fan, coolness)
    else:
        print("passwords don't match")
    return flask.redirect(flask.url_for('home'))


def send_commands(toggle_power, temperature, fan, coolness):
    r = remote.get_connection()
#    r = 1
    if toggle_power == 'on':
        remote.send_command(r, 'p')
    if temperature < 0:
        for i in range(abs(temperature)):
            remote.send_command(r, 'd')
    elif temperature > 0:
        for i in range(temperature):
            remote.send_command(r, 'u')
    if fan < 0:
        for i in range(fan):
            remote.send_command(r, 'l')
    elif fan > 0:
        for i in range(fan):
            remote.send_command(r, 'r')
    if coolness == 'cool':
        remote.send_command(r, 'c')
    elif coolness == 'energy':
        remote.send_command(r, 'r')
    elif coolness == 'fan':
        remote.send_command(r, 'f')


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
