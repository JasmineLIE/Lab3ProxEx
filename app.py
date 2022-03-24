from flask import Flask, request, render_template
import random

starNouns = []
starAdjs = []

with open('txtfiles/stars_nouns.txt', 'r') as f:
  for line in f:
    starNouns.append(line.strip())

with open('txtfiles/stars_adjectives.txt', 'r') as t:
  for line in t:
    starAdjs.append(line.strip())

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])

def index():


        
#--------------USER VISITS-------------------
    # Load current count
    f = open("txtfiles/count.txt", "r")
    count = int(f.read())
    f.close()


    # Increment the count
    count += 1
    
    f = open("txtfiles/count.txt", "w")
    f.write(str(count))
    f.close()

    # Overwrite the count

#--------------USER VISITS-------------------

#--------------STAR GAZING-------------------
    
    f = open("txtfiles/user_stargaze.txt", "r")
    user_stargaze = str(f.read())
    f.close()

    user_stargaze = (starAdjs[random.randint(0, len(starAdjs)-1)]) + "\n" + (starNouns[random.randint(0, len(starNouns)-1)]) 

    f = open("txtfiles/user_stargaze.txt", "w")
    f.write(str(user_stargaze))
    f.close()

    f = open("txtfiles/stargaze.txt", "r")
    stargaze = str(f.read())
    f.close()
    
    
    if count%2==0:
        f = open("txtfiles/stargaze.txt", "w")
        f.write(str(user_stargaze))
        f.close()

#--------------STAR GAZING-------------------

#--------------SMORES-------------------




    f = open("txtfiles/smore.txt", "r")
    smore = str(f.read())
    f.close()
    if request.method == 'POST':
        if request.form.get('action1') == 'Classic Graham':


            smore = "Graham Classic"
    
            f = open("txtfiles/smore.txt", "w")
            f.write(str(smore))
            f.close()
        elif  request.form.get('action2') == 'Strawberry':
            smore = "Strawberry"
            f = open("txtfiles/smore.txt", "w")
            f.write(str(smore))
            f.close()
        elif  request.form.get('action3') == 'Minty':
            smore = "Minty"
            f = open("txtfiles/smore.txt", "w")
            f.write(str(smore))
            f.close()
        elif  request.form.get('action4') == 'Jumbo Marshmellow':
            smore = "Jumbo Marshmellow"
            f = open("txtfiles/smore.txt", "w")
            f.write(str(smore))
            f.close()
        elif  request.form.get('action5') == 'Triple Chocolate':
            smore = "Triple Chocolate"
            f = open("txtfiles/smore.txt", "w")
            f.write(str(smore))
            f.close()
    elif request.method == 'GET':

        
        return render_template('index.html', count=count, user_stargaze=user_stargaze, stargaze=stargaze, smore=smore)

#--------------SMORES-------------------
    # Render HTML with count variable
    return render_template("index.html", count=count, user_stargaze=user_stargaze, stargaze=stargaze, smore=smore)



if __name__ == "__main__":
    app.run()

