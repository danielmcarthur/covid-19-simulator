"""
Author: Daniel John McArthur
date-last-modified: 16 December 2020

This function was created to generate the viral severity (or load) by each person. This simulation acts with the notion that all
persons produce a viral_load, however contagious persons have a calculated value and non-contagious persons have a
viral_load of 0. Hence, during infection only the contagious persons deliver an affecting viral_load. This function then
runs a simulation for the virus spread after the introduction of a patient 0 who is contagious. 
"""

import math

from f1_sample_set_loading import *

# This defines the parent class of Person, Patient. It has infection capabilities and values for health
class Patient(Person):
    def __init__(self, first_name, last_name, health):
        Person.__init__(self, first_name, last_name)
        self.health = int(health)
        self.friend_list = []

    def get_health(self):
        print(int(self.health))
        return self.health

    def set_health(self, new_health):
        self.health = new_health
        # This checks the health - if it goes over 100, it returns to 100 and similar if it goes below 0
        if self.health < 0:
            self.health = 0
        if self.health > 100:
            self.health = 100

    def is_contagious(self):
        if self.health <= 49:
            return True
        else:
            return False

    def infect(self, viral_load):
        # When someone is infected, they receive the viral load of another person
        # Conditions for the health points affected with the viral load
        if self.health <= 29:
            self.set_health(self.health - 0.1 * viral_load)
        if 20 < self.health < 50:
            self.set_health(self.health - 1 * viral_load)
        if self.health >= 50:
            self.set_health(self.health - 2 * viral_load)

    def get_viral(self):    # This function calculates the viral_load of the person, given they are contagious
        if self.is_contagious() is True:        # If the person is contagious, they will produce a viral load
            viral_load = 5 + (math.pow((self.health - 25), 2)) / 62  # Formula for the viral load
        elif self.is_contagious() is False:     # If the person is not contagious, their viral_load is 0
            viral_load = 0
        return viral_load

    def sleep(self):    # When a person sleeps, their new health is increased by 5
        self.set_health(self.health + 5)


def run_simulation(days, meeting_probability, patient_zero_health):
    all_patients = load_patients(75)  # Loads all of the patients into the function, stores them as a list
    all_patients[0].set_health(patient_zero_health)  # Sets the first patient as having the p_zero_health
    contagious = 0
    contagious_tally = []   # List of the daily count of contagious people

    import random

    d = 1
    while d <= days:    # This is the iterative day simulation: everything done in one day will occur here
        contagious_day = 0  # This is the daily count of contagious people

        # Meetings for the day
        for x in all_patients:  # For each patient in the patient list
            x.is_contagious()
            for y in x.friend_list:     # Look at their friend list
                r = random.random()     # Random float between 0 and 1
                if r < meeting_probability:     # Checks the probability of meeting
                    # If either of x and y are contagious, they should infect one another
                    if x.is_contagious() or y.is_contagious() is True:
                        # Because if either are non-contagious, their get_viral will return a 0 load value
                        y.infect(x.get_viral())
                        x.infect(y.get_viral())
                else:   # This was not a viral meeting
                    # print("No infection")
                    pass

        for x in all_patients:  # Count the no. of infectious persons per day then record this
            if x.is_contagious() is True:
                contagious_day += 1
        contagious_tally.append(contagious_day)

        # Meetings have completed, now the end of the day occurs and everyone sleeps, they may recover overnight
        for x in all_patients:
            x.sleep()

        d += 1

    # Once the simulation is over this will count the patients that are contagious after all days
    for x in all_patients:
        if x.is_contagious() is True:
            contagious += 1
    return contagious_tally


def load_patients(initial_health):
    sample_set_open = open("sample_set.txt", "r")
    sample_set = sample_set_open.read().splitlines()
    all_patients = []  # This is the list of all person objects

    # This goes through each line in the sample_set.txt and takes the first name of each line
    for x in sample_set:
        x.strip("\n")
        person_name = x.split(": ")[0]  # Takes the string before the :
        person_object = Patient(person_name.split(" ")[0], person_name.split(" ")[1], initial_health)  # Creates Patient
        all_patients.append(person_object)  # Adds the created patient to the all_patients list

    # All patients are now defined, this goes back through the sample_set and adds friends to the persons
    for y in sample_set:  # For each line from the sample_set
        y.strip("\n")  # Get rid of the new line
        person_name = y.split(": ")  # Takes the string before the ": " this will be the parent object
        person_fname = person_name[0].split(" ")[0]  # Creates the first name for this person
        person_lname = person_name[0].split(" ")[1]
        # This creates a list with each element a string of the friend's name
        friend_strlist = person_name[1].split(", ")

        # I have the person's name: person_fname and a list(friend_list[]) with each friend's first name
        for k in all_patients:  # For every person object
            if k.first_name == person_fname and k.last_name == person_lname:  # Verifies this is the correct person
                for x in all_patients:  # For any of the persons in the all_persons list
                    if x in k.friend_list:  # If they are in the friend list already, break
                        break
                    else:   # This will check the first and last name of the person with the sample set and then add
                        for f in friend_strlist:
                            if f.split(" ")[0] == x.first_name and f.split(" ")[1] == x.last_name:
                                k.add_friend(x)
    sample_set_open.close()
    return all_patients


if __name__ == '__main__':
    pass
    # to check if the code is working the way you expect.

    # test = run_simulation(30, 0.6, 25)  # Days, Meet, Health
    # print(test)

    # This checks the names and friend lists
    # load = load_patients(100)
    # for x in load:    # Check the True/False of is_contagious
    #     print(x.first_name, x.last_name, ":")
    #     for y in x.friend_list:
    #         print(y.first_name, y.last_name)
    #     print("\n")

    # for x in all_patients:    # Check the infect function
    #     # x.infect(10)
    #     x.sleep()
    #     print(x.first_name, x.last_name, sep=" ")
    #     # for y in x.friend_list:    # Check their friend list - all patients Person objects in their friend list
    #     #     print(y.first_name)

    # for x in all_patients:    # Check the person's viral load
    #     print(x.viral_load)

    # This is a sample test case. Write your own testing code here.
    # test_result = run_simulation(15, 0.8, 49)
    # print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    # test_result = run_simulation(40, 1, 1)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

# do not add code here (outside the main block).
