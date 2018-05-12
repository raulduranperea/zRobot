import numpy as np
import math
import skfuzzy as fuzz

class Processor:
    def __init__(self):
        pass

    def process(self, array_distances):
        r = [1.0] * 2
        theta = [10, 46, 82, 118, 154, -170, -134, -98, -62,
                 -26]  # Sensores colocados a partir del angulo 10 en posiciones de 36 grados
        x = 0
        y = 0

        for i in range(0.10):
            x = x + array_distances[i] * math.cos(np.radians(theta[i]))
            y = y + array_distances[i] * math.sin(np.radians(theta[i]))

        repulsion_angle = math.atan2(y, x)

        angulo = np.arange(-math.pi, math.pi, 0.1)
        x_speed_dcha = np.arange(0, 1, 0.1)
        x_speed_izda = np.arange(0, 1, 0.1)

        angulo_negativo = fuzz.trimf(angulo, [-math.pi, -math.pi, -math.pi / 4])
        angulo_nulo = fuzz.trimf(angulo, [-math.pi, 0, math.pi])
        angulo_positivo = fuzz.trimf(angulo, [math.pi / 4, math.pi, math.pi])

        speed_dcha_lento = fuzz.trimf(x_speed_dcha, [0, 0, 0.9])
        speed_dcha_medio = fuzz.trimf(x_speed_dcha, [0.5, 0.9, 1.3])
        speed_dcha_rapido = fuzz.trimf(x_speed_dcha, [0.9, 1.5, 1.5])

        speed_izda_lento = fuzz.trimf(x_speed_izda, [0, 0, 0.9])
        speed_izda_medio = fuzz.trimf(x_speed_izda, [0.5, 0.9, 1.3])
        speed_izda_rapido = fuzz.trimf(x_speed_izda, [0.9, 1.5, 1.5])

        angulo_nivel_negativo = fuzz.interp_membership(angulo, angulo_negativo, repulsion_angle)
        angulo_nivel_nulo = fuzz.interp_membership(angulo, angulo_nulo, repulsion_angle)
        angulo_nivel_positivo = fuzz.interp_membership(angulo, angulo_positivo, repulsion_angle)

        speed_activation_dcha_lento = np.fmin(angulo_nivel_negativo, speed_dcha_rapido)
        speed_activation_dcha_medio = np.fmin(angulo_nivel_nulo, speed_dcha_medio)
        speed_activation_dcha_rapido = np.fmin(angulo_nivel_positivo, speed_dcha_lento)

        speed_activation_izda_lento = np.fmin(angulo_nivel_negativo, speed_izda_lento)
        speed_activation_izda_medio = np.fmin(angulo_nivel_nulo, speed_izda_medio)
        speed_activation_izda_rapido = np.fmin(angulo_nivel_positivo, speed_izda_rapido)

        aggregated1 = np.fmax(speed_activation_izda_medio,
                              np.fmax(speed_activation_izda_rapido, speed_activation_izda_lento))
        aggregated2 = np.fmax(speed_activation_dcha_rapido,
                              np.fmax(speed_activation_dcha_medio, speed_activation_dcha_lento))
        r[0] = fuzz.defuzz(x_speed_izda, aggregated1, 'mom')
        r[1] = fuzz.defuzz(x_speed_dcha, aggregated2, 'mom')

        return r


class MockProcessor:
    def __init__(self):
        pass

    def process(self, array_distances):
        print("distance:" + array_distances)
