import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

print("hi")
p = GPIO.PWM(23, 1000)
g = GPIO.PWM(24, 1000)
p.start(0)
g.start(0)
try:
    print("hi")
    while 1:
        print("hi")
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            time.sleep(0.01)
                    
except KeyboardInterrupt:
    pass
    p.stop()
    g.stop()
    GPIO.cleanup()
