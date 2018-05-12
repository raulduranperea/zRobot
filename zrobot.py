from sensors import Sensor
from sensors import Sensors
from wheels import Wheel
from wheels import MockWheel
from wheels import Wheels
import RPi.GPIO as GPIO
from runtime import Runtime


GPIO.setmode(GPIO.BOARD)

sensor1 = Sensor(11, 13)
# sensor2 = Sensor()
sensor3 = Sensor(15, 16)
# sensor4 = Sensor()
sensor5 = Sensor(18, 19)
sensor6 = Sensor(21, 22)
# sensor7 = Sensor()
sensor8 = Sensor(23, 24)
# sensor9 = Sensor()
sensor10 = Sensor(26, 29)

zrobot_sensors = Sensors([sensor1, sensor3, sensor5, sensor6, sensor8, sensor10])
leftMotor = MockWheel("leftMotor")
rightMotor = MockWheel("rightMotor")
zrobot_wheels = Wheels(leftMotor, rightMotor)

zrobot_processor = None
zrobot_runtime = Runtime(zrobot_sensors, zrobot_processor, zrobot_wheels)
zrobot_runtime.start()
