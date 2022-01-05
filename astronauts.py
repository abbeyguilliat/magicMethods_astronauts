
class Astronaut:
    '''Astronaut Class'''
    def __init__(self,name,status,hrFlight):
        self.__name = name
        self.__status = status
        self.__flight = int(hrFlight)

    def __str__(self):
        return('%s, %s' % (self.__name,self.__status))
    
    def __gt__(self,other):
        if self.__flight > other.__flight:
            print("__gt__ called: True\n%s's Flight Time: %i hrs > %s's Flight Time: %i hrs!" % (self.__name,self.__flight,other.__name,other.__flight))
        else:
            print("__gt__ called: False")

    def __ge__(self,other):
        if self.__flight > other.__flight or self.__flight == other.__flight:
            print("__ge__ called: True\n%s's Flight Time: %i hrs >= %s's Flight Time: %i hrs!" % (self.__name,self.__flight,other.__name,other.__flight))
        else:
            print("__ge__ called: False")

    def __eq__(self,other):
        if self.__flight == other.__flight:
            print("__eq__ called: True\n%s's Flight Time: %i hrs = %s's Flight Time: %i hrs!" % (self.__name,self.__flight,other.__name,other.__flight))
        else:
            print("__eq__ called: False")

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def flight(self):
        return self.__flight
    @flight.setter
    def flight(self, new_flight):
        self.__flight = new_flight

## PART 3
import csv
import random

astronauts = []
with open("astronauts.csv","r",newline='',encoding="utf-8-sig") as csvfile:
    astronaut_reader = csv.DictReader(csvfile)
    for row in astronaut_reader:
        astronaut = Astronaut(row['Name'],row['Status'],row['Space Flight (hr)'])
        astronauts.append(astronaut)

# listing mutable properties for astronaut object 1
astro0 = astronauts[0]
print("Astronaut Object 1:\n===================")
print(astro0.name)
print(astro0.status)
print(astro0.flight)

# testing magic methods!
astro1 = random.choice(astronauts)
astro2 = random.choice(astronauts)
print("\nComparing Astronauts:\n=====================")
print('+ ' + str(astro1))
print('+ ' + str(astro2))
print("\n")
astro1 > astro2
print("\n")
astro2 > astro1
print("\n")
astro2 >= astro1
print("\n")
astro1 >= astro2
print("\n")
astro1 == astro2
print("\n")

# complete list of astronauts
print("Complete List of Astronauts:\n============================")
for row in astronauts:
    print(row)

## initializes more-detailed astronaut class
# not required for exercise
'''
class Astronaut:
    'Astronaut Class'
    def __init__(self,name,group,status,gender,birthDate,birthPlace,deathDate):
        self.__name = name
        self.__group = group
        self.__status = status
        self.__gender = gender
        self.__birthDate = birthDate
        self.__birthPlace = birthPlace
        self.__deathDate = deathDate
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, new_group):
        self.__group = new_group

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, new_gender):
        self.__gender = new_gender

    @property
    def birthDate(self):
        return self.__birthDate
    @birthDate.setter
    def birthDate(self, new_birthDate):
        self.__birthDate = new_birthDate

    @property
    def birthPlace(self):
        return self.__birthPlace
    @birthPlace.setter
    def birthPlace(self, new_birthPlace):
        self.__birthPlace = new_birthPlace

    @property
    def deathDate(self):
        return self.__deathDate
    @deathDate.setter
    def deathDate(self, new_deathDate):
        self.__deathDate = new_deathDate
'''
