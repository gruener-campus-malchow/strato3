from picamera import PiCamera, Color
from time import sleep
from datetime import datetime


# init camera
camera = PiCamera()
def capture(now):
    try:
        camera.resolution = (3280, 2464)
        # less resolution but full sensor 1640x1232
        # full resolution: 3280x2464
    
        # off auto night nightpreview backlight spotlight sports snow beach verylong fixedfps antishake fireworks
        camera.exposure_mode = 'antishake'

        # off auto sunlight cloudy shade tungsten fluorescent incandescent flash horizon
        camera.awb_mode = 'horizon'

        # init subtitle
        camera.annotate_text_size = 50
        camera.annotate_background = Color('blue')
        camera.annotate_foreground = Color('yellow')

        date_time = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
        print('date: ' + date_time)
        camera.annotate_text = "EARTHCAM: " + date_time
        camera.capture('/home/pi/shots/earth_' + date_time + '.jpg')
    finally:
        camera.close
