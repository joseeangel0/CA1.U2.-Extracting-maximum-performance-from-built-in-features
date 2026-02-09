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

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        # Optimization 1: Loop over particles OUTSIDE the time steps
        # This allows us to pre-calculate the angular velocity factor
        for p in self.particles:
            t_x_ang = timestep * p.v  # assuming p.v holds the angular velocity

            for i in range(nsteps):
                # Optimization 2: Simplified math inside the tight loop
                norm = (p.x**2 + p.y**2)**0.5
                
                # Update x and y simultaneously
                p.x, p.y = (p.x - t_x_ang * p.y/norm,
                            p.y + t_x_ang * p.x/norm)

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