"""
Author: Daniel John McArthur

This function creates the Person class, and then reads our starting list, "sample_set.txt". This will then
define each person in our population, their friends and store them into a list for use in the simulation.
"""

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = str(first_name)  # This is the person's first name
        self.last_name = str(last_name)  # This is the person's last name
        self.friend_list = []  # This is the person's list of friends (other person objects)

    def add_friend(self, friend_person):
        # This will add another person class to this person's friend list
        self.friend_list.append(friend_person)

    def get_name(self):
        # This method returns a string containing the person's first and last name concatenated together
        print(str(self.first_name) + " " + str(self.last_name))

    def get_friends(self):
        return self.friend_list
        # for x in self.friend_list:
        #     print(x.first_name + " " + x.last_name)


def load_people():
    sample_set_open = open("sample_set.txt", "r")
    sample_set = sample_set_open.read().splitlines()
    all_persons = []  # This is the list of all person objects created from a2_sample_set.txt

    # This goes through each line in the sample_set.txt and takes the first person of each line and creates an object
    for x in sample_set:
        x.strip("\n")
        person_name = x.split(": ")[0]  # Takes the string before the :
        person_object = Person(person_name.split(" ")[0], person_name.split(" ")[1])    # Creates Person object
        all_persons.append(person_object)  # Adds the created person to the all_persons list
        # print(person_object.__dict__)

    # All persons are now defined, this goes back through the sample_set and adds friends to the persons
    for y in sample_set:  # For each line from the sample_set
        y.strip("\n")  # Get rid of the new line
        person_name = y.split(": ")  # Takes the string before the ": " this will be the parent object
        person_fname = person_name[0].split(" ")[0]  # Creates the first name for this person
        person_lname = person_name[0].split(" ")[1]

        # This creates a list with each element a string of the friend's name
        friend_strlist = person_name[1].split(", ")
        print(friend_strlist)

        # I have the person's name: person_fname and a list(friend_list[]) with each friend's first name
        for k in all_persons:  # For every person object:
            if k.first_name == person_fname and k.last_name == person_lname:  # Verifies correct person
                for x in all_persons:  # For any of the persons in the all_persons list
                    if x in k.friend_list:  # If they are in the friend list already, break
                        break
                    else:
                        for f in friend_strlist:    # Verifies the friend person with the string from sample_set
                            if f.split(" ")[0] == x.first_name and f.split(" ")[1] == x.last_name:
                                k.add_friend(x)
    sample_set_open.close()

    # Debug:
    # print("\n")
    # for x in all_persons:
    #     print(x.__dict__)
    #     x.get_name()
    #     x.get_friends()
    #
    # for x in all_persons:
    #     print(len(x.friend_list))
    #
    # print(len(all_persons))
    return all_persons  # Returns the all_people list with all person objects and their friend_lists filled


if __name__ == '__main__':
    all_persons = load_people()
    print(str(len(all_persons)) + " people in the list")
    for x in all_persons:
        print(x.first_name, ":")
        for y in x.friend_list:
            print(y.first_name, y.last_name)
        print("\n")
    pass


