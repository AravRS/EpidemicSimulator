# Epidemic Simulator Terminal App
import random


class Simulation():
    """Controls the entire simulation i.e spread of disease."""

    def __init__(self):
        """Initialize attributes"""
        self.day_number = 1
        self.population_size = int(input(">Enter the population size: "))
        self.infection_percent = float(input(">Enter the percentage (0-100) of the population to initially infect: "))/100
        self.infection_probability = float(input(">Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_duration = int(input(">Enter the duration (in days) of the infection: "))
        self.mortality_rate = float(input(">Enter the mortality rate (0-100) of the infection: "))
        self.sim_days = int(input(">Enter the number of days to simulate: "))


class Person():
    """Controls the simulation of an individual person."""

    def __init__(self):
        """Initialize attributes"""
        self.is_infected = False  # Person starts healthy, not infected
        self.is_dead = False  # Person starts alive!
        self.days_infected = 0  # Before it begins!

    def infect(self, simulation):
        """Infect a person based on simulation conditions"""
        if random.randint(0, 100) < simulation.infection_probability:
            self.is_infected = True

    def heal(self):
        """Heals a person based on simulation conditions"""
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        """Kills a person based on simulation conditions"""
        self.is_dead = True

    def update(self, simulation):
        """Updates person if not dead, if infected, increase days_infected, then heal or kill, based on simulation conditions"""
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                if random.randint(0, 100) < simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()


class Population():
    pass


sim = Simulation()
