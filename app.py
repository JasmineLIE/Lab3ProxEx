from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        m = open("marshmellow.txt", "r")
        marshmellowCount = int(m.read())
        m.close()
        marshmellowCount+=1
        m = open("marshmellow.txt", "w")
        m.write(str(marshmellowCount))
        m.close()
    return render_template("index.html", marshmellowCount=marshmellowCount)

@app.route("/")


def index():
   



    



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
    return render_template("index.html", count=count)


if __name__ == "__main__":
    app.run()

