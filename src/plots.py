import sys
import random


class Solvers:
    def __init__(self):
        self.instances = {'House': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'Wilson': {'empirical': False,
                                     'curious': True,
                                     'funny': True,
                                     'rash': False},
                          'Foreman': {'empirical': True,
                                      'curious': True,
                                      'funny': False,
                                      'rash': False},
                          'Cameron': {'empirical': False,
                                      'curious': True,
                                      'funny': False,
                                      'rash': True},
                          'Chase': {'empirical': False,
                                    'curious': False,
                                    'funny': True,
                                    'rash': True},
                          'Cuddy': {'empirical': True,
                                    'curious': False,
                                    'funny': True,
                                    'rash': False}}


class Victims:
    def __init__(self):
        self.instances = {'Beyonce': {'musician': True,
                                      'actor': False,
                                      'athlete': False},
                          'Taylor Swift': {'musician': True,
                                           'actor': False,
                                           'athlete': False},
                          'Justin Bieber': {'musician': True,
                                            'actor': False,
                                            'athlete': False},
                          'Kanye West': {'musician': True,
                                         'actor': False,
                                         'athlete': False},
                          'Kim Kardashian': {'musician': False,
                                             'actor': True,
                                             'athlete': False},
                          'Donald Trump': {'musician': False,
                                           'actor': True,
                                           'athlete': False},
                          'Ellen DeGeneres': {'musician': False,
                                              'actor': True,
                                              'athlete': False},
                          'Will Smith': {'musician': False,
                                         'actor': True,
                                         'athlete': False},
                          'Michael Jordan': {'musician': False,
                                             'actor': False,
                                             'athlete': True},
                          'Roger Federer': {'musician': False,
                                            'actor': False,
                                            'athlete': True},
                          'Serena Williams': {'musician': False,
                                              'actor': False,
                                              'athlete': True},
                          'Danica Patrick': {'musician': False,
                                             'actor': False,
                                             'athlete': True}}

    def get_instances_by_attribute(self, musician, actor, athlete):
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

    def get_random_instance_by_attribute(self, musician, actor, athlete):
        instances = self.get_instances_by_attribute(musician, actor, athlete)
        return random.choice(instances)


class Locations:
    def __init__(self):
        self.instances = {'music_concert': {'musician': True,
                                            'actor': True,
                                            'athlete': True},
                          'tv_show': {'musician': True,
                                      'actor': True,
                                      'athlete': False},
                          'athletic_performance': {'musician': True,
                                                   'actor': False,
                                                   'athlete': True},
                          'fashion_show': {'musician': False,
                                           'actor': True,
                                           'athlete': True},
                          'fundraiser': {'musician': True,
                                         'actor': True,
                                         'athlete': True}}

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        return self.instances[instance]['musician'], self.instances[instance]['actor'], self.instances[instance][
            'athlete'],


class Problems:
    def __init__(self):
        self.instances = {'infection': {'quickly_curable': True,
                                        'fast_acting': True},
                          'virus': {'quickly_curable': False,
                                    'fast_acting': True},
                          'disease': {'quickly_curable': True,
                                      'fast_acting': True},
                          'poisoning': {'quickly_curable': True,
                                        'fast_acting': True},
                          'vitamin deficiency': {'quickly_curable': True,
                                                 'fast_acting': False},
                          'cancer': {'quickly_curable': False,
                                     'fast_acting': True},
                          'inherited problems': {'quickly_curable': True,
                                                 'fast_acting': False}}


class Symptoms:
    def __init__(self):
        self.instances = {'collapsed': {'low_severity': True,
                                        'medium_severity': False,
                                        'high_severity': False},
                          'seizures': {'low_severity': False,
                                       'medium_severity': False,
                                       'high_severity': True},
                          'hallucinations': {'low_severity': False,
                                             'medium_severity': True,
                                             'high_severity': False},
                          'white_blood_cell_count_drop': {'low_severity': False,
                                                          'medium_severity': True,
                                                          'high_severity': False},
                          'bodily_function_false': {'low_severity': False,
                                                    'medium_severity': False,
                                                    'high_severity': True},
                          'leg_pain': {'low_severity': True,
                                       'medium_severity': False,
                                       'high_severity': False},
                          'allergic_rash': {'low_severity': True,
                                            'medium_severity': False,
                                            'high_severity': False}}


class PlotFragments:
    def __init__(self):
        self.instances = {'device': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'experiments': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'epiphany': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'location_activity': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'past_family_history': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'recall_similar_situation': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'risking_treatment': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True},
                          'death': {'empirical': True,
                                    'curious': True,
                                    'funny': True,
                                    'rash': True}}

    def get_random_instance(self):
        return random.choice(self.instances)


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

    def generate(self):
        print("Generated Plot:")

        location = self.locations.get_random_instance()
        print('LOCATION: ' + str(location))

        musician, actor, athlete = self.locations.get_instance_attributes(location)
        victims = self.victims.get_random_instance_by_attribute(musician, actor, athlete)
        print('VICTIM: ' + str(victims))

        plot = self.plot_fragments.get_random_instance()
        print('PLOT FRAGMENT: ' + str(plot))


if __name__ == '__main__':
    generator = PlotGenerator()
    generator.generate()
