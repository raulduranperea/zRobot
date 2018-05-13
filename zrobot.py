from sensors import Sensor
from sensors import Sensors
from wheels import Wheel
from wheels import MockWheel
from wheels import Wheels
import RPi.GPIO as GPIO
from runtime import Runtime
from processor import Processor

GPIO.setmode(GPIO.BOARD)

sensor1 = Sensor(11, 13)
sensor3 = Sensor(15, 16)
sensor5 = Sensor(18, 19)
sensor6 = Sensor(21, 22)
sensor8 = Sensor(23, 24)
sensor10 = Sensor(26, 29)

leftMotor = Wheel(3, 5, 7, 7)
rightMotor = Wheel(8, 10, 12, 1)
# rightMotor = MockWheel("rightWheel")

zrobot_runtime = Runtime(Sensors([sensor1, sensor3, sensor5, sensor6, sensor8, sensor10]),
                         Processor(),
                         Wheels(leftMotor, rightMotor))
zrobot_runtime.start()
