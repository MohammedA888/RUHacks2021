from gpiozero import Motor
import time

wrist = Motor(11,12)
mill = Motor(13,15)

wrist.stop()
mill.stop()

def stop():
    wrist.stop()
    mill.stop()