from flask import Flask, request, render_template

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


def set_power(power):
    power = int(power)
    try:
        #p.ChangeDutyCycle(power)
        print(power)
    except KeyboardInterrupt:
        pass
        #p.stop()


def set_light(light):
    print(light)


def set_horn(horn):
    print(horn)


# todo play sound when charged


def handle_request(request):
    set_power(request['power'])
    set_light(request['light'])
    set_horn(request['horn'])


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
