import csv
import flask
import printModule
import writeModule
import graphModule
import pandas
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

print("""
    Welcome to the Brutus Data Processing Program (BDPP).
    Type "help" for help using the program.
    """)

while True:
    CLI = input("> ").lower()
    CLI_list = CLI.split()

    if (not CLI):
        continue

    if ("help" in CLI):
        print("""
        This program is a data processing and visualization program made for Brutus A/S.
        Type "man name" with name being the name of a command for more information.
        It supports many commands such as:
        
        print_line [-c column]
        append_line [-f file] [-d data]
        graph [-c column]
        print...
        etc...
        """)
    elif (CLI_list[0] == "print_line" or CLI_list[0] == "append_lines" or CLI_list[0] == "graph"):
        break
    else:
        print("Sorry, no valid command found.\nType \"help\" for more information.")

#run_print_line = False

#ages = []
first_names = []
last_names = []
streets = []
cities = []
states = []
latitudes = []
longitudes = []
ccnumbers = []


if (CLI_list[0] == "print_line"):
    #run_print_line = True
    #print(32)
    if (len(CLI_list) >= 3):
        printModule.print_line(CLI_list[2])
    else:
        printModule.print_line()

if (CLI_list[0] == "append_lines"):
    if (len(CLI_list) >= 3):
        if (CLI_list[1] == "-f"):
            writeModule.append_lines(file_name=CLI_list[2])
        elif (CLI_list[1] == "-d"):
            writeModule.append_lines(read_data=CLI_list[2])


if (CLI_list[0] == "graph"):
    if (CLI_list[2] == "ages"):
        graphModule.graph_ages()
    elif (CLI_list[2] == "first_names"):
        graphModule.graph_first_names()
    elif (CLI_list[2] == "locations"):
        graphModule.graph_locations()
    else:
        pass
        # Graph what?

