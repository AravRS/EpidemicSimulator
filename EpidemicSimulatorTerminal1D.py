# Epidemic Simulator Terminal App
import random


class Simulation():
    """Controls the entire simulation i.e spread of disease."""

    def __init__(self):
        """Initialize attributes"""
        self.day_number = 1
        print("\n---------EPIDEMIC SIMULATOR TERMINAL APP---------")
        print("People arranged in a line, i.e 1D\n")
        self.population_size = int(input("> Enter the population size: "))
        self.infection_percent = float(input("> Enter the percentage (0-100) of the population to initially infect: "))/100
        self.infection_probability = float(input("> Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_duration = int(input("> Enter the duration (in days) of the infection to last: "))
        self.mortality_rate = float(input("> Enter the mortality rate (0-100) of the infection: "))
        self.sim_days = int(input("> Enter the number of days to simulate: "))


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
    """Controls the simulation of an multiple person objects."""

    def __init__(self, simulation):
        """Initialize attributes"""
        self.population = []
        # Creates a person based on simulation conditions
        for i in range(simulation.population_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, simulation):
        """Initially infects a portion of the population."""
        infected_count = int(round(simulation.infection_percent*simulation.population_size, 0))
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
        random.shuffle(self.population)

    def spread_infection(self, simulation):
        """Spreads infection to adjacent 1D array of persons in population."""
        # only left-right 2D Line
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                # i-th person is first, can check to right only
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                # i-th person is middle, can check to left and right
                elif i < len(self.population)-1:
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                # i-th person is last, can check to left only
                elif i == len(self.population)-1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)

    def update(self, simulation):
        """Update the entire population by updating the persons individually."""
        simulation.day_number += 1

        for person in self.population:
            person.update(simulation)

    def display_stats(self, simulation):
        """Display the current statistics."""
        total_infected_count = 0
        total_death_count = 0

        for person in self.population:
            if person.is_infected:
                total_infected_count += 1
                if person.is_dead:
                    total_death_count += 1

        infected_percent = round((total_infected_count/simulation.population_size)*100, 4)
        death_percent = round((total_death_count/simulation.population_size)*100, 4)

        print(f"\n-----DAY #{simulation.day_number}-----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {death_percent}%")
        print(f"Total Infected: {total_infected_count} / {simulation.population_size}")
        print(f"Total Dead: {total_death_count} / {simulation.population_size}")

    def graphics(self):
        """A graphical representation of our population. O  healthy, I  infected, X dead."""
        status = []
        for person in self.population:
            if person.is_dead:
                char = "X"
            else:
                if person.is_infected:
                    char = "I"
                else:
                    char = "O"
            status.append(char)

        for letter in status:
            print(letter, end="-")


# Main code
sim = Simulation()
pop = Population(sim)

pop.initial_infection(sim)
pop.display_stats(sim)
pop.graphics()
input("\nPress Enter to begin the simulation.")

for i in range(1, sim.sim_days):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_stats(sim)
    pop.graphics()

    # if i != sim.sim_days-1:
    #     input("\Press Enter to  advance to the next day.")
