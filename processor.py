import numpy as np
import math
import skfuzzy as fuzz


class Processor:
    thetas = [45, 90, 135, -135, -90, -45]

    angle = np.arange(-math.pi, math.pi, 0.1)
    x_speed_right = np.arange(0, 1, 0.1)
    x_speed_left = np.arange(0, 1, 0.1)

    angle_negative = fuzz.trimf(angle, [-math.pi, -math.pi, -math.pi / 4])
    angle_null = fuzz.trimf(angle, [-math.pi, 0, math.pi])
    angle_positive = fuzz.trimf(angle, [math.pi / 4, math.pi, math.pi])

    speed_right_slow = fuzz.trimf(x_speed_right, [0.0, 0.0, 0.2])
    speed_right_medium = fuzz.trimf(x_speed_right, [0, 0.5, 0.8])
    speed_right_fast = fuzz.trimf(x_speed_right, [0.4, 1.0, 1.0])

    speed_left_slow = fuzz.trimf(x_speed_left, [0.0,0.0, 0.2])
    speed_left_medium = fuzz.trimf(x_speed_left, [0.0, 0.5, 0.8])
    speed_left_fast = fuzz.trimf(x_speed_left, [0.4, 1.0, 1.0])

    def __init__(self):
        pass

    def process(self, array_distances):
        #print "Distances: ", array_distances
        repulsion_angle = self.calc_repulsion_angle(array_distances)

        angle_level_negative = fuzz.interp_membership(self.angle, self.angle_negative, repulsion_angle)
        angle_level_null = fuzz.interp_membership(self.angle, self.angle_null, repulsion_angle)
        angle_level_positive = fuzz.interp_membership(self.angle, self.angle_positive, repulsion_angle)

        left_fuzz = self.aggregated_left(angle_level_negative, angle_level_null, angle_level_positive)
        right_fuzz = self.aggregated_right(angle_level_positive, angle_level_null, angle_level_negative)

        return self.calc_velocity(left_fuzz, right_fuzz)

    def calc_velocity(self, left_fuzz, right_fuzz):
        r = [1.0] * 2
        r[0] = fuzz.defuzz(self.x_speed_left, left_fuzz, 'mom')
        r[1] = fuzz.defuzz(self.x_speed_right, right_fuzz, 'mom')

        return r

    def aggregated_left(self, negative, null, positive):
        return self.aggregated(negative,
                               null,
                               positive,
                               self.speed_left_slow,
                               self.speed_left_medium,
                               self.speed_left_fast)

    def aggregated_right(self, negative, null, positive):
        return self.aggregated(negative,
                               null,
                               positive,
                               self.speed_right_slow,
                               self.speed_right_medium,
                               self.speed_right_fast)

    def aggregated(self, negative, null, positive, slow, medium, fast):
        activation_slow = np.fmin(negative, slow)
        activation_medium = np.fmin(null, medium)
        activation_fast = np.fmin(positive, fast)
        return np.fmax(activation_slow, np.fmax(activation_medium, activation_fast))

    def calc_repulsion_angle(self, array_distances):
        x = 0.0
        y = 0.0

        for i in range(0, 6):
            x = x + array_distances[i] * math.cos(np.radians(self.thetas[i]))
            y = y + array_distances[i] * math.sin(np.radians(self.thetas[i]))
        repulsion = math.atan2(y, x)
        print "angulo en radianes: ", repulsion
        return repulsion


class MockProcessor:
    def __init__(self):
        pass

    def process(self, array_distances):
        print "Distances: ", array_distances
        return [0.1, 0.1]
