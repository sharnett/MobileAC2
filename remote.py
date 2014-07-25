import serial
import sys
from time import sleep

def get_connection():
    locations= ['/dev/tty.usbmodemfd121',
                '/dev/ttyACM0', 
                '/dev/tty.usbserial-A700dYwR']
    for device in locations:    
        try:    
            print "Trying...",device  
            robot = serial.Serial(device, 9600)   
            print "serial connected successfully"
            sleep(2)
            break  
        except:    
            print "Failed to connect on",device    
        robot = False
    return robot

def send_command(robot, cmd):
    try:    
        robot.write(cmd)    
        print "sent %s to the robot" % (cmd,)
    except:    
        print "Failed to send: %s" % (cmd,)
