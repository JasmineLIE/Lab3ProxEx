from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)

@app.route("/")


def index():
   

    m = open("marshmellow.txt", "r")
    marshmellowCount = int(m.read())
    m.close()

    @app.route("/roast/", methods=['POST'])
    def roastButtonClick():
        marshmellowCount +=1
        return render_template('index.html', marshmellowCount=marshmellowCount)

    m - open("marshmellow.txt", "w")
    m.write(str(marshmellowCount))
    m.close()

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