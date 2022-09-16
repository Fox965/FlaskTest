from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1> Здраствуй Flask </h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


@app.route('/center')
def center():
    return "<h1> <center>текст в центре </center></h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


@app.route('/i')
def i():
    return "<h1> <i>текст курсивный </i></h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


@app.route('/right')
def right():
    return "<h1> <p align=right>текст справа </p></h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


if __name__ == '__main__':
    app.run(debug=True)
