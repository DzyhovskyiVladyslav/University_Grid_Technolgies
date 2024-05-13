import math



class Cone:
    def __init__(self, x, v, h, ro, alpha, rozh, f, g):
        self.x = x
        self.v = v
        self.h = h
        self.ro = ro
        self.alpha = alpha
        self.rozh = rozh
        self.f = f
        self.g = g
        self.m = (math.pi * ro / 3) * math.tan(alpha) ** 2 * h ** 3
        self.h0 = h * (ro / rozh) ** (1 / 3)

    def calculated2xd2t(self, x, v):
        return -self.g + ((math.pi * math.tan(self.alpha) ** 2 * (self.h0 - x) ** 2) / self.m) * (
                (self.rozh * self.g / 3) * (self.h0 - x) - self.f * v / math.sin(self.alpha))

    def moving(self, dt):
        d2xd2t = self.calculated2xd2t(self.x, self.v)
        self.x += self.v * dt
        self.v += d2xd2t * dt

    def getPosition(self):
        return self.x

    def getSpeed(self):
        return self.v


if __name__ == '__main__':
    cone = Cone(0.1, 0.0, 0.25, 500, 30 * math.pi / 180, 500, 30, 9.8)
    file = open("output.csv", "w")
    file.write("Time,Position,Speed\n")
    dt = 0.001
    t_max = 10.0

    time = []
    position = []
    speed = []

    for t in range(int(t_max / dt) + 1):
        cone.moving(dt)
        time.append(t * dt)
        position.append(cone.getPosition())
        speed.append(cone.getSpeed())
        file.write(str(t * dt))
        file.write(",")
        file.write(str(cone.getPosition()))
        file.write(",")
        file.write(str(cone.getSpeed()))
        file.write(",\n")

    file.close()
