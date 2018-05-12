import RPi.GPIO as GPIO
import runtime
import wiringpi


class Wheels:
    left_wheel = None
    right_wheel = None

    def __init__(self, left_wheel, right_wheel):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

        pass

    def setup(self):
        self.left_wheel.setup()
        self.right_wheel.setup()

    def move(self, array_velocities):
        self.left_wheel.move(array_velocities[0])
        self.right_wheel.move(array_velocities[1])


class Wheel:
    GPIO_PWM = None
    GPIO_control1 = None
    GPIO_control2 = None

    def __init__(self, GPIO_control1, GPIO_control2, GPIO_PWM):
        self.GPIO_control1 = GPIO_control1
        self.GPIO_control2 = GPIO_control2
        self.GPIO_PWM = GPIO_PWM
        pass

    def setup(self):
        GPIO.setup(self.GPIO_PWM, GPIO.OUT)
        GPIO.setup(self.GPIO_control1, GPIO.OUT)
        GPIO.setup(self.GPIO_control2, GPIO.OUT)

    def move(self, velocity):

        if velocity < 0:
            duty_cycle = velocity * -100
            wiringpi.softPwmWrite(self.GPIO_PWM, duty_cycle)
            GPIO.output(self.GPIO_control1, GPIO.LOW)
            GPIO.output(self.GPIO_control2, GPIO.HIGH)

        else:
            duty_cycle = velocity * 100
            wiringpi.softPwmWrite(self.GPIO_PWM, duty_cycle)
            GPIO.output(self.GPIO_control1, GPIO.HIGH)
            GPIO.output(self.GPIO_control2, GPIO.LOW)


class MockWheel:

    Name = "noname"

    def __init__(self, name):
        self.Name = name
        print "init Mock Wheel ", self.Name

    def setup(self):
        print "setup Wheel ", self.Name

    def move(self, velocity):
        print "move Wheel ", self.Name, " with velocity: ", velocity
