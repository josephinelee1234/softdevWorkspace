# The Penguins | Josephine Lee (Kitty), Qina Liu (Nyx), Roshani Shrestha (Pete)
# SoftDev
# K13: Template for Success - Serves a templated page
# 2021-10-08

import random
import os
from flask import Flask, render_template 
app = Flask(__name__);

@app.route("/")
def make_dict():
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

def rand_occ(dictionary):
    return random.choices(list(dictionary), weights=dictionary.values())[0]

# @app.route("/")
# def hello_world():
#     return "No hablo queso!"

dictionary = make_dict()
team = "The Penguins: Josephine Lee (Kitty), Qina Liu (Nyx), and Roshani Shrestha (Pete)" 
header = "This program displays a random occupation at the top of the page using occupations.csv. It also displays a tablified version of the occupations."
@app.route("/tablified_template") 
def test_tmplt():
    return render_template( 'tablified.html', foo="K13: Template for Success", occupation=rand_occ(dictionary), occupations=dictionary, team=team, header=header) 

if __name__ == "__main__":
    app.debug = True
    app.run()
