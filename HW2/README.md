# PUI2015_saf537_hw2
###Homework #2 for Principles of Urban Informatics###

This exercise consists in retrieving information from the MTA buses service via its api, using json format and practicing how to export results to .csv files. For accessing the data, a user key needed to be generated. Note that in both assignments the Key needs to be used in the input line, because the code will be retrieving the real data via internet.

#####Assignment 1#####

Run the following command: "python show_bus_locations.py e92f290b-c495-4836-a7b3-df9446bad55d bus" where "bus" is the name of the route. Some examples are: M7, B52 and B67.

This will return the location of each of the buses that are currently working for the selected route.

#####Assignment 2#####

Run the following command "get_bus_info.py e92f290b-c495-4836-a7b3-df9446bad55d bus bus.csv" where "bus" is the name of the route. Some examples are: M7, B52 and B67.

This will return a .csv file named as the route (if you make sure to use the command right: for example "get_bus_info.py KEY M7 M7.csv") with the location of each bus, the name of its next stop and how far the bus is from the stop.

