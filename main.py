from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        result = "<u>" + function() + "</u>"
        return result
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media2.giphy.com/media/2LbaBjoSAays/200w.webp?cid=ecf05e4733l7gexcgsrmi64z9k32mhzccwwizttvkqgog4k0&rid=200w.webp&ct=g" width=200px>' \


@app.route("/bye")
@make_emphasis
@make_underlined
@make_bold
def bye():
    return "Bye~"

@app.route("/username/<names>/<int:number>")
def greet(names, number):
    return f"Good night {names}! you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)

