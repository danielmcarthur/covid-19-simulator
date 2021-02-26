# COVID-19 Python Simulator

## 1. Introduction

The intention of this project was to simulate the ways in which social distancing restrictions can affect the spread of a contagious virus. 

The simulation consists of 200 persons, each with their own list of 'close contacts'. Our starting point is a .txt file with the names of each person and their close contacts. Our Python function creates custom class objects representing each person and assigns relevant attributes such as name, close contacts, health score, infectious(T/F). Withnin the population is a designated 'patient zero' who is the infected person and can transmit the virus to others. 

The simulation is run over a desired amount of days and the restrictions level (determined by probability of meeting close contacts). Each day, if the infected person has met with close contacts then the disease has a chance of being transmitted. Finally, the results of the run simulation are graphed using matplotlib. 

## 2. Video Explanation

I've recorded an explanation video of this project, which you can watch on Vimeo. 

[![You can watch my video explanation here](https://i.vimeocdn.com/video/1016431723.webp?mw=1100&mh=591)](https://vimeo.com/491460076)

<p><a href="https://vimeo.com/491460076" target="_blank">Daniel McArthur | Python Project | COVID-19 Spread Simulator</a> from <a href="https://vimeo.com/user129314614">Daniel McArthur</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

All work shown in this video has been completed by myself, Daniel McArthur in Python using PyCharm CE environment.

## 3. Specific Skills

* Creation of custom class objects in Python
* Creation of parent and child class objects
* Use of created functions
* Graphing simulation results using the `matplotlib` package

## 4. Method

Our starting point consisted of a text file containing 200 persons with their list of close contacts. This file was read and custom person classes were made as our participants in the simulation's population. 

> Snapshot of input .txt file
```
Ethel Beerman: Ina Donley, Halina Hamby, Shenita Boso
Ossie Digangi: Stefany Crotty, Voncile Kilduff, Song Grigg, Sindy Worley, Gill Bates, Halina Hamby
Dina Seegmiller: Claudia Mcginn, Vicenta Seidel
Farah Courchesne: Siu Buscher
Vertie Lunceford: Cathleen Healey, Kena Redwood, Arcelia Sitz
Brenda Lefkowitz: Stefany Crotty, Cliff Ayala, Lorene Straub, Rosaura Perrino, Cleora Hoch
Carno Start: Federico Rheaume, Perry Lachermeier
```

Each of these persons from our input list were created into a "Person" object, which we defined using a custom class object. Each "Person" had several attributes and functions important to the virus simulation. 

> Custom class object for each Person in the population
```python
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
```

In order to create the effect of viral spread, a parent class of the Person class object was used. The "Patient" had several more attributes relevant to their health and the virus. 

```python
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

    def is_contagious(self): # A person is contagious if their health is <= 49
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
```

The simulation was run over several days, with the likelihood of each patient visiting their close contacts determined by the defined restrictions. In this way, we were able to visualise the varying ways that the virus can spread given eased or strict social distancing measures.

## 5. Conclusions

This was a needed exercise in the use of Python class objects, for and if/else statements, graphing with matplotlib and function creation. Given this was my first ever Python project, it was quite a challenge and took some time. However, my learning in the use of such methods is highly beneficial and I have used these techniques since this project. 

Whilst this was quite a simple simulation of a virus' spread, its message aligns with the messages released by health officials not only in Australia, but around the world. The COVID-19 virus is able to spread rapidly and social distancing measures are effective in slowing this effect. In a real world scenario, many more variables would contribute to the spread of a virus than we have in this simulation. Regardless, this was a worthwhile exercise. 
