from flask import Flask, render_template, Response, request


app = Flask(__name__)


@app.route("/")


def index():
   
    # Load current count
    f = open("marshmellow.txt", "r")
    marshmellowCount = int(f.read())
    f.close()
    
    # Overwrite the count
    f = open("marshmellow.txt", "w")
    f.write(str(count))
    f.close()


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

    # Render HTML with count variable
    return render_template("index.html", count=count, marshmellowCount=marshmellowCount)


if __name__ == "__main__":
    app.run()

