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
                          'Meghan Trainor': {'musician': True,
                                             'actor': False,
                                             'athlete': False},
                          'Justin Bieber': {'musician': True,
                                            'actor': False,
                                            'athlete': False},
                          'Kanye West': {'musician': True,
                                         'actor': False,
                                         'athlete': False},
                          'Big Sean': {'musician': True,
                                       'actor': False,
                                       'athlete': False},
                          'Kim Kardashian': {'musician': False,
                                             'actor': True,
                                             'athlete': False},
                          'Ellen DeGeneres': {'musician': False,
                                              'actor': True,
                                              'athlete': False},
                          'Ginnifer Woodwin': {'musician': False,
                                               'actor': True,
                                               'athlete': False},
                          'Donald Trump': {'musician': False,
                                           'actor': True,
                                           'athlete': False},
                          'Will Smith': {'musician': False,
                                         'actor': True,
                                         'athlete': False},
                          'Josh Dallas': {'musician': False,
                                          'actor': True,
                                          'athlete': False},
                          'Michael Jordan': {'musician': False,
                                             'actor': False,
                                             'athlete': True},
                          'Roger Federer': {'musician': False,
                                            'actor': False,
                                            'athlete': True},
                          'Michael Phelps': {'musician': False,
                                             'actor': False,
                                             'athlete': True},
                          'Tiger Woods': {'musician': False,
                                          'actor': False,
                                          'athlete': True},
                          'Serena Williams': {'musician': False,
                                              'actor': False,
                                              'athlete': True},
                          'Danica Patrick': {'musician': False,
                                             'actor': False,
                                             'athlete': True},
                          'Alex Morgan': {'musician': False,
                                          'actor': False,
                                          'athlete': True},
                          'Kerri Walsh Jennings': {'musician': False,
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
                          'fundraiser': {'musician': True,
                                         'actor': True,
                                         'athlete': True},
                          'fancy_restaurant': {'musician': True,
                                               'actor': True,
                                               'athlete': True},
                          'home': {'musician': True,
                                   'actor': True,
                                   'athlete': True},
                          'vacation': {'musician': True,
                                       'actor': True,
                                       'athlete': True},
                          'talk_show': {'musician': True,
                                        'actor': True,
                                        'athlete': True},
                          'athletic_performance': {'musician': True,
                                                   'actor': False,
                                                   'athlete': True},
                          'gym': {'musician': False,
                                  'actor': True,
                                  'athlete': True},
                          'park': {'musician': False,
                                   'actor': True,
                                   'athlete': True},
                          'beach': {'musician': False,
                                    'actor': True,
                                    'athlete': True},
                          'bar': {'musician': True,
                                  'actor': False,
                                  'athlete': True},
                          'on_set_at_tv_show': {'musician': False,
                                                'actor': True,
                                                'athlete': True},
                          'salon': {'musician': True,
                                    'actor': True,
                                    'athlete': False},
                          'fashion_show': {'musician': True,
                                           'actor': True,
                                           'athlete': False},
                          'mall': {'musician': True,
                                   'actor': False,
                                   'athlete': True},
                          'dentist': {'musician': True,
                                      'actor': False,
                                      'athlete': True},
                          'plastic_surgery_hospital': {'musician': True,
                                                       'actor': True,
                                                       'athlete': False},
                          'Grammy’s': {'musician': True,
                                       'actor': True,
                                       'athlete': False},
                          'studio': {'musician': True,
                                     'actor': False,
                                     'athlete': True},
                          'post office': {'musician': True,
                                          'actor': False,
                                          'athlete': True}}

    def get_random_instance(self):
        instances = list(self.instances.keys())

        return random.choice(instances)

    def get_instance_attributes(self, instance):
        return self.instances[instance]['musician'], self.instances[instance]['actor'], self.instances[instance][
            'athlete'],


class Problems:
    def __init__(self):
        self.instances = {
            'Infection': {'quickly_curable': True,
                          'fast_acting': True},
            'Disease': {'quickly_curable': True,
                        'fast_acting': True},
            'Overdose': {'quickly_curable': True,
                         'fast_acting': True},
            'Poisoning': {'quickly_curable': True,
                          'fast_acting': True},
            'Parasite': {'quickly_curable': True,
                         'fast_acting': True},
            'Vitamin deficiency': {'quickly_curable': True,
                                   'fast_acting': False},
            'Immune System': {'quickly_curable': True,
                              'fast_acting': False},
            'Lung problems': {'quickly_curable': True,
                              'fast_acting': False},
            'Inherited problems': {'quickly_curable': True,
                                   'fast_acting': False},
            'Fungus': {'quickly_curable': True,
                       'fast_acting': False},
            'Radiation': {'quickly_curable': True,
                          'fast_acting': False},
            'Incorrect transplant': {'quickly_curable': True,
                                     'fast_acting': False},
            'Cancer': {'quickly_curable': False,
                       'fast_acting': True},
            'Virus': {'quickly_curable': False,
                      'fast_acting': True},
            'Bone problems': {'quickly_curable': False,
                              'fast_acting': True},
            'Mental problems': {'quickly_curable': False,
                                'fast_acting': True},
            'Brain issues': {'quickly_curable': False,
                             'fast_acting': True},
            'Blood issues': {'quickly_curable': False,
                             'fast_acting': True},
            'Drug influence': {'quickly_curable': False,
                               'fast_acting': True},
            'Genetic problems': {'quickly_curable': False,
                                 'fast_acting': True}}


class Symptoms:
    def __init__(self):
        self.instances = {
            'Seizures': {'low_severity': False,
                         'medium_severity': False,
                         'high_severity': True},
            'Bodily function fail': {'low_severity': False,
                                     'medium_severity': False,
                                     'high_severity': True},
            'Blindness': {'low_severity': False,
                          'medium_severity': False,
                          'high_severity': True},
            'White blood cell drop': {'low_severity': False,
                                      'medium_severity': False,
                                      'high_severity': True},
            'Irregular heartbeat': {'low_severity': False,
                                    'medium_severity': False,
                                    'high_severity': True},
            'Fever': {'low_severity': False,
                      'medium_severity': False,
                      'high_severity': True},
            'Hypothermia': {'low_severity': False,
                            'medium_severity': False,
                            'high_severity': True},
            'Hallucinations': {'low_severity': False,
                               'medium_severity': True,
                               'high_severity': False},
            'Collapsed': {'low_severity': False,
                          'medium_severity': True,
                          'high_severity': False},
            'Swelling': {'low_severity': False,
                         'medium_severity': True,
                         'high_severity': False},
            'Shortness of breathe': {'low_severity': False,
                                     'medium_severity': True,
                                     'high_severity': False},
            'Coughing': {'low_severity': False,
                         'medium_severity': True,
                         'high_severity': False},
            'Weakness': {'low_severity': False,
                         'medium_severity': True,
                         'high_severity': False},
            'Stiffness': {'low_severity': True,
                          'medium_severity': False,
                          'high_severity': False},
            'Leg pain': {'low_severity': True,
                         'medium_severity': False,
                         'high_severity': False},
            'Dizziness': {'low_severity': True,
                          'medium_severity': False,
                          'high_severity': False},
            'Loss of hearing': {'low_severity': True,
                                'medium_severity': False,
                                'high_severity': False},
            'Numbness': {'low_severity': True,
                         'medium_severity': False,
                         'high_severity': False},
            'Sensitivity': {'low_severity': True,
                            'medium_severity': False,
                            'high_severity': False},
            'Rash': {'low_severity': True,
                     'medium_severity': False,
                     'high_severity': False}}


class PlotFragments:
    def __init__(self):
        self.instances = {'device': {'empirical': True,
                                     'curious': True,
                                     'funny': False,
                                     'rash': False},
                          'multiple_experiments': {'empirical': True,
                                                   'curious': True,
                                                   'funny': False,
                                                   'rash': False},
                          'epiphany_hearing_something': {'empirical': False,
                                                         'curious': True,
                                                         'funny': True,
                                                         'rash': False},
                          'epiphany_seeing_something': {'empirical': False,
                                                        'curious': True,
                                                        'funny': True,
                                                        'rash': False},
                          'epiphany_smelling_something': {'empirical': False,
                                                          'curious': True,
                                                          'funny': True,
                                                          'rash': False},
                          'location_activity': {'empirical': False,
                                                'curious': True,
                                                'funny': True,
                                                'rash': True},
                          'past_family_history': {'empirical': False,
                                                  'curious': True,
                                                  'funny': True,
                                                  'rash': True},
                          'scour_journals': {'empirical': True,
                                             'curious': True,
                                             'funny': False,
                                             'rash': False},
                          'consult_other_doctors': {'empirical': True,
                                                    'curious': True,
                                                    'funny': False,
                                                    'rash': False},
                          'ancient_techniques': {'empirical': False,
                                                 'curious': True,
                                                 'funny': True,
                                                 'rash': True},
                          'state_of_art_technique': {'empirical': True,
                                                     'curious': False,
                                                     'funny': False,
                                                     'rash': False},
                          'recall_similar_problem': {'empirical': False,
                                                     'curious': True,
                                                     'funny': True,
                                                     'rash': False},
                          'doctor_gets_similar_problem': {'empirical': True,
                                                          'curious': False,
                                                          'funny': False,
                                                          'rash': True},
                          'watch_another_doctor_show': {'empirical': True,
                                                        'curious': False,
                                                        'funny': True,
                                                        'rash': False},
                          'risking_treatment': {'empirical': True,
                                                'curious': False,
                                                'funny': True,
                                                'rash': True},
                          'accidentally_apply_correct_treatment': {'empirical': False,
                                                                   'curious': False,
                                                                   'funny': True,
                                                                   'rash': True},
                          'realize_smaller_problems': {'empirical': True,
                                                       'curious': False,
                                                       'funny': True,
                                                       'rash': False},
                          'death': {'empirical': True,
                                    'curious': False,
                                    'funny': False,
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
