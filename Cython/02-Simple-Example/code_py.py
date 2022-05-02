import math

def generate_waves(length):
    waves = []
    for i in range(length):
        waves.append(math.sin(i))
    return waves