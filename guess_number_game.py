import random
from flask import Flask

app = Flask(__name__)


def creat_number():
    number = random.randrange(1, 10)
    return number


get_number = creat_number()

@app.route('/')
def hello():
    return '<h1>Welcome</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500px>'


@app.route('/<int:number>')
def guess_page(number):
    if number > get_number:
        return '<h1>Too Hight</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500px>'
    elif number < get_number:
        return '<h1>Too Low</h2>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500px>'
    else:
        return "<h1>You are right~</h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500px>'


if __name__ == "__main__":
    app.run(debug=True)

