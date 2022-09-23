from flask import Flask, request, render_template
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
import sys
sys.path.append('/path/to/ffmpeg')
from playsound import playsound
playsound('starting.mp3')
import subprocess


light_on = False
is_charging = False
# raspberry pi
import time


raspberry_pi = False
if (raspberry_pi):


    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)

    frequency = 1000


    # head left
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)

    # head right
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    headlight = [
        GPIO.PWM(2, frequency),
        GPIO.PWM(3, frequency),
        GPIO.PWM(4, frequency),
        GPIO.PWM(14, frequency),
        GPIO.PWM(15, frequency),
        GPIO.PWM(18, frequency)
    ]



    # backlight
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    backlight = [
        GPIO.PWM(17, frequency),
        GPIO.PWM(27, frequency),
        GPIO.PWM(22, frequency),
        GPIO.PWM(23, frequency),
        GPIO.PWM(24, frequency),
        GPIO.PWM(10, frequency),
        GPIO.PWM(9, frequency),
        GPIO.PWM(11, frequency)
    ]


    # motors
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    f_motor = GPIO.PWM(20, frequency)
    b_motor = GPIO.PWM(21, frequency)


def start(GPIO):
    GPIO.start(0)


    # headlight
    for i in range(len(headlight)):
        start(headlight[i])

    for j in range(len(backlight)):
        start(backlight[j])

    start(f_motor)
    start(b_motor)




def start_in_sec(sec, light):
    for i in range(100):
        #light.ChangeDutyCycle(i)
        #print(i)
        time.sleep(sec/100)


def stop_in_sec(sec, light):
    for i in range(100):
        light.ChangeDutyCycle(100-i)
        #print(100-i)
        time.sleep(sec/100)


def stop_lights():
    for i in range(len(headlight)):
        stop_in_sec(0.5, headlight[i])

    for i in range(len(backlight)):
        stop_in_sec(0.5, backlight[i])


def start_head():
    # start upper ones
    Thread(target=start_in_sec(1, "light1")).start()
    Thread(target=start_in_sec(1, "light4")).start()
    time.sleep(1)
    Thread(target=stop_in_sec(1, "light1")).start()
    Thread(target=stop_in_sec(1, "light4")).start()

    # second
    Thread(target=start_in_sec(1, "light2")).start()
    Thread(target=start_in_sec(1, "light5")).start()
    time.sleep(1)
    Thread(target=stop_in_sec(1, "light2")).start()
    Thread(target=stop_in_sec(1, "light5")).start()

    # third
    Thread(target=start_in_sec(1, "light3")).start()
    Thread(target=start_in_sec(1, "light6")).start()
    time.sleep(1)
    Thread(target=start_in_sec(1, "light2")).start()
    Thread(target=start_in_sec(1, "light5")).start()
    time.sleep(1)
    Thread(target=start_in_sec(1, "light1")).start()
    Thread(target=start_in_sec(1, "light4")).start()


def start_back():
    Thread(target=start_in_sec(1, "light4")).start()
    Thread(target=start_in_sec(1, "light5")).start()
    time.sleep(1)
    Thread(target=stop_in_sec(1, "light4")).start()
    Thread(target=stop_in_sec(1, "light5")).start()

    Thread(target=start_in_sec(1, "light3")).start()
    Thread(target=start_in_sec(1, "light6")).start()
    time.sleep(1)
    Thread(target=stop_in_sec(1, "light3")).start()
    Thread(target=stop_in_sec(1, "light6")).start()

    Thread(target=start_in_sec(1, "light2")).start()
    Thread(target=start_in_sec(1, "light7")).start()
    time.sleep(1)
    Thread(target=stop_in_sec(1, "light2")).start()
    Thread(target=stop_in_sec(1, "light7")).start()

    Thread(target=start_in_sec(1, "light1")).start()
    Thread(target=start_in_sec(1, "light8")).start()

    Thread(target=start_in_sec(1, "light2")).start()
    Thread(target=start_in_sec(1, "light7")).start()

    Thread(target=start_in_sec(1, "light3")).start()
    Thread(target=start_in_sec(1, "light6")).start()

    Thread(target=start_in_sec(1, "light4")).start()
    Thread(target=start_in_sec(1, "light5")).start()


def start_lights():
    Thread(target=start_head).start()
    Thread(target=start_back).start()


def set_power(power):
    power = int(power)
    try:
        #p.ChangeDutyCycle(power)
        print(power)
        if power == 100:
            playsound('winning.mp3')
            playsound('wii winner.mp3')



    except KeyboardInterrupt:
        pass
        #p.stop()


def set_light(light, light_on=False):
    #from main import light_on
    #light_on = False


    if light == "change" and not light_on:
        start_lights()
        light_on = True
    if light == "change" and light_on:
        stop_lights()
        light_on = False


def set_horn(horn):
    if horn == "on":
        playsound('horn.mp3')
        # pip3 install PyObjC
    print(horn)


def set_charge(charge, is_charging):
    print(charge)
    if charge == "charge" and not is_charging:
        playsound('charging.mp3')
        subprocess.run(["stopUSB.sh", "--input_file=input.txt"])
        is_charging = True
    if charge == "charge" and is_charging:
        subprocess.run(["startUSB.sh", "--input_file=input.txt"])
        is_charging = False


def handle_request(request):
    set_power(request['power'])
    set_light(request['light'], light_on)
    set_horn(request['horn'])
    set_charge(request['charge'], is_charging)


# server
app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
def handler():
    if request.method == 'POST':
        handle_request(request.form)
        return "ok"

    else:
        user = request.args.get('nm')
        return render_template('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", 8000)

# todo usb Port an aus
# todo wlan erstellen
# todo autostart
# todo den hintergrund
# todo enable led
# https://ios.gadgethacks.com/how-to/turn-any-website-into-full-screen-app-your-iphone-0384426/
