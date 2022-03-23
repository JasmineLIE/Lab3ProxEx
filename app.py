from flask import Flask, render_template
import random

starNouns = []
starAdjs = []

with open('stars_nouns.txt', 'r') as f:
  for line in f:
    starNouns.append(line.strip())

with open('stars_adjectives.txt', 'r') as t:
  for line in t:
    starAdjs.append(line.strip())

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])


def index():

#--------------USER VISITS-------------------
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()


    # Increment the count
    count += 1


    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
#--------------USER VISITS-------------------

#--------------STAR GAZING-------------------
    
    f = open("user_stargaze.txt", "r")
    user_stargaze = str(f.read())
    f.close()

    user_stargaze = (starAdjs[random.randint(0, len(starAdjs)-1)]) + "\n" + (starNouns[random.randint(0, len(starNouns)-1)]) 

    f = open("user_stargaze.txt", "w")
    f.write(str(user_stargaze))
    f.close()

    f = open("stargaze.txt", "r")
    stargaze = str(f.read())
    f.close()
    
    
    if count%2==0:
        f = open("stargaze.txt", "w")
        f.write(str(user_stargaze))
        f.close()

#--------------STAR GAZING-------------------

#--------------MARSHMELLOWS-------------------

#--------------MARSHMELLOWS-------------------



    # Render HTML with count variable
    return render_template("index.html", count=count, user_stargaze=user_stargaze, stargaze=stargaze)


if __name__ == "__main__":
    app.run()

