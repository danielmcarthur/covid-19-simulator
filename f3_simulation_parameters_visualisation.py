"""
FIT9136 Algorithms and Programming Foundations in Python S1 2020: Assignment 2 v.1.5.1
student: Daniel John McArthur
student-id: 31421393
student-email: dmca0006@student.monash.edu
date-last-modified: 8 June 2020

The following was made using the provided template from the subject Moodle.
This program utilises the functions from Task 1 and Task 2 of the Assignment in order to produce a visualisation of
the daily count of contagious persons.
"""

from f2_patient_simulation import *


def visual_curve(days, meeting_probability, patient_zero_health):
    sim_list = run_simulation(days, meeting_probability, patient_zero_health)
    print(sim_list)
    import matplotlib.pyplot as plt
    plt.plot(sim_list)
    plt.ylabel("Infectious Patients")
    plt.xlabel("Days")
    plt.show()
    return sim_list


if __name__ == '__main__':
    # Numbers are: Days, Likelihood of Meeting, 'Patient Zero' Health
    visual_curve(90, 0.18, 40)
    pass

# do not add code here (outside the main block).
