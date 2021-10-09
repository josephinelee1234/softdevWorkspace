# The Penguins | Josephine Lee (Kitty), Qina Liu (Minx), Roshani Shrestha (Pete)
# SoftDev
# K13: Template for Success - Serves a templated page
# 2021-10-08

import random
import os
from flask import Flask, render_template 
app = Flask(__name__);

@app.route("/")
def hello_world():
    file = open("data/occupations.csv")
    lines = file.read().split("\n");
    del lines[0]; #Remove "Job Class, Percentage" line
    split = [];
    for i in lines:
        if "," in i:
            #remove quotes, split string into job and %, then convert % to float
            i = i.replace("\"","");
            comma = i.rsplit(",",1);
            comma[1] = float(comma[1]);
            #add to necessary arrays
            split.append(comma);

    del split[len(split)-1]; # Remove "Total" as a job
    dictionary = dict(split)
    
    return dictionary

def chooseOccupation():
    file = open("data/occupations.csv")
    lines = file.read().split("\n");
    del lines[0]; #Remove "Job Class, Percentage" line
    split = [];
    for i in lines:
        if "," in i:
            #remove quotes, split string into job and %, then convert % to float
            i = i.replace("\"","");
            comma = i.rsplit(",",1);
            comma[1] = float(comma[1]);
            #add to necessary arrays
            split.append(comma);

    del split[len(split)-1]; # Remove "Total" as a job
    dictionary = dict(split)
    return (random.choices(list(dictionary), weights=dictionary.values()))[0]
# @app.route("/")
# def hello_world():
#     return "No hablo queso!"

@app.route("/tablified_template") 
def test_tmplt():
    return render_template( 'tablified.html', foo="K13: Template for Success", occupations=hello_world(), occupationChosen = chooseOccupation())

if __name__ == "__main__":
    app.debug = True
    app.run()