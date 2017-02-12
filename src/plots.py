import sys
import json
import random


class Solvers:
    EMPIRICAL = 'empirical'
    CURIOUS = 'curious'
    FUNNY = 'funny'
    RASH = 'rash'

    def __init__(self):
        with open('solvers.json') as data_file:
            self.instances = json.load(data_file)

    def get_instances_by_attributes(self, empirical, curious, funny, rash):
        ret = []
        for key in self.instances.keys():
            if empirical == True:
                if self.instances[key][self.EMPIRICAL] == True:
                    ret.append(key)
            if curious == True:
                if self.instances[key][self.CURIOUS] == True:
                    ret.append(key)
            if funny == True:
                if self.instances[key][self.FUNNY] == True:
                    ret.append(key)
            if rash == True:
                if self.instances[key][self.RASH] == True:
                    ret.append(key)
        return ret

    def get_random_instance_by_attributes(self, empirical, curious, funny, rash):
        instances = self.get_instances_by_attributes(empirical, curious, funny, rash)
        return random.choice(instances)


class Victims:
    MUSICIAN = 'musician'
    ACTOR = 'actor'
    ATHLETE = 'athlete'

    def __init__(self):
        with open('victims.json') as data_file:
            self.instances = json.load(data_file)

    def get_instances_by_attributes(self, musician, actor, athlete):
        ret = []
        for key in self.instances.keys():
            if musician == True:
                if self.instances[key][self.MUSICIAN] == True:
                    ret.append(key)
            if actor == True:
                if self.instances[key][self.ACTOR] == True:
                    ret.append(key)
            if athlete == True:
                if self.instances[key][self.ATHLETE] == True:
                    ret.append(key)
        return ret

    def get_random_instance_by_attributes(self, musician, actor, athlete):
        instances = self.get_instances_by_attributes(musician, actor, athlete)
        return random.choice(instances)


class Locations:
    MUSICIAN = 'musician'
    ACTOR = 'actor'
    ATHLETE = 'athlete'

    def __init__(self):
        with open('locations.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        musician = self.instances[instance][self.MUSICIAN]
        actor = self.instances[instance][self.ACTOR]
        athlete = self.instances[instance][self.ATHLETE]

        return musician, actor, athlete


class Problems:
    QUICKLY_CURABLE = 'quickly_curable'
    FAST_ACTING = 'fast_acting'

    def __init__(self):
        with open('problems.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        quickly_curable = self.instances[instance][self.QUICKLY_CURABLE]
        fast_acting = self.instances[instance][self.FAST_ACTING]

        return quickly_curable, fast_acting


class Symptoms:
    LOW = 'low_severity'
    MEDIUM = 'medium_severity'
    HIGH = 'high_severity'

    def __init__(self):
        with open('symptoms.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instances_by_attributes(self, quickly_curable, fast_acting):
        low = []
        medium = []
        high = []
        for symptom in self.instances.keys():
            if self.instances[symptom][self.LOW] == True:
                low.append(symptom)
            if self.instances[symptom][self.MEDIUM] == True:
                medium.append(symptom)
            if self.instances[symptom][self.HIGH] == True:
                high.append(symptom)

        num_low = 0
        num_medium = 0
        num_high = 0
        if quickly_curable == True and fast_acting == True:
            num_low = random.randint(1, 2)
            num_medium = 1
        elif quickly_curable == True and fast_acting == False:
            num_low = random.randint(1, 3)
            num_high = 1
        elif quickly_curable == False and fast_acting == True:
            num_low = random.randint(1, 2)
            num_medium = 1
            num_high = 1
        else:
            pass

        symptoms = []
        symptoms += random.sample(low, num_low)
        symptoms += random.sample(medium, num_medium)
        symptoms += random.sample(high, num_high)

        return symptoms


class PlotFragments:
    EMPIRICAL = 'empirical'
    CURIOUS = 'curious'
    FUNNY = 'funny'
    RASH = 'rash'

    def __init__(self):
        with open('plotfragments.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        return random.choice(list(self.instances.keys()))

    def get_instance_attributes(self, instance):
        empirical = self.instances[instance][self.EMPIRICAL]
        curious = self.instances[instance][self.CURIOUS]
        funny = self.instances[instance][self.FUNNY]
        rash = self.instances[instance][self.RASH]

        return empirical, curious, funny, rash


class PlotGenerator:
    EMPIRICAL = 'empirical'
    CURIOUS = 'curious'
    FUNNY = 'funny'
    RASH = 'rash'
    MUSICIAN = 'musician'
    ACTOR = 'actor'
    ATHLETE = 'athlete'

    def __init__(self):
        self.solvers = Solvers()
        self.victims = Victims()
        self.locations = Locations()
        self.problems = Problems()
        self.symptoms = Symptoms()
        self.plot_fragments = PlotFragments()

        with open('templates.json') as data_file:
            self.templates = json.load(data_file)

        with open('choices.json') as data_file:
            self.choices = json.load(data_file)

    def run(self):
        location = self.locations.get_random_instance()
        musician, actor, athlete = self.locations.get_instance_attributes(location)
        victim = self.victims.get_random_instance_by_attributes(musician, actor, athlete)
        plot = self.plot_fragments.get_random_instance()
        empirical, curious, funny, rash = self.plot_fragments.get_instance_attributes(plot)
        solver = self.solvers.get_random_instance_by_attributes(empirical, curious, funny, rash)
        problem = self.problems.get_random_instance()
        quickly_curable, fast_acting = self.problems.get_instance_attributes(problem)
        symptoms = self.symptoms.get_random_instances_by_attributes(quickly_curable, fast_acting)

        # print("Basic Generated Plot:")
        # print('PLOT FRAGMENT:   ' + str(plot))
        # print('SOLVER:          ' + str(solver))
        # print('VICTIM:          ' + str(victim))
        # print('LOCATION:        ' + str(location))
        # print('PROBLEM:         ' + str(problem))
        # print('SYMPTOMS:        ' + str(symptoms))
        #
        # print("\nMedium Generated Plot:")
        # print("In this episode, <<<" + str(victim) + ">>> suddenly experiences <<<" + str(symptoms) + ">>>")
        # print("while at <<<" + location + ">>>. (S)he is taken to the hospital, where the doctors try to diagnose")
        # print("the problem. <<<" + str(solver) + ">>> finally use/look <<<" + str(plot) + ">>>")
        # print("to discover that the problem was <<<" + str(problem) + ">>>.\n")

        self.generate(location, victim, plot, solver, problem, symptoms)

    def generate(self, location, victim, plot, solver, problem, symptoms):
        plotkey = None
        for plotkey in self.templates:
            if plot in self.templates[plotkey]:
                break

        print(plot)

        summary = self.templates[plotkey]['summary']
        if len(symptoms) < 3:
            string_symptoms = symptoms[0] + " and " + symptoms[1]
        else:
            string_symptoms = ", ".join(symptoms[:-1])
            string_symptoms += ", and " + str(symptoms[-1])
        summary = str(summary).replace("#SYMPTOMS#", string_symptoms)

        string_plot = self.templates[plotkey][plot]
        # string_plot = str(string_plot).replace("#SOLVER#", solver)
        # string_plot = str(string_plot).replace("#VICTIM#", victim)
        # string_plot = str(string_plot).replace("#LOCATION#", location)
        summary = str(summary).replace("#PLOTFRAG#", string_plot)

        if plot in self.choices:
            choice = random.choice(self.choices[plot])
            summary = str(summary).replace("#CHOICE#", choice)

        summary = str(summary).replace("#SOLVER#", solver)
        summary = str(summary).replace("#VICTIM#", victim)
        summary = str(summary).replace("#LOCATION#", location)
        summary = str(summary).replace("#PROBLEM#", problem)

        print(summary)

if __name__ == '__main__':
    generator = PlotGenerator()
    done = False
    while not done:
        try:
            generator.run()
            done = True
        except:
            pass
