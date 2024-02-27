from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
@app.route('/<title>')
def main(title):
    return render_template('home.html', title=title)

if __name__ == '__main__':
    app.run()
