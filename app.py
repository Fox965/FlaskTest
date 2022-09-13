from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1> Здраствуй Flask </h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


@app.route('/hello')
def greeting():
    return "<h1> Привет никита </h1> <p> Вторая строка </p>" \
           " <table border='1px solid black' > <tr><th> Моргунов </th> <th> Михаил </th></tr> <tr></tr></table>"


if __name__ == '__main__':
    app.run(debug=True)