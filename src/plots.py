import sys
import json
import random


class Solvers:
    def __init__(self):
        with open('solvers.json') as data_file:
            self.instances = json.load(data_file)

    def get_instances_by_attributes(self, empirical, curious, funny, rash):
        ret = []
        for key in self.instances.keys():
            if empirical == True:
                if self.instances[key]['empirical'] == True:
                    ret.append(key)
            if curious == True:
                if self.instances[key]['curious'] == True:
                    ret.append(key)
            if funny == True:
                if self.instances[key]['funny'] == True:
                    ret.append(key)
            if rash == True:
                if self.instances[key]['rash'] == True:
                    ret.append(key)
        return ret

    def get_random_instance_by_attributes(self, empirical, curious, funny, rash):
        instances = self.get_instances_by_attributes(empirical, curious, funny, rash)
        return random.choice(instances)


class Victims:
    def __init__(self):
        with open('victims.json') as data_file:
            self.instances = json.load(data_file)

    def get_instances_by_attributes(self, musician, actor, athlete):
        ret = []
        for key in self.instances.keys():
            if musician == True:
                if self.instances[key]['musician'] == True:
                    ret.append(key)
            if actor == True:
                if self.instances[key]['actor'] == True:
                    ret.append(key)
            if athlete == True:
                if self.instances[key]['athlete'] == True:
                    ret.append(key)
        return ret

    def get_random_instance_by_attributes(self, musician, actor, athlete):
        instances = self.get_instances_by_attributes(musician, actor, athlete)
        return random.choice(instances)


class Locations:
    def __init__(self):
        with open('locations.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        musician = self.instances[instance]['musician']
        actor = self.instances[instance]['actor']
        athlete = self.instances[instance]['athlete']

        return musician, actor, athlete


class Problems:
    def __init__(self):
        with open('problems.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        quickly_curable = self.instances[instance]['quickly_curable']
        fast_acting = self.instances[instance]['fast_acting']

        return quickly_curable, fast_acting


class Symptoms:
    def __init__(self):
        with open('symptoms.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instances_by_attributes(self, quickly_curable, fast_acting):
        low = []
        medium = []
        high = []
        for symptom in self.instances.keys():
            if self.instances[symptom]['low_severity'] == True:
                low.append(symptom)
            if self.instances[symptom]['medium_severity'] == True:
                medium.append(symptom)
            if self.instances[symptom]['high_severity'] == True:
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
    def __init__(self):
        with open('plotfragments.json') as data_file:
            self.instances = json.load(data_file)

    def get_random_instance(self):
        return random.choice(list(self.instances.keys()))

    def get_instance_attributes(self, instance):
        empirical = self.instances[instance]['empirical']
        curious = self.instances[instance]['curious']
        funny = self.instances[instance]['funny']
        rash = self.instances[instance]['rash']

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

    def run(self):
        print("Basic Generated Plot:")

        location = self.locations.get_random_instance()
        print('LOCATION:        ' + str(location))

        musician, actor, athlete = self.locations.get_instance_attributes(location)
        victim = self.victims.get_random_instance_by_attributes(musician, actor, athlete)
        print('VICTIM:          ' + str(victim))

        plot = self.plot_fragments.get_random_instance()
        print('PLOT FRAGMENT:   ' + str(plot))

        empirical, curious, funny, rash = self.plot_fragments.get_instance_attributes(plot)
        solver = self.solvers.get_random_instance_by_attributes(empirical, curious, funny, rash)
        print('SOLVER:          ' + str(solver))

        problem = self.problems.get_random_instance()
        print('PROBLEM:         ' + str(problem))

        quickly_curable, fast_acting = self.problems.get_instance_attributes(problem)
        symptoms = self.symptoms.get_random_instances_by_attributes(quickly_curable, fast_acting)
        print('SYMPTOMS:        ' + str(symptoms))

        print("\nMedium Generated Plot:")
        print("In this episode, <<<" + str(victim) + ">>> suddenly experiences <<<" + str(symptoms) + ">>>")
        print("while at <<<" + location + ">>>. (S)he is taken to the hospital, where the doctors try to diagnose")
        print("the problem. <<<" + str(solver) + ">>> finally use/look <<<" + str(plot) + ">>>")
        print("to discover that the problem was <<<" + str(problem) + ">>>.")

    def generate(self, location, victim, plot, solver, problem, symptoms):
        if plot == 'device':
            pass
        elif plot == 'multiple_experiments':
            pass
        elif plot == 'epiphany_hearing_something':
            pass
        elif plot == 'epiphany_seeing_something':
            pass
        elif plot == 'epiphany_smelling_something':
            pass
        elif plot == 'location_activity':
            pass
        elif plot == 'past_family_history':
            pass
        elif plot == 'scour_journals':
            pass
        elif plot == 'consult_other_doctors':
            pass
        elif plot == 'ancient_techniques':
            pass
        elif plot == 'state_of_art_technique':
            pass
        elif plot == 'recall_similar_problem':
            pass
        elif plot == 'doctor_gets_similar_problem':
            pass
        elif plot == 'watch_another_doctor_show':
            pass
        elif plot == 'risking_treatment':
            pass
        elif plot == 'accidentally_apply_correct_treatment':
            pass
        elif plot == 'realize_smaller_problems':
            pass
        elif plot == 'death':
            pass


if __name__ == '__main__':
    generator = PlotGenerator()
    generator.run()
