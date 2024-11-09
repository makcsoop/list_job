from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Заготовка"
    return render_template('base.html', title=user)

@app.route('/training/<prof>')
def main(prof):
    return render_template('training.html', )

@app.route('/list_prof/<format>')
def prof(format):
    roob = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог']
    return render_template('list_prof.html', format=format, job=roob)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
    #dfgbgfdfgb