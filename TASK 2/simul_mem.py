from random import uniform

class Particle:
    __slots__ = ('x', 'y', 'v')  # This line is for the second part of the test.
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y/norm
                v_y = p.x/norm
                d_x = timestep * p.v * v_x
                d_y = timestep * p.v * v_y
                p.x += d_x
                p.y += d_y

@profile 
def benchmark_memory():
    # We use 100,000 particles to make the memory usage visible
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(100000)]
    
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)

if __name__ == '__main__':
    benchmark_memory()