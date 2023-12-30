from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def typing_speed_test():
    return render_template('typetest.html')

if __name__ == '__main__':
    app.run(debug=True)