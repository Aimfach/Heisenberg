from flask import Flask, request, render_template

# raspberry pi
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

print("hi")
p = GPIO.PWM(23, 1000)
g = GPIO.PWM(24, 1000)
u = GPIO.PWM(26, 1000)
a = GPIO.PWM(12, 1000)
i = GPIO.PWM(17, 1000)
p.start(0)
g.start(0)
u.start(0)
a.start(0)
i.start(0)






def set_power(power):
    power = int(power)
    try:
        p.ChangeDutyCycle(power)
        g.ChangeDutyCycle(power/2)
        u.ChangeDutyCycle(power-10)
        a.ChangeDutyCycle(power-30)
        i.ChangeDutyCycle(power/3)
        print(power)                
    except KeyboardInterrupt:
        pass
        p.stop()
        g.stop()
        u.stop()
        a.stop()
        i.stop()
        GPIO.cleanup()
    

def set_light(light):
    print(light)


def set_horn(horn):
    print(horn)
#todo play sound when charged

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

