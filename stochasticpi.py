import random
import math


def start(arrow_count, output_interval):

    """
    Simulate firing arrows at a circle within a square, the proportion hitting
    the circle being used to estimate a value for Pi.
    """

    arrows_fired = 0
    circle_hits = 0
    pi_estimate = 0
    x = 0
    y = 0

    for i in range(0, arrow_count):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        arrows_fired += 1

        if _in_unit_circle(x, y):
            circle_hits += 1

        pi_estimate = (circle_hits / arrows_fired) * 4

        if arrows_fired % output_interval == 0:

            print("Intermediate estimate of Pi after {} arrows: {:.16f}".format(arrows_fired, pi_estimate))

    print("Final estimate of Pi after {} arrows: {:.16f}".format(arrow_count, pi_estimate))


def _in_unit_circle(x, y):

    """
    Calculate whether a particular position within a square
    is within a circle fitting the square.
    """

    if math.sqrt(x**2 + y**2) <= 1:
        return True
    else:
        return False
