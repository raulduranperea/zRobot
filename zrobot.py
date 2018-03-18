from sensors import Sensor
from sensors import Sensors
from wheels import Wheel
from wheels import Wheels
from runtime import Runtime


sensor1 = Sensor()
sensor2 = Sensor()
sensor3 = Sensor()
sensor4 = Sensor()
sensor5 = Sensor()
sensor6 = Sensor()
sensor7 = Sensor()
sensor8 = Sensor()
sensor9 = Sensor()
sensor10 = Sensor()

zrobot_sensors = Sensors([sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10])
leftMotor = Wheel()
rightMotor = Wheel()
zrobot_wheels = Wheels(leftMotor, rightMotor)

zrobot_processor = None
zrobot_runtime = Runtime(zrobot_sensors, zrobot_processor, zrobot_wheels)
zrobot_runtime.start()
