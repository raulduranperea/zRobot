
class Runtime:
    sensors = None
    processor = None
    wheels = None

    def __init__(self, sensors, processor, wheels):
        self.sensors = sensors
        self.processor = processor
        self.wheels = wheels
        pass

    def start(self):
        self.wheels.setup()
        self.sensors.setup()
        self.sensors.start(self._step)

    def _step(self, array_distances):
        velocities = self.processor.process(array_distances) #array de dos posiciones de -1 a 1
        self.wheels.move(velocities)