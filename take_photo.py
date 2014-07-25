from time import sleep, strftime
from picamera import PiCamera as Cam

def take_photo(filename='/home/pi/test.jpg'):
    with Cam() as c:
        c.resolution = (320, 240)
        c.start_preview()
        sleep(2)
        c.capture(filename)

def take_unique_photo():
    filename = '/home/pi/%s.jpg' % strftime('%Y%m%d_%H%M%S') 
    take_photo(filename)

def take_sequence(lower=59, upper=65):
    base = '/home/pi/sequence/%d.jpg'
    with Cam() as c:
        c.start_preview()
        sleep(2)
        for i in range(lower, upper):
            filename = base % i
            print(i)
            sleep(1)
            c.capture(filename)

if __name__ == '__main__':
    take_photo()
