# Libraries
import RPi.GPIO as GPIO
import time


class Sensors:
    array_sensors = None

    def __init__(self, array_sensors):
        self.array_sensors = array_sensors
        pass

    def setup(self):
        for sensor in self.array_sensors:
            sensor.setup()

    def start(self, callback):
        while True:
            distances = []
            for sensor in self.array_sensors:
                distances.append(sensor.pulse())

            print "Distances: ", distances
            callback(distances)


class Sensor:
    TRIGGER = None
    ECHO = None

    def __init__(self, trigger, echo):
        self.TRIGGER = trigger
        self.ECHO = echo
        pass

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        # set GPIO direction (IN / OUT)
        GPIO.setup(self.TRIGGER, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def pulse(self):
        print "Sensor: " + self.TRIGGER + " " + self.ECHO + " START PULSE"
        GPIO.output(self.TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.TRIGGER, False)
        start = time.time()
        stop = time.time()

        # save start
        while GPIO.input(self.ECHO) == 0:
            start = time.time()

        # save time of arrival
        while GPIO.input(self.ECHO) == 1:
            stop = time.time()

        # time difference between start and arrival
        TimeElapsed = stop - start
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        distance = distance / 100
        if distance > 1.0:
            distance = 1.0

        print "Sensor: ", self.TRIGGER, " ", self.ECHO, " END PULSE -> ", distance

        return distance
