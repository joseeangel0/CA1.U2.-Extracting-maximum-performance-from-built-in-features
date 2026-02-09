import matplotlib.pyplot as plt
from matplotlib import animation


class Particle:
    def __init__(self,x,y,v):
        self.x = x
        self.y = y
        self.v = v

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    @profile
    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        for i in range(nsteps):
            for p in self.particles:
                #calculate the distance from the center
                r = (p.x**2 + p.y**2)**0.5
                sin_theta = p.y / r
                cos_theta = p.x / r
                #calculate the displacemente
                dx = -timestep*p.v*sin_theta
                dy = timestep*p.v*cos_theta
                #update the position
                p.x += dx
                p.y += dy

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    
    fig = plt.figure()
    ax = plt.subplot(111,aspect= 'equal')
    line, = ax.plot(X,Y,'o')

    plt.xlim(-1,1)
    plt.ylim(-1,1)

    def init():
        line.set_data([],[])
        return line, 

    def animate(i):
        simulator.evolve(0.1)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X,Y)
        return line, 

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=10, blit=True)
    plt.show()

                    

def test_visualize():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, 0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

#BENCHMARK
from random import uniform

def benchmark():
    # Create 1000 particles (NO visualization)
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(1000)]
    
    simulator = ParticleSimulator(particles)
    # Run the simulation math ONLY
    simulator.evolve(0.1)

if __name__ == '__main__':
    #test_visualize()  #  <-- Make sure this is commented out or removed
    benchmark()