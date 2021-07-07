import os
import csv
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def graph_first_names():
    open("first_names.csv", "w")
    first_names = []
    with open('datasett.csv', newline='') as datasett:
        reader = csv.reader(datasett, delimiter=',', quotechar='|')
        for row in reader:
            first_names.append(row[1])
    first_names.remove(r"name/first")
    first_name_set = set()
    for first_name in first_names:
        first_name_set.add(first_name)
    first_name_set_list = []
    for first_name in first_name_set:
        first_name_set_list.append(first_name)
    first_name_set_list.sort()
    first_name_occurrences = []
    for first_name in first_name_set_list:
        counter = 0
        for ffirst_name in first_names:
            if (ffirst_name == first_name):
                counter += 1
        first_name_occurrences.append(counter)
    print(first_name_occurrences)
    print(first_name_set_list)
    fig = plt.figure(figsize=(100, 6))
    plt.plot(first_name_set_list, first_name_occurrences)
    plt.tight_layout()
    plt.xticks(rotation=90)
    plt.show()


def graph_ages():
    open("ages.csv", "w")
    ages = []
    with open('datasett.csv', newline='') as datasett:
        reader = csv.reader(datasett, delimiter=',', quotechar='|')
        #for i, row in enumerate(reader):
        for row in reader:
            ages.append(row[3])
    ages.remove("age")
    age_set = set()
    for age in ages:
        age_set.add(age)
    age_set_list = []
    for age in age_set:
        age_set_list.append(age)
    age_set_list.sort()
    age_occurrences = []
    for age in age_set_list:
        counter = 0
        for aage in ages:
            if (aage == age):
                counter += 1
        age_occurrences.append(counter)
    print(age_occurrences)
    print(age_set_list)
    fig = plt.figure(figsize=(12, 6))
    plt.plot(age_set_list, age_occurrences)
    plt.tight_layout()
    plt.show()


def graph_locations():
    open("locations.csv", "w")
    lat = []
    lon = []
    locations = []
    with open('datasett.csv', newline='') as datasett:
        reader = csv.reader(datasett, delimiter=',', quotechar='|')
        for row in reader[1:]:
            lat.append(row[7])
            lon.append(row[8])
            locations.append(row[7] + "," + row[8])
    locations.remove("latitude,longitude")
    data = {'latitude': [lat[2]], 'longitude': [lon[2]]}
    df = pd.DataFrame(data)
    print(df)
    fig = px.scatter_geo(df, lat="latitude", lon="longitude")
    fig.show()
