import noise


class PerlinNoise():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scale = 175
        self.octaves = 6         # Number of layers of noise to combine
        self.persistence = 0.5   # Amplitude multiplier for each successive octave
        self.lacunarity = 2.0    # Frequency multiplier for each successive octave

    def get_value(self, x, y):
        return  noise.pnoise2(
            x / self.scale,
            y / self.scale,
            self.octaves,
            self.persistence,
            self.lacunarity,
            repeatx=self.width,
            repeaty=self.height
        )
