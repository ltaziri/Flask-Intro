from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return  """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        Click <a href = "/hello">here</a> to continue.
      </body>
    </html>
    """

    


@app.route('/hello')
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

        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          Select an insult: 
          <input type="radio" name="diss" value="forgetful">Forgetful 
          <input type="radio" name="diss" value="lame">Lame       
          <input type="radio" name="diss" value="awkward">Awkward
          <input type="radio" name="diss" value="annoying">Annoying
          <input type="radio" name="diss" value="irritating">Irritating
          <input type="submit">
        </form>
      </body>
    </html>
    """
        # <form action="/greet">
        #   <label>What's your name? <input type="text" name="person"></label>
        #   <br>
        #   Select a compliment: 
        #   <input type="radio" name="comp" value="awesome">Awesome
        #   <input type="radio" name="comp" value="terrific">Terrific       
        #   <input type="radio" name="comp" value="fantastic">Fantastic
        #   <input type="radio" name="comp" value="neato">Neato
        #   <input type="radio" name="comp" value="fantabulous">Fantabulous
        #   <input type="submit">
        # </form>

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("comp")

    # compliment = choice(AWESOMENESS)
   
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    insult = request.args.get("diss")

    # compliment = choice(AWESOMENESS)
   
    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
