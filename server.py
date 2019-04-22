"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
      <head>
          <title>Hi There!</title>
      </head>
      <body>
        Hi! This is the home page. <a href ="/hello"> Hello Link</a>
      </body>
    </html> """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? Choose a compliment.<input type="text" name="person">
          <select name = "complimente">
            <option value="awesome"> Awesome</option>
            <option value="terrific"> Terrific</option>
            <option value="fantastic"> Fantastic</option>
            <option value="neato"> Neato</option>
            <option value="fantabulous"> Fantabulous</option>
            <option value="wowza"> Wowza</option>
            <option value="oh-so-not-meh"> Oh-so-not-meh</option>
            <option value="brilliant"> Brilliant</option>
            <option value="ducky"> Ducky</option>
            <option value="coolio"> Coolio</option>
          </select>
          <input type="submit" value="Submit"> <br><br>
        </form> <form action="/diss">
          What's your name? Choose an insult. <input type="text" name="person">
          <select name = "insults">
            <option value="archloch"> Archloch</option>
            <option value="terrible"> Terrible</option>
            <option value="horrible"> Horrible</option>
          </select>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""
    complimente = request.args.get('complimente')
    player = request.args.get("person")


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {complimente}!
      </body>
    </html>
    """

@app.route("/diss")
def insult_person():
    insults = request.args.get("insults")
    player = request.args.get("person")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player,insults)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
